
class Method:
    name:str
    email:str
    def __init__(self,name, email):
        self.name = name
        self.email = email
    def show_info(self) -> str:
        return f'{self.name} - {self.email}'
    @classmethod
    def get_info_class(cls, data):
        name, email = data
        return cls(name, email)
    @staticmethod
    def get_info_static(self):
        return f'{self.name} - {self.email}'
data=['Alex', 'd.d.date@mail.com']
user2= Method.get_info_class(data)
print(user2.show_info())

user = Method(name='Lesha', email='a.a.r@.ru')
print(user.show_info())
print(user.get_info_static(user))




class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity

        # """
        # TODO Верните True если количество продукта больше или равно запрашиваемому
        #     и False в обратном случае
        # """


    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity = self.quantity - quantity
        else:
            raise ValueError('Продуктов не хватает')
        # """
        # TODO реализуйте метод покупки
        #     Проверьте количество продукта используя метод check_quantity
        #     Если продуктов не хватает, то выбросите исключение ValueError
        # """



    def __hash__(self):
        return hash(self.name + self.description)


class Cart():
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] = self.products[product] + buy_count
            print(f' Если в корзине уже что то было {self.products}')
        else:
            self.products[product] = buy_count
            print(f'Если в корзине ничего не было - {self.products}')
        # """
        # Метод добавления продукта в корзину.
        # Если продукт уже есть в корзине, то увеличиваем количество
        # """
        # raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None:
            print('Ничего не передали для удаления')
            self.products = {}
        elif remove_count >= self.products[product]:
            print('Количество для удаления больше')
            del self.products[product]
        else:
            print('Удаляем необходимое количество')
            self.products[product] = self.products[product] -remove_count
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        # raise NotImplementedError

    def clear(self):
        self.products.clear()

    def get_total_price(self, product: Product, quantity) -> float:
        dict = product.__dict__
        price=0
        if quantity <= dict['quantity']:
            dict['quantity']= dict['quantity'] - quantity
            print(f'Поздравляем вы купили {quantity} шт {dict['name']}')
            price = dict['price'] * quantity
            return price
        else:
            raise ValueError('Продуктов не хватает')


    def buy(self, product: Product, quantity: int):
        dict = product.__dict__
        if quantity <= dict['quantity']:
            dict['quantity']= dict['quantity'] - quantity
            print(f'Поздравляем вы купили {quantity} шт {dict['name']}')
            self.clear()
        else:
            raise ValueError('Продуктов не хватает')
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
