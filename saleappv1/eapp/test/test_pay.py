from eapp.models import User
from eapp.test.test_base import test_app, test_client

def test_pay_success(test_client, mocker):
    class FakeUser:
        is_authenticated = True

    mocker.patch("flask_login.utils._get_user", return_value=FakeUser())

    mocker.patch("eapp.dao.current_user", new=FakeUser())

    with test_client.session_transaction() as sess:
        sess['cart'] = {
            "1": {
                "id": "1",
                "name": "hello",
                "price": 1000,
                "quantity": 3
            }
        }

    mock_add = mocker.patch("eapp.dao.add_receipt")

    res = test_client.post("/api/pay")
    data = res.get_json()

    assert data["status"] == 200
    with test_client.session_transaction() as sess:
        assert 'cart' not in sess

    mock_add.assert_called_once()


def test_pay_fail(test_client, mocker):
    class FakeUser:
        is_authenticated = True

    mocker.patch("flask_login.utils._get_user", return_value=FakeUser())

    mocker.patch("eapp.dao.current_user", new=FakeUser())

    with test_client.session_transaction() as sess:
        sess['cart'] = {
            "1": {
                "id": "1",
                "name": "hello",
                "price": 1000,
                "quantity": 3
            }
        }

    mock_add = (
        mocker.patch("eapp.dao.add_receipt", side_effect=Exception('db error')))

    res = test_client.post("/api/pay")
    data = res.get_json()

    assert data["status"] == 400
    assert data["err_msg"] == 'db error'
    with test_client.session_transaction() as sess:
        assert 'cart' in sess

    mock_add.assert_called_once()



