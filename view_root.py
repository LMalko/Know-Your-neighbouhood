import os


class ViewRoot():

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_login_screen(self):
        self.clear_screen()
        self.user_name = input("Enter Your name: ")
        return self.take_user_input(self.user_name)

    def take_user_input(self, user_name):
        return self.user_name

    @staticmethod
    def display_message(text):
        print('\n' + text + '\n')

    @staticmethod
    def set_input(question):
        return input('\n' + str(question) + '\n')

    def display_menu_screen(self, menu_options):
        self.menu_options = menu_options
        self.clear_screen()
        for i in self.menu_options:
            print(i)
