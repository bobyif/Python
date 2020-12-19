from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import string

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        incorrect = False
        for symbols in string.punctuation:
            if symbols in uname:
                print("You can't use: !#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
                incorrect = True
        for symbols1 in string.punctuation:
            if symbols1 in pword:
                print("You can't use: !#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
                incorrect = True
        if incorrect:
            pass
        elif len(uname) < 5:
            print("Your username is too short")
        elif len(pword) < 7:
            print("Your password is too short")
        else:
            print("This is the Username : {} and this is the password : {} of this user".format(uname, pword))


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
