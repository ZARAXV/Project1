from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    cookie_count = 0
    cookie_money = 0
    sandwich_count = 0
    sandwich_money = 0
    water_count = 0
    water_money = 0

    def __init__(self, *args, **kwargs) -> None:
        """
        Function will set up the interface
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.buttonOption.clicked.connect(lambda: self.submit())
        self.radio_cookie.clicked.connect(lambda: self.item())
        self.radio_sandwich.clicked.connect(lambda: self.item())
        self.radio_water.clicked.connect(lambda: self.item())
        self.radio_exit.clicked.connect(lambda: self.exit())
        self.radio_cookie.hide()
        self.radio_sandwich.hide()
        self.radio_water.hide()
        self.radio_exit.hide()

    def submit(self) -> None:
        """
        Function will work only once submit is clicked
        Will ask the user for the option
        :return: interface change based on user selection
        """
        option = self.inputOption.text().lower()

        try:
            if option == 's':
                self.labelTitle.clear()
                self.labelOption1.clear()
                self.labelOption2.clear()
                self.inputOption.clear()
                self.labelOutput.clear()

                self.labelTitle.setText(f'----CART MENU----')
                self.radio_cookie.show()
                self.radio_sandwich.show()
                self.radio_water.show()
                self.radio_exit.show()

                self.buttonOption.hide()
                self.inputOption.hide()
                self.labelInput.clear()

            elif option == 'x':
                self.inputOption.clear()
                self.labelOutput.setText(f'------------------------------\n'
                                         f'(0) - Cookie = ${Controller.cookie_money:.2f}\n'
                                         f'(0) - Sandwich = ${Controller.sandwich_money:.2f}\n'
                                         f'(0) - Water = ${Controller.water_money:.2f}\n'
                                         f'---------------------------------\n'
                                         f'GRAND TOTAL = $0.00\n'
                                         f'---------------------------------'
                                         )

            else:
                raise ValueError
        except ValueError:
            self.inputOption.clear()
            self.labelOutput.setText(f'Invalid must be either s/x')

    def item(self) -> None:
        """
        Function will add item based on what user has chosen and will print that on a label
        :return: Phrase showing what has been added
        """

        if self.radio_cookie.isChecked():

            Controller.cookie_count += 1
            Controller.cookie_money += 1.50
            self.labelOutput.setText(f'Added Cookie {Controller.cookie_count}')

        elif self.radio_sandwich.isChecked():
            Controller.sandwich_count += 1
            Controller.sandwich_money += 4.00
            self.labelOutput.setText(f'Added Sandwich {Controller.sandwich_count}')

        else:

            Controller.water_count += 1
            Controller.water_money += 1.00
            self.labelOutput.setText(f'Added Water {Controller.water_count}')

    def exit(self) -> None:
        """
        Function will show the total amount on the GUI
        :return: total amount on interface
        """
        total = Controller.cookie_money + Controller.sandwich_money + Controller.water_money
        self.labelOutput.setText(f'------------------------------\n'
                                 f'({Controller.cookie_count}) - Cookie = ${Controller.cookie_money:.2f}\n'
                                 f'({Controller.sandwich_count}) - Sandwich = ${Controller.sandwich_money:.2f}\n'
                                 f'({Controller.water_count}) - Water = ${Controller.water_money:.2f}\n'
                                 f'---------------------------------\n'
                                 f'GRAND TOTAL = ${total:.2f}\n'
                                 f'---------------------------------'
                                 )
