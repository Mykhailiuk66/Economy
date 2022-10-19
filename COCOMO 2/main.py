import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import math

preliminary_factors = {
        'PREC': [6.20, 4.96, 3.72, 2.48, 1.24, 0.00],
        'FLEX': [5.07, 4.05, 3.04, 2.03, 1.01, 0.00],
        'RESL': [7.07, 5.56, 4.24, 2.83, 1.41, 0.00],
        'TEAM': [5.48, 4.38, 3.29, 2.19, 1.10, 0.00],
        'PMAT': [7.80, 6.24, 4.86, 3.12, 1.56, 0.00],

        'PERS': [2.12, 1.62, 1.26, 1.00, 0.83, 0.63, 0.50],
        'PREX': [1.59, 1.33, 1.22, 1.00, 0.87, 0.74, 0.62],
        'RCPX': [0.49, 0.60, 0.83, 1.00, 1.33, 1.91, 2.72],
        'RUSE': [0, 0, 0.95, 1.00, 1.07, 1.15, 1.24],
        'PDIF': [0, 0, 0.87, 1.00, 1.29, 1.81, 2.61],
        'FCIL': [1.43, 1.30, 1.10, 1.00, 0.87, 0.73, 0.62],
        'SCED': [0, 1.43, 1.14, 1.00, 1.00, 0, 0],
}



detailed_factors = {
        'PREC': [6.20, 4.96, 3.72, 2.48, 1.24, 0.00],
        'FLEX': [5.07, 4.05, 3.04, 2.03, 1.01, 0.00],
        'RESL': [7.07, 5.56, 4.24, 2.83, 1.41, 0.00],
        'TEAM': [5.48, 4.38, 3.29, 2.19, 1.10, 0.00],
        'PMAT': [7.80, 6.24, 4.86, 3.12, 1.56, 0.00],

        'ACAP': [1.42, 1.29, 1.00, 0.85, 0.71, 0],
        'AEXP': [1.22, 1.10, 1.00, 0.88, 0.81, 0],
        'PCAP': [1.34, 1.15, 1.00, 0.88, 0.76, 0],
        'PCON': [1.29, 1.12, 1.00, 0.90, 0.81, 0],
        'PEXP': [1.19, 1.09, 1.00, 0.91, 0.85, 0],
        'LTEX': [1.20, 1.09, 1.00, 0.91, 0.84, 0],
        'RELY': [0.84, 0.92, 1.00, 1.10, 1.26, 0],
        'DATA': [0, 0.23, 1.00, 1.14, 1.28, 0],
        'CPLX': [0.73, 0.87, 1.00, 1.17, 1.34, 1.74],
        'RUSE': [0, 0.95, 1.00, 1.07, 1.15, 1.24],
        'DOCU': [0.81, 0.91, 1.00, 1.11, 1.23, 0],
        'TIME': [0, 0, 1.00, 1.11, 1.29, 1.63],
        'STOR': [0, 0, 1.00, 1.05, 1.17, 1.46],
        'PVOL': [0, 0.87, 1.00, 1.15, 1.30, 0],
        'TOOL': [1.17, 1.09, 1.00, 0.90, 0.78, 0],
        'SITE': [1.22, 1.09, 1.00, 0.93, 0.86, 0.80],
        'SCED': [1.43, 1.14, 1.00, 1.00, 1.00, 0],
    }


def start_app():
    app = QtWidgets.QApplication([])
    application = Calculator()
    application.show()


    sys.exit(app.exec())




class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.preliminary = 1

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_UI()

    def init_UI(self):
        width = 800
        height = 560
        self.setFixedSize(width, height)
        
        ly = QtWidgets.QVBoxLayout()
        self.ui.preliminaryFrame.setLayout(ly)
        ly2 = QtWidgets.QVBoxLayout()
        self.ui.detailedFrame.setLayout(ly)

        self.ui.detailedFrame.hide()
    
        self.ui.type_input.currentTextChanged.connect(self.on_combobox_changed)

        self.ui.pushButton.clicked.connect(self.calculate)
        
    
    def on_combobox_changed(self, value):
        if self.preliminary:
            self.preliminary = 0
            
            self.ui.preliminaryFrame.hide()
            self.ui.detailedFrame.show()
        else: 
            self.preliminary = 1
            
            self.ui.detailedFrame.hide()
            self.ui.preliminaryFrame.show()

    
    def get_preliminary_spinboxes(self):
        preliminary_spinboxes = [
            self.ui.p_prec,
            self.ui.p_flex,
            self.ui.p_resl,
            self.ui.p_team,
            self.ui.p_pmat,
            self.ui.p_pers,
            self.ui.p_prex,
            self.ui.p_rcpx,
            self.ui.p_ruse,
            self.ui.p_pdif,
            self.ui.p_fcil,
            self.ui.p_sced,         
        ]
        
        
        return preliminary_spinboxes


    def get_detailed_spinboxes(self):
        detailed_spinboxes = [
            self.ui.d_prec,
            self.ui.d_flex,
            self.ui.d_resl,
            self.ui.d_team,
            self.ui.d_pmat,
            self.ui.d_acap,
            self.ui.d_aexp,
            self.ui.d_pcap,
            self.ui.d_pcon,
            self.ui.d_pexp,         
            self.ui.d_ltex,
            self.ui.d_rely,
            self.ui.d_data,
            self.ui.d_cplx,
            self.ui.d_ruse,
            self.ui.d_docu,
            self.ui.d_time,
            self.ui.d_stor,
            self.ui.d_pvol,
            self.ui.d_tool,
            self.ui.d_site,
            self.ui.d_sced
        ]
        
        return detailed_spinboxes

    
    def calculate_preliminary(self, kloc, factors):
        count_iter_list_data = 0
        SF = 0
        EAF = 1
        for a in factors:
            if count_iter_list_data <= 4:
                if type(a) != str:
                    SF += a
            else:
                if type(a) != str:
                    EAF = EAF * a
            count_iter_list_data += 1
        E = 0.91 + 0.01 * SF
        PM = EAF * 2.94 * int(kloc)**E
        
        return PM
    
    
    def calculate_detailed(self, kloc, factors):
        count_iter_list_data = 0
        SF = 0
        EAF = 1
        for a in factors:
            if count_iter_list_data <= 4:
                if type(a) != str:
                    SF += a
            else:
                if type(a) != str:
                    EAF = EAF * a
            count_iter_list_data += 1
        E = 0.91 + 0.01 * SF
        PM = EAF * 2.45 * (int(kloc)**E)
        
        return PM
    

    def calculate(self):
        
        input_kloc = self.ui.kloc_input.value()
        input_type = self.ui.type_input.currentText()

        if input_type == "Preliminary":
            factors = preliminary_factors
            spinboxes = self.get_preliminary_spinboxes()
        else:
            factors = detailed_factors
            spinboxes = self.get_detailed_spinboxes()
        
        
        list_data_indexes = []
        for spinbox in spinboxes:
            list_data_indexes.append(spinbox.value()-1)
        
        
        chosen_factors = [factor[i] for i, factor in zip(list_data_indexes, factors.values())]
    
        
        if input_type == "Preliminary":
            PM = self.calculate_preliminary(input_kloc, chosen_factors)
        else:
            PM = self.calculate_detailed(input_kloc, chosen_factors)
        
        
        PM = round(PM, 2)
        
        self.ui.result.setText(str(PM))
        


if __name__ == "__main__":
    start_app()
