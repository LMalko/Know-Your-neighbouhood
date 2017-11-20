from controller_root import ControllerRoot


class App():

    def __init__(self):

        self.root = ControllerRoot()


if __name__ == "__main__":
    initiate_program = App()
    initiate_program.root.flow()