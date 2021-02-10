# libraries
# alt + shift + l
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from scrapper import scrapper
from datetime import datetime
from kivy.uix.image import Image
import json

# main program
Builder.load_file("design.kv")


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.current = "sign_up_screen"


    def login(self, username, pword):
        with open("login.json") as file:
            user = json.load(file)
        if username in user and user[username]["password"] == pword:
            self.manager.current = "login_almost_success"
        else:
            self.ids.login_wrong.text = "Wrong password"


class SignUpScreen(Screen):
    def sign_up_list(self, uname, pword):
        with open("login.json") as file:
            user = json.load(file)

        user[uname] = {"username": uname, "password": pword,
                       "date": datetime.now().strftime("%Y-%M-%D %h-%M-%S")}

        with open("login.json", "w") as file:
            json.dump(user, file)
        self.manager.current = "login_almost_success"


class LoginAlmostSuccess(Screen):
    def person(self, person):
        scrapper(person)
        self.manager.current = "login_success"


class LoginSuccess(Screen):
    print(Image(source="hollyh16.jpg"))

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
