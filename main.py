import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class EspressoWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.db_name = 'coffee.sqlite'
        all_coffee = self.get_data_from_db()
        self.insert_table_data(all_coffee)

    def get_data_from_db(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        query = "SELECT * FROM coffee"
        cur.execute(query)
        return cur.fetchall()

    def insert_table_data(self, coffee_data):
        self.tableCoffee.setRowCount(0)
        for row_index, row_data in enumerate(coffee_data):
            self.tableCoffee.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.tableCoffee.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EspressoWidget()
    ex.show()
    sys.exit(app.exec())