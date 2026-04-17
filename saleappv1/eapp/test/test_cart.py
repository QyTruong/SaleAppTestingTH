from eapp.test.test_base import test_app, test_client

def test_add_to_cart_success(test_client):
    test_client.post("/api/carts", json={
        "id": 1,
        "name": "Laptop",
        "price": 1000
    })

    res = test_client.post("/api/carts", json={
        "id": 1,
        "name": "Laptop",
        "price": 1000
    })

    data = res.get_json()
    assert data["total_quantity"] == 2
    assert data["total_amount"] == 2000


def test_add_to_cart_increase(test_client):
    test_client.post("/api/carts", json={
        "id": 1,
        "name": "iPhone",
        "price": 1000
    })
    test_client.post("/api/carts", json={
        "id": 1,
        "name": "iPhone",
        "price": 1000
    })
    res = test_client.post("/api/carts", json={
        "id": 2,
        "name": "Galaxy",
        "price": 2000
    })

    data = res.get_json()

    assert data["total_quantity"] == 3
    assert data["total_amount"] == 4000


def test_existing_item(test_client):
    with test_client.session_transaction() as sess:
        sess['cart'] = {
            "1": {
                "id": "1",
                "name": "abcdef",
                "price": 1000,
                "quantity": 2
            }
        }

    res = test_client.post("/api/carts", json={
        "id": 1,
        "name": "iGalaPhone",
        "price": 1000
    })

    data = res.get_json()

    assert data["total_quantity"] == 3

    with test_client.session_transaction() as sess:
        assert sess['cart']['1']['quantity'] == 3


def test_update_cart(test_client):
    with test_client.session_transaction() as sess:
        sess['cart'] = {
            "1": {
                "id": "1",
                "name": "abcdef",
                "price": 1000,
                "quantity": 2
            }
        }

    res = test_client.put("/api/carts/1", json={
        "quantity": 12
    })

    data = res.get_json()

    assert data['total_quantity'] == 12
    assert data['total_amount'] == 12000

    with test_client.session_transaction() as sess:
        assert len(sess['cart']) == 1


def test_delete_cart(test_client):
    with test_client.session_transaction() as sess:
        sess['cart'] = {
            "1": {
                "id": "1",
                "name": "abcdef",
                "price": 1000,
                "quantity": 2
            },

            "2": {
                "id": "2",
                "name": "xyz",
                "price": 2000,
                "quantity": 4
            }
        }

    res = test_client.delete("/api/carts/1")

    data = res.get_json()

    assert data['total_quantity'] == 4
    assert data['total_amount'] == 8000

    with test_client.session_transaction() as sess:
        assert len(sess['cart']) == 1
        assert "1" not in sess['cart']