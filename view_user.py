import os


class ViewUser():

    def get_user_input(self, text):
        return input(text)

    def display_collection(self, collection):
        for item in collection:
            print(item)

    def display_message(self, text):
        print(text)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
