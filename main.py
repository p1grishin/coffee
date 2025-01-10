import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


class EspressoWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.db_name = 'coffee.sqlite'
        self.load_and_display_data()

        self.add_btn.clicked.connect(self.add_form)
        self.edit_btn.clicked.connect(self.edit_form)

    def get_data_from_db(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        query = "SELECT * FROM coffee"
        cur.execute(query)
        data = cur.fetchall()
        con.close()
        return data

    def insert_table_data(self, coffee_data):
        self.tableCoffee.setRowCount(0)
        for row_index, row_data in enumerate(coffee_data):
            self.tableCoffee.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.tableCoffee.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def load_and_display_data(self):
        all_coffee = self.get_data_from_db()
        self.insert_table_data(all_coffee)

    def add_form(self):
        dialog = AddEditCoffeeForm(self, mode='add')
        dialog.exec()
        self.load_and_display_data()

    def edit_form(self):
        selected_row = self.tableCoffee.currentRow()  # Получаем индекс текущей строки
        if selected_row == -1:
            print("Строка не выбрана!")
            return

        row_data = tuple(
            int(self.tableCoffee.item(selected_row, 3).text()) if col_index == 3 else
            float(self.tableCoffee.item(selected_row, col_index).text()) if col_index in [5, 6] else
            self.tableCoffee.item(selected_row, col_index).text()
            for col_index in range(self.tableCoffee.columnCount())
        )

        dialog = AddEditCoffeeForm(self, mode='edit', data=row_data)
        dialog.exec()
        self.load_and_display_data()



class AddEditCoffeeForm(QDialog):
    def __init__(self, parent=None, mode=None, data=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.mode = mode
        self.data = data

        self.close_btn.clicked.connect(self.close_dialog)
        self.done_btn.clicked.connect(self.done_button)

        if self.mode == 'add':
            self.label_id.hide()
            self.id.hide()

        elif mode == 'edit':
            self.label_id.show()
            self.id.show()
            self.id.setReadOnly(True)

            self.paste_data_form()

    def close_dialog(self):
        self.close()

    def get_form_data(self):
        sort = self.sort.text()
        degree = self.degree.currentText()
        ground = self.ground.currentText()
        description = self.description.toPlainText()
        price = self.price.value()
        volume = self.volume.value()
        return sort, degree, ground, description, price, volume

    def paste_data_form(self):
        self.id.setText(self.data[0])  # ID
        self.sort.setText(self.data[1])  # Сорт
        self.degree.setCurrentText(self.data[2])  # Уровень обжарки
        self.ground.setCurrentText(str(self.data[3]))  # Тип (молотый/зёрна)
        self.description.setPlainText(self.data[4])  # Описание
        self.price.setValue(float(self.data[5]))  # Цена
        self.volume.setValue(float(self.data[6]))  # Объём упаковки

    def done_button(self):
        if self.mode == 'add':
            data_form = self.get_form_data()
            q = """
                    INSERT INTO coffee (
                        sort_title, degree_of_roasting, ground_or_grains,
                        flavor_description, price, volume_of_packaging
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """
            self.query(q, data_form)

        if self.mode == 'edit':
            new_data = self.get_form_data()
            q = f"""
                            UPDATE coffee
                            SET
                                sort_title = ?,
                                degree_of_roasting = ?,
                                ground_or_grains = ?,
                                flavor_description = ?,
                                price = ?,
                                volume_of_packaging = ?
                            WHERE id = {int(self.data[0])}
                        """
            self.query(q, new_data)

    def query(self, q, d):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute(q, d)
        con.commit()
        con.close()
        self.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EspressoWidget()
    ex.show()
    sys.exit(app.exec())