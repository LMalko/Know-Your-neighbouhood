from model_root import ModelRoot
from view_root import ViewRoot
from controller_user import ControllerUser


class ControllerRoot():

    def __init__(self):
        self.initialize_model()
        self.view = view_root.ViewRoot()

    def initialize_model(self):
        self.model = model_root.ModelRoot()

    def initialize_user_controller(self):
        self.user_controller = ControllerUser()

    def initialize_containers(self):
        self.malopolska_area_container = model_root.import_malopolska_area_data()

    def login(self):
        self.login = view_root.display_login_screen

    def menu_screen(self):
        self.menu = view_root.display_menu_screen()



    
