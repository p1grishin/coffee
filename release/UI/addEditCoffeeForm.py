# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 709)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 30, 274, 618))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_id = QtWidgets.QLabel(parent=self.widget)
        self.label_id.setObjectName("label_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_id)
        self.id = QtWidgets.QLineEdit(parent=self.widget)
        self.id.setObjectName("id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.id)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_2)
        self.sort = QtWidgets.QLineEdit(parent=self.widget)
        self.sort.setObjectName("sort")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sort)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_3)
        self.degree = QtWidgets.QComboBox(parent=self.widget)
        self.degree.setObjectName("degree")
        self.degree.addItem("")
        self.degree.addItem("")
        self.degree.addItem("")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.degree)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_4)
        self.ground = QtWidgets.QComboBox(parent=self.widget)
        self.ground.setObjectName("ground")
        self.ground.addItem("")
        self.ground.addItem("")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ground)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_5)
        self.description = QtWidgets.QPlainTextEdit(parent=self.widget)
        self.description.setObjectName("description")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.ItemRole.FieldRole, self.description)
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_6)
        self.price = QtWidgets.QDoubleSpinBox(parent=self.widget)
        self.price.setMaximum(9999999.99)
        self.price.setObjectName("price")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.ItemRole.FieldRole, self.price)
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_7)
        self.volume = QtWidgets.QDoubleSpinBox(parent=self.widget)
        self.volume.setMaximum(9999999999.99)
        self.volume.setObjectName("volume")
        self.formLayout.setWidget(30, QtWidgets.QFormLayout.ItemRole.FieldRole, self.volume)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.done_btn = QtWidgets.QPushButton(parent=self.widget)
        self.done_btn.setObjectName("done_btn")
        self.horizontalLayout.addWidget(self.done_btn)
        self.close_btn = QtWidgets.QPushButton(parent=self.widget)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Редактирование/добавление записей"))
        self.label_id.setText(_translate("Dialog", "id"))
        self.label_2.setText(_translate("Dialog", "Сорт"))
        self.label_3.setText(_translate("Dialog", "Степень обжарки"))
        self.degree.setItemText(0, _translate("Dialog", "Светлая"))
        self.degree.setItemText(1, _translate("Dialog", "Темная"))
        self.degree.setItemText(2, _translate("Dialog", "Высшая"))
        self.label_4.setText(_translate("Dialog", "Молотый/зерно"))
        self.ground.setItemText(0, _translate("Dialog", "0"))
        self.ground.setItemText(1, _translate("Dialog", "1"))
        self.label_5.setText(_translate("Dialog", "Описание вкуса"))
        self.label_6.setText(_translate("Dialog", "Цена"))
        self.label_7.setText(_translate("Dialog", "Объем упаковки"))
        self.done_btn.setText(_translate("Dialog", "Применить"))
        self.close_btn.setText(_translate("Dialog", "Отменить"))
