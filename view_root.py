import os


class ViewRoot():

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_login_screen(self):
        self.clear_screen()
        _new_lines = '\n' * 4
        self.user_name = input("Enter Your name: ")
        return self.take_user_input(self.user_name)

    def take_user_input(self, user_name):
        return self.user_name

    @staticmethod
    def display_message(text):
        print('\n\n' + text + '\n\n')

    def display_menu_screen(self):
        self.menu_options = ["(1) List statistics\n",
                        "(2) Display 3 cities with longest names\n",
                        "(3) Display county's name with the largest number of communities\n",
                        "(4) Display locations, that belong to more than one category\n",
                        "(5) Advanced search\n",
                        "(0) Exit program\n"]
        return self.menu_options
