from PyQt5.QtWidgets import *
from view import *
import random


class Controller(QMainWindow, Ui_MainWindow):
    """
    A QMainWindow and Ui_MainWindow class representing the main logic controller for a 'Controller' object.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Function to initialize the 'Controller' object by setting up the user interface, setting every label except the 'rules' label's background colors to cyan, setting the 'rules' label's and 'fire' push button's background colors to tan, creating a '__boardtop' string and '__spaces', '__rows', '__playerboard', and '__computerboard' lists, displaying both boards with the 'displayPlayerBoard()' and 'displayComputerBoard()' functions, and setting the push button to the 'fire()' function respectively.
        :param args: A tuple used to pass a variable number of non-key worded arguments to this function.
        :param kwargs: A dictionary used to pass a keyworded variable-length argument list to this function.
        :return: None
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.label_title.setStyleSheet("background-color:cyan")
        self.label_key.setStyleSheet("background-color:cyan")
        self.label_player.setStyleSheet("background-color:cyan")
        self.label_computer.setStyleSheet("background-color:cyan")
        self.label_playerboard.setStyleSheet("background-color:cyan")
        self.label_computerboard.setStyleSheet("background-color:cyan")
        self.label_prompt.setStyleSheet("background-color:cyan")
        self.label_rules.setStyleSheet("background-color:tan")
        self.pushButton_fire.setStyleSheet("background-color:tan")
        self.__boardtop: str = "   1  2  3  4  5  6  7  8  9 10\n"
        self.__spaces: list = ["░░", "**", "~~", "██", "??"]
        self.__rows: list = ["A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J "]
        self.__playerboard: list = [[2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
                                    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                                    [0, 2, 2, 2, 2, 2, 0, 2, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__computerboard: list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 2, 0, 2, 2, 2, 0],
                                      [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                                      [0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
                                      [0, 2, 0, 0, 0, 0, 2, 0, 0, 0],
                                      [0, 2, 0, 0, 0, 0, 2, 0, 0, 0],
                                      [0, 2, 0, 0, 0, 0, 2, 0, 0, 0],
                                      [0, 2, 0, 0, 0, 0, 0, 2, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 2, 0, 0]]
        self.displayPlayerBoard()
        self.displayComputerBoard()
        self.pushButton_fire.clicked.connect(lambda: self.fire())

    def fire(self) -> None:
        """
        Function to interpret the validity of the coordinate that was entered by the user and set the equivalent location on the computer's board to a 'hit' or 'miss' status.
        :return: None
        """
        if len(self.lineEdit_input.text().strip().lower()) > 1:
            letter: str = list(self.lineEdit_input.text().strip().lower())[0]
            if "abcdefghij".rfind(letter) > -1:
                text: list = list(self.lineEdit_input.text().strip().lower())
                text.pop(0)
                try:
                    if 0 < int(''.join(text)) < 11:
                        if self.__computerboard["abcdefghij".rfind(letter)][int(''.join(text)) - 1] % 2 == 0:
                            self.label_prompt.setText("Enter Coordinates Here (Ex: \"a1\")")
                            self.lineEdit_input.setText("")
                            self.__computerboard["abcdefghij".rfind(letter)][int(''.join(text)) - 1]: list = self.__computerboard["abcdefghij".rfind(letter)][int(''.join(text)) - 1] + 1
                            self.displayComputerBoard()
                            self.moveComputer()
                        else:
                            self.label_prompt.setText("      Please Enter Coordinates\n          Free Of Destruction\n(Ex: \"(free letter)(free number)\")")
                    else:
                        self.label_prompt.setText("  Please Enter Coordinates With\n   Numbers In Range (Ex: \"a1\")")
                except ValueError:
                    self.label_prompt.setText("   Please Enter Coordinates With\n     Valid Numbers (Ex: \"a1\")")
            else:
                self.label_prompt.setText("  Please Enter Coordinates With\n     Letters In Range (Ex: \"a1\")")
        else:
            self.label_prompt.setText("   Please Enter Valid Coordinates\n              Here (Ex: \"a1\")")

    def displayPlayerBoard(self) -> None:
        """
        Function to display the current status of the player's board and determine if the player has lost the game.
        :return: None
        """
        lost: bool = True
        output: str = ""
        for i in range(10):
            output: str = output + self.__rows[i]
            for j in range(10):
                output: str = f"{output}{self.__spaces[self.__playerboard[i][j]]} "
                for k in range(int(self.__playerboard[i][j] == 2)):
                    lost: bool = False
            for e in range(int(i < 9)):
                output: str = output + "\n"
        self.label_playerboard.setText(self.__boardtop + output)
        if lost:
            self.lineEdit_input.hide()
            self.pushButton_fire.hide()
            self.label_prompt.setText("                    Computer Wins")

    def displayComputerBoard(self) -> None:
        """
        Function to display the current status of the computer's board.
        :return: None
        """
        output: str = ""
        for i in range(10):
            output: str = output + self.__rows[i]
            for j in range(10):
                output: str = f"{output}{self.__spaces[(self.__computerboard[i][j] * (self.__computerboard[i][j] % 2)) + int((self.__computerboard[i][j] % 2) == 0) * 4]} "
            for e in range(int(i < 9)):
                output: str = output + "\n"
        self.label_computerboard.setText(self.__boardtop + output)

    def moveComputer(self) -> None:
        """
        Function to make the computer player act on the player's board and set the determined coordinate to a 'hit' or 'miss' status if the computer has validated that it has not lost the game.
        :return: None
        """
        lost: bool = True
        for i in range(len(self.__computerboard)):
            for j in range(len(self.__computerboard[i])):
                for k in range(int(self.__computerboard[i][j] == 2)):
                    lost: bool = False
        if not lost:
            y: int = random.randint(0, 9)
            x: int = random.randint(0, 9)
            while self.__playerboard[y][x] % 2 == 1:
                y: int = random.randint(0, 9)
                x: int = random.randint(0, 9)
            self.__playerboard[y][x]: list = self.__playerboard[y][x] + 1
            self.displayPlayerBoard()
        else:
            self.lineEdit_input.hide()
            self.pushButton_fire.hide()
            self.label_prompt.setText("                    Player Wins")
