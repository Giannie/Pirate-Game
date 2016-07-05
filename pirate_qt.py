import sys
import datetime
import threading
import os
import configparser
import pirate_generator

from PyQt5 import QtGui, QtCore, QtWidgets
#import qt5_layout as qt_layout

# from PyQt4 import QtGui, QtCore
# from PyQt4 import QtGui as QtWidgets
import qt_test as qt_layout

tablestyle = "QTableWidget::item{ selection-background-color: #6699ff}"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)



class PirateApp(QtWidgets.QMainWindow, qt_layout.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PirateApp, self).__init__(parent)
        self.setupUi(self)
        self.pigen = pirate_generator.pirateGenerator()
        for i in range(self.tableWidget.horizontalHeader().count()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        for i in range(self.tableWidget.verticalHeader().count()):
            self.tableWidget.verticalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.next_button.clicked.connect(self.next)
        self.quit_button.clicked.connect(self.close)
        self.tableWidget.setStyleSheet(tablestyle)
        self.cell_edit.returnPressed.connect(self.next)

    def next(self):
        selection = self.cell_edit.text()
        self.cell_edit.clear()
        if selection.upper() in self.pigen:
            cell = selection
        elif len(selection) == 0:
            cell = None
        else:
            self.cell_label.setText("X")
            return
        ref = self.pigen.next_item(ref=cell)
        cellRef = self.pigen.cellRef(ref)
        index = self.tableWidget.model().index(cellRef[0], cellRef[1])
        self.tableWidget.selectionModel().select(index, QtCore.QItemSelectionModel.Select)
        self.cell_label.setText(ref)
        if len(self.pigen) == 0:
            self.next_button.hide()
            self.cell_edit.hide()
            self.label.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(style)
    form = PirateApp()
    form.show()
    app.exec_()
