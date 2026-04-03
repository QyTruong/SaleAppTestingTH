from eapp.dao import add_user
from eapp.test.test_base import test_session, test_app, mock_cloudinary
from eapp.models import User
import hashlib
import pytest

@pytest.mark.parametrize('name, username, password', [
    ('aaaaaaaa', 'bbbbbbbbbbbb', 'abc12341234')
])
def test_register_success(name, username, password, test_session):
    add_user(name=name, username=username, password=password, avatar=None)

    u = User.query.filter(User.username.__eq__(username)).first()

    assert u is not None
    assert u.name == name
    assert u.password == str(hashlib.md5(password.encode('utf-8')).hexdigest())



@pytest.mark.parametrize('name, username, password, avatar', [
    ('aaaaaaaa', 'bbbbbbbbbbbb', 'abc12341234', 'aaaa'),
])
def test_avatar(name, username, password, avatar, test_session, mock_cloudinary):
    add_user(name=name, username=username, password=password, avatar=avatar)

    u = User.query.filter(User.username.__eq__(username)).first()

    assert u is not None
    assert u.name == name
    assert u.password == str(hashlib.md5(password.encode('utf-8')).hexdigest())
    assert u.avatar == 'http://fake-image.png'