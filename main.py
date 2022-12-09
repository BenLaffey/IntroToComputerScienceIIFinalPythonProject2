#Requires the PyQt5 Package to be installed in order to run
#Project 2: Battleship Game

#Feedback Implemented: Customized Game Fonts, Improved Background, Added Rules
from controller import *


def main() -> None:
    """
    Function to act as the main graphical window creator and updater.
    :return: None
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()