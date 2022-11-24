from model.model import Model
from view.view import View
from controller.controller import Controller


class Main:
    def __init__(self):
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.controller)

    def build(self):
        self.view.run()


if __name__ == '__main__':
    mvc = Main()
    mvc.build()
