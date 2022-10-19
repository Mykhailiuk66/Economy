import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import math

RATIO_TABLE = {
    'Organic': [2.4, 1.05, 2.5, 0.38],
    'Semidetach': [3, 1.12, 2.5, 0.35],
    'Embedded': [3.6, 1.2, 2.5, 0.32],
}

RATIO_TABLE_INTERMEDIATE = {
    'Organic': [3.2, 1.05],
    'Semidetach': [3, 1.12],
    'Embedded': [2.8, 1.2],
} 

WEIGHTTING_FACTORS = [
    [0.75, 0.88, 1, 1.15, 1.4, 0],
    [0, 0.94, 1, 1.08, 1.16, 0],
    [0.7, 0.85, 1, 1.15, 1.3, 1.65],
    
    [0, 0, 1, 1.11, 1.3, 1.66],
    [0, 0, 1, 1.06, 1.21, 1.56],
    [0, 0.87, 1, 1.15, 1.3, 0],
    [0, 0.87, 1, 1.07, 1.15, 0],
    
    [1.46, 1.19, 1, 0.86, 0.71, 0],
    [1.29, 1.13, 1, 0.91, 0.82, 0],
    [1.42, 1.17, 1, 0.86, 0,7, 0],
    [1.21, 1.1, 1, 0.9, 0, 0],
    [1.14, 1.07, 1, 0.95, 0, 0],
    
    [1.24, 1.1, 1, 0.91, 0.82, 0],
    [1.24, 1.1, 1, 0.91, 0.83, 0],
    [1.23, 1.08, 1, 1.04, 1.1, 0],
    
]

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_UI()

    def init_UI(self):
        width = 800
        height = 620

        self.setFixedSize(width, height)
        self.ui.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        input_kloc = self.ui.kloc_input.value()
        input_type = self.ui.type_input.currentText()

        a, b, c, d = RATIO_TABLE[input_type]

        pm = round(a * pow(input_kloc, b), 2)
        tm = round(c * pow(pm, d), 2)
        ss = round(pm/tm, 2)
        p = round(input_kloc/pm, 2)
        
        self.ui.pm_output.setText(str(pm))
        self.ui.tm_output.setText(str(tm))
        self.ui.ss_output.setText(str(ss))
        self.ui.p_output.setText(str(p))
        
        factors_intexes = []
        factors_intexes.append(self.ui.rely_input.value())
        factors_intexes.append(self.ui.data_input.value())
        factors_intexes.append(self.ui.cplx_input.value())
        factors_intexes.append(self.ui.time_input.value())
        factors_intexes.append(self.ui.stor_input.value())
        factors_intexes.append(self.ui.virt_input.value())
        factors_intexes.append(self.ui.turn_input.value())
        factors_intexes.append(self.ui.acap_input.value())
        factors_intexes.append(self.ui.aexp_input.value())
        factors_intexes.append(self.ui.pcap_input.value())
        factors_intexes.append(self.ui.vexp_input.value())
        factors_intexes.append(self.ui.lexp_input.value())
        factors_intexes.append(self.ui.modp_input.value())
        factors_intexes.append(self.ui.tool_input.value())
        factors_intexes.append(self.ui.sced_input.value())
        
        factors = []
        for i, j in zip(WEIGHTTING_FACTORS, factors_intexes): factors.append(i[j-1])
        
        eaf = math.prod(factors)
        
        a_intermediate, b_intermediate = RATIO_TABLE_INTERMEDIATE[input_type]
        
        pm_effort = eaf * a_intermediate * pow(input_kloc, b_intermediate)
        pm_effort = round(pm_effort, 2)
        
        self.ui.pm_output_2.setText(str(pm_effort))



app = QtWidgets.QApplication([])
application = Calculator()
application.show()


sys.exit(app.exec())
