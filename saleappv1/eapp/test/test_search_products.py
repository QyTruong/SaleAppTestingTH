from eapp.dao import load_products
from eapp.test.test_base import sample_products, test_session, test_app
import pytest


def test_all(sample_products):
    actual_products = load_products()

    assert len(actual_products) == len(sample_products)


def test_keyword(sample_products):
    actual_products = load_products(kw='iPhone')

    assert len(actual_products) == 3
    assert all('iPhone' in p.name for p in actual_products)



def test_paging(sample_products):
    actual_products = load_products(page=1)

    assert len(actual_products) == 2

    actual_products = load_products(page=3)

    assert len(actual_products) == 1


def test_cate(sample_products):
    actual_products = load_products(cate_id=1)

    assert len(actual_products) == 2

    actual_products = load_products(cate_id=2)

    assert len(actual_products) == 3

@pytest.mark.parametrize('page, kw, expected', [
    (2, 'iPhone', 1), (1, 'iPhone', 2), (3,'iPhone', 0),
    (1, 'samsung', 1), (2, 'samsung', 0), (3, 'samsung', 0),
    (1, 'iPad', 1), (2, 'iPad', 0), (3, 'iPad', 0)
])
def test_kw_paging(sample_products, page, kw, expected):
    actual_products = load_products(page=page, kw=kw)

    assert len(actual_products) == expected
    assert all(kw in p.name for p in actual_products)


@pytest.mark.parametrize('kw, cate_id, expected', [

])
def test_kw_cate(sample_products, kw, cate_id, expected):
    assert load_products(kw=kw, cate_id=cate_id) == expected


@pytest.mark.parametrize('page, cate_id, expected', [

])
def test_page_cate(sample_products, page, cate_id, expected):
    assert load_products(page=page, cate_id=cate_id) == expected