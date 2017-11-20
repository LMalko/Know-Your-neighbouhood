from model_root import ModelRoot
from view_root import ViewRoot
from controller_user import ControllerUser


class ControllerRoot():

    def __init__(self):
        self.initialize_model()
        self.view = ViewRoot()

    def initialize_model(self):
        self.model = ModelRoot()

    def initialize_user_controller(self):
        self.user_controller = ControllerUser()

    def initialize_containers(self):
        self.malopolska_area_container = self.model.get_malopolska_area_container()

    def login(self):
        self.login = ViewRoot().display_login_screen()

    def menu_screen(self):
        self.menu_options = ModelRoot().get_menu_options()
        self.menu = ViewRoot().display_menu_screen(self.menu_options)

    def flow(self):
        self.initialize_model()
        self.initialize_user_controller()
        self.initialize_containers()
        self.login()
        self.menu_screen()



    
