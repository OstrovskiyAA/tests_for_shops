"""
Протестируйте классы из модуля homework/models.py
"""
import dataclasses

import pytest

from models import Product
from models import Cart

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(111) == True, 'На складе отсутствует столько товара'
        assert product.check_quantity(product.quantity)
        assert product.check_quantity(product.quantity + 1) is False
        # TODO напишите проверки на метод check_quantity

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(25)
        assert product.quantity == 975

        product.buy(75)
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:

    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):
        print()
        cart.add_product(product, 6)
        assert cart.products == {product:6}

        cart.add_product(product, 6)
        assert cart.products == {product:12}

    def test_remove_product(self, cart, product):
        cart.add_product(product, 6)
        cart.remove_product(product, 1)
        assert cart.products == {product: 5}

        cart.remove_product(product)
        assert cart.products == {}

        cart.add_product(product, 8)
        cart.remove_product(product, 20)
        assert cart.products == {}

    def test_clear(self,cart, product):
        cart.add_product(product, 8)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self,cart, product):
        assert cart.get_total_price(product, 75) == product.price * 75

    def test_buy(self, cart, product):
        cart.buy(product,75)
        assert product.quantity == 925

    def test_product_buy_more_than_available(self, cart, product):
        with pytest.raises(ValueError):
            cart.buy(product, 1001)