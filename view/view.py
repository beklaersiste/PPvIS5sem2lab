from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


class Manager(ScreenManager):
    pass


class View(MDApp):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.model = controller.model

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        Builder.load_file("view/ui.kv")
        return Manager()

    def newProfile(self):
        self.controller.newProfile(self.root.ids.name.text, self.root.ids.money.text, self.root.ids.login.text, self.root.ids.password.text)


