import glob
import json
import random
import string
from datetime import datetime
from pathlib import *

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

from hoverable import HoverBehavior

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]["password"] == pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.wrong_pword.text = "Wrong username or password"


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        incorrect = False
        for symbols in string.punctuation:
            if symbols in uname:
                print("You can't use: !#$%&'()*+,-./:;<=>?@[\]^_`{|}~  in the username")
                incorrect = True
                break

        for symbols1 in string.punctuation:
            if symbols1 in pword:
                print("You can't use: !#$%&'()*+,-./:;<=>?@[\]^_`{|}~  in the username")
                incorrect = True
                break

        if incorrect:
            None
        elif len(uname) < 5:
            print("Your username is too short")
        elif len(pword) < 7:
            print("Your password is too short")
        else:
            with open('users.json') as file:
                users = json.load(file)

            users[uname] = {'username': uname, 'password': pword,
                            'created': datetime.now().strftime("%Y-%M-%D %h-%M-%S")}

            with open("users.json", "w") as file:
                json.dump(users, file)
            self.manager.current = "Sign_Up_Screen_Success"


class SignUpScreenSuccess(Screen):
    def go_login(self):
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "left"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in
                              available_feelings]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class RootWidget(ScreenManager):
    pass


class ImageButton(ButtonBehavior, Image, HoverBehavior):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
