import random
from model.names import foodNames
from model.names import merchNames
from model.names import merchColors
from model.names import stadiumNames
from model.names import gameNames


class Model:
    def __init__(self):
        self.sportGame = SportGame()


class SportGame:
    def __init__(self):
        self.fan = None
        self.fans = []
        self.stadiums = [Stadium(random.choice(stadiumNames), random.choice(gameNames), random.randrange(40, 100), random.randrange(60, 181)) for i in range(3)]

    def newProfile(self, profile):
        self.fans.append(profile)
        self.fan = profile


class Fan:
    def __init__(self, name, money, login, password):
        self.name = name
        self.money = money
        self.login = login
        self.password = password
        self.visitedGames = []


class Stadium:
    def __init__(self, name, game, capacity, time):
        self.name = name
        self.game = game
        self.capacity = capacity
        self.tickets = self._createTickets()
        self.availableTickets = self.tickets
        self.income = 0
        self.time = time
        self.shop = Shop()


    def _createTickets(self):
        number = [i + 1 for i in range(self.capacity)]
        ticket = []
        date = str(random.randrange(1, 31)) + '/' + str(random.randrange(1, 13))
        time = str(random.randrange(6, 23)) + ':' + str(random.randrange(1, 6)) + '0'
        ticket.append(Ticket(date, time, random.randrange(10, 30), self.name) for i in range(self.capacity // 3))
        ticket.append(Ticket(date, time, random.randrange(100, 200), self.name) for i in range(self.capacity // 3))
        ticket.append(Ticket(date, time, random.randrange(30, 100), self.name) for i in range(self.capacity - 2 * self.capacity // 3))
        return dict(zip(number, ticket))

    def buy(self, num):
        self.income += self.tickets[num].price
        return self.availableTickets.pop(num)



class Ticket:
    def __init__(self, date, time, price, place):
        self.date = date
        self.time = time
        self.price = price
        self.place = place


class Shop:
    def __init__(self):
        self.food = [Food(random.choice(foodNames), random.randrange(5, 15)) for i in range(6)]
        self.merch = [Merch(random.choice(merchNames), random.randrange(5, 15), random.choice(merchColors)) for i in range(6)]
        self.income = 0

    def buy(self, product):
        if self.food.count(product) == 1 or self.merch.count(product) == 1:
            self.income += product.price


class Product:
    def __init__(self, price):
        self.price = price


class Food(Product):
    def __init__(self, name, price):
        super().__init__(price)
        self.name = name


class Merch(Product):
    def __init__(self, name, price, color):
        super().__init__(price)
        self.name = name
        self.color = color
