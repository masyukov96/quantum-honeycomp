# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fermi = QtWidgets.QLineEdit(self.tab_3)
        self.fermi.setEnabled(True)
        self.fermi.setObjectName("fermi")
        self.gridLayout.addWidget(self.fermi, 1, 1, 1, 1)
        self.rashba = QtWidgets.QLineEdit(self.tab_3)
        self.rashba.setObjectName("rashba")
        self.gridLayout.addWidget(self.rashba, 5, 1, 1, 1)
        self.mAB = QtWidgets.QLineEdit(self.tab_3)
        self.mAB.setObjectName("mAB")
        self.gridLayout.addWidget(self.mAB, 9, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 8, 0, 1, 1)
        self.kanemele = QtWidgets.QLineEdit(self.tab_3)
        self.kanemele.setObjectName("kanemele")
        self.gridLayout.addWidget(self.kanemele, 6, 1, 1, 1)
        self.mAF = QtWidgets.QLineEdit(self.tab_3)
        self.mAF.setObjectName("mAF")
        self.gridLayout.addWidget(self.mAF, 10, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 7, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 11, 0, 1, 1)
        self.haldane = QtWidgets.QLineEdit(self.tab_3)
        self.haldane.setObjectName("haldane")
        self.gridLayout.addWidget(self.haldane, 7, 1, 1, 1)
        self.By = QtWidgets.QLineEdit(self.tab_3)
        self.By.setObjectName("By")
        self.gridLayout.addWidget(self.By, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.Bz = QtWidgets.QLineEdit(self.tab_3)
        self.Bz.setObjectName("Bz")
        self.gridLayout.addWidget(self.Bz, 4, 1, 1, 1)
        self.Bx = QtWidgets.QLineEdit(self.tab_3)
        self.Bx.setObjectName("Bx")
        self.gridLayout.addWidget(self.Bx, 2, 1, 1, 1)
        self.antihaldane = QtWidgets.QLineEdit(self.tab_3)
        self.antihaldane.setObjectName("antihaldane")
        self.gridLayout.addWidget(self.antihaldane, 8, 1, 1, 1)
        self.swave = QtWidgets.QLineEdit(self.tab_3)
        self.swave.setObjectName("swave")
        self.gridLayout.addWidget(self.swave, 11, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setEnabled(False)
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 0, 0, 1, 1)
        self.strain = QtWidgets.QLineEdit(self.tab_3)
        self.strain.setEnabled(False)
        self.strain.setObjectName("strain")
        self.gridLayout.addWidget(self.strain, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 2, 1)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.show_structure = QtWidgets.QPushButton(self.tab_4)
        self.show_structure.setObjectName("show_structure")
        self.gridLayout_11.addWidget(self.show_structure, 1, 0, 1, 1)
        self.show_structure_3d = QtWidgets.QPushButton(self.tab_4)
        self.show_structure_3d.setObjectName("show_structure_3d")
        self.gridLayout_11.addWidget(self.show_structure_3d, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.nsuper_struct = QtWidgets.QLineEdit(self.tab_4)
        self.nsuper_struct.setObjectName("nsuper_struct")
        self.gridLayout_3.addWidget(self.nsuper_struct, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bands_color = QtWidgets.QComboBox(self.tab_5)
        self.bands_color.setObjectName("bands_color")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.bands_color.addItem("")
        self.gridLayout_2.addWidget(self.bands_color, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.nk_bands = QtWidgets.QLineEdit(self.tab_5)
        self.nk_bands.setObjectName("nk_bands")
        self.gridLayout_2.addWidget(self.nk_bands, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 0, 1, 1)
        self.bands_colormap = QtWidgets.QComboBox(self.tab_5)
        self.bands_colormap.setObjectName("bands_colormap")
        self.gridLayout_2.addWidget(self.bands_colormap, 1, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.show_bands = QtWidgets.QPushButton(self.tab_5)
        self.show_bands.setObjectName("show_bands")
        self.gridLayout_8.addWidget(self.show_bands, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_36 = QtWidgets.QGridLayout()
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.label_50 = QtWidgets.QLabel(self.tab_6)
        self.label_50.setObjectName("label_50")
        self.gridLayout_36.addWidget(self.label_50, 0, 0, 1, 1)
        self.dos_delta = QtWidgets.QLineEdit(self.tab_6)
        self.dos_delta.setObjectName("dos_delta")
        self.gridLayout_36.addWidget(self.dos_delta, 2, 1, 1, 1)
        self.dos_ewindow = QtWidgets.QLineEdit(self.tab_6)
        self.dos_ewindow.setObjectName("dos_ewindow")
        self.gridLayout_36.addWidget(self.dos_ewindow, 1, 1, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.tab_6)
        self.label_51.setObjectName("label_51")
        self.gridLayout_36.addWidget(self.label_51, 1, 0, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.tab_6)
        self.label_48.setObjectName("label_48")
        self.gridLayout_36.addWidget(self.label_48, 2, 0, 1, 1)
        self.dos_nk = QtWidgets.QLineEdit(self.tab_6)
        self.dos_nk.setObjectName("dos_nk")
        self.gridLayout_36.addWidget(self.dos_nk, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_36, 0, 0, 1, 1)
        self.show_dos = QtWidgets.QPushButton(self.tab_6)
        self.show_dos.setObjectName("show_dos")
        self.gridLayout_5.addWidget(self.show_dos, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.kdos_ewindow = QtWidgets.QLineEdit(self.tab)
        self.kdos_ewindow.setObjectName("kdos_ewindow")
        self.gridLayout_9.addWidget(self.kdos_ewindow, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setObjectName("label_20")
        self.gridLayout_9.addWidget(self.label_20, 0, 0, 1, 1)
        self.kdos_mesh = QtWidgets.QLineEdit(self.tab)
        self.kdos_mesh.setObjectName("kdos_mesh")
        self.gridLayout_9.addWidget(self.kdos_mesh, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setObjectName("label_21")
        self.gridLayout_9.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setObjectName("label_40")
        self.gridLayout_9.addWidget(self.label_40, 2, 0, 1, 1)
        self.kdos_colormap = QtWidgets.QComboBox(self.tab)
        self.kdos_colormap.setObjectName("kdos_colormap")
        self.gridLayout_9.addWidget(self.kdos_colormap, 2, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.show_kdos = QtWidgets.QPushButton(self.tab)
        self.show_kdos.setObjectName("show_kdos")
        self.gridLayout_13.addWidget(self.show_kdos, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_8)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scf_initialization = QtWidgets.QComboBox(self.tab_12)
        self.scf_initialization.setObjectName("scf_initialization")
        self.scf_initialization.addItem("")
        self.scf_initialization.addItem("")
        self.scf_initialization.addItem("")
        self.gridLayout_10.addWidget(self.scf_initialization, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_12)
        self.label_22.setObjectName("label_22")
        self.gridLayout_10.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_12)
        self.label_23.setObjectName("label_23")
        self.gridLayout_10.addWidget(self.label_23, 1, 0, 1, 1)
        self.hubbard = QtWidgets.QLineEdit(self.tab_12)
        self.hubbard.setObjectName("hubbard")
        self.gridLayout_10.addWidget(self.hubbard, 1, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.tab_12)
        self.label_34.setObjectName("label_34")
        self.gridLayout_10.addWidget(self.label_34, 2, 0, 1, 1)
        self.filling_scf = QtWidgets.QLineEdit(self.tab_12)
        self.filling_scf.setObjectName("filling_scf")
        self.gridLayout_10.addWidget(self.filling_scf, 2, 1, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_10, 0, 0, 1, 2)
        self.do_scf = QtWidgets.QCheckBox(self.tab_12)
        self.do_scf.setObjectName("do_scf")
        self.gridLayout_18.addWidget(self.do_scf, 1, 0, 1, 1)
        self.solve_scf = QtWidgets.QPushButton(self.tab_12)
        self.solve_scf.setObjectName("solve_scf")
        self.gridLayout_18.addWidget(self.solve_scf, 1, 1, 1, 1)
        self.tabWidget_4.addTab(self.tab_12, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_32 = QtWidgets.QLabel(self.tab_11)
        self.label_32.setObjectName("label_32")
        self.gridLayout_12.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_11)
        self.label_14.setObjectName("label_14")
        self.gridLayout_12.addWidget(self.label_14, 1, 0, 1, 1)
        self.nk_scf = QtWidgets.QLineEdit(self.tab_11)
        self.nk_scf.setObjectName("nk_scf")
        self.gridLayout_12.addWidget(self.nk_scf, 1, 1, 1, 1)
        self.mix_scf = QtWidgets.QLineEdit(self.tab_11)
        self.mix_scf.setObjectName("mix_scf")
        self.gridLayout_12.addWidget(self.mix_scf, 0, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.tab_11)
        self.label_33.setObjectName("label_33")
        self.gridLayout_12.addWidget(self.label_33, 2, 0, 1, 1)
        self.smearing_scf = QtWidgets.QLineEdit(self.tab_11)
        self.smearing_scf.setObjectName("smearing_scf")
        self.gridLayout_12.addWidget(self.smearing_scf, 2, 1, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_11, "")
        self.gridLayout_15.addWidget(self.tabWidget_4, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.show_magnetism = QtWidgets.QPushButton(self.tab_13)
        self.show_magnetism.setObjectName("show_magnetism")
        self.gridLayout_16.addWidget(self.show_magnetism, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_13, "")
        self.gridLayout_6.addWidget(self.tabWidget_3, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.nsuper = QtWidgets.QLineEdit(self.tab_2)
        self.nsuper.setObjectName("nsuper")
        self.gridLayout_4.addWidget(self.nsuper, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.lattice = QtWidgets.QComboBox(self.tab_2)
        self.lattice.setObjectName("lattice")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.lattice.addItem("")
        self.gridLayout_4.addWidget(self.lattice, 0, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_6.addWidget(self.tabWidget, 1, 1, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setObjectName("label_46")
        self.gridLayout_6.addWidget(self.label_46, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.bands_color.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3D crystals"))
        self.fermi.setText(_translate("MainWindow", "0.0"))
        self.rashba.setText(_translate("MainWindow", "0.0"))
        self.mAB.setText(_translate("MainWindow", "0.0"))
        self.label_11.setText(_translate("MainWindow", "Kane-Mele"))
        self.label_4.setText(_translate("MainWindow", "Zeeman Jy"))
        self.label_3.setText(_translate("MainWindow", "Zeeman Jx"))
        self.label_5.setText(_translate("MainWindow", "Zeeman Jz"))
        self.label_25.setText(_translate("MainWindow", "Anti-Haldane"))
        self.kanemele.setText(_translate("MainWindow", "0.0"))
        self.mAF.setText(_translate("MainWindow", "0.0"))
        self.label_10.setText(_translate("MainWindow", "Rashba"))
        self.label_13.setText(_translate("MainWindow", "Antiferromagnetism"))
        self.label_12.setText(_translate("MainWindow", "Sublattice imbalance"))
        self.label_24.setText(_translate("MainWindow", "Haldane"))
        self.label_26.setText(_translate("MainWindow", "swave pairing"))
        self.haldane.setText(_translate("MainWindow", "0.0"))
        self.By.setText(_translate("MainWindow", "0.0"))
        self.label.setText(_translate("MainWindow", "Fermi energy"))
        self.Bz.setText(_translate("MainWindow", "0.0"))
        self.Bx.setText(_translate("MainWindow", "0.0"))
        self.antihaldane.setText(_translate("MainWindow", "0.0"))
        self.swave.setText(_translate("MainWindow", "0.0"))
        self.label_44.setText(_translate("MainWindow", "Strain"))
        self.strain.setText(_translate("MainWindow", "0.0"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Terms in the Hamiltonian"))
        self.show_structure.setText(_translate("MainWindow", "Show structure"))
        self.show_structure_3d.setText(_translate("MainWindow", "Show 3D structure"))
        self.label_7.setText(_translate("MainWindow", "Supercell"))
        self.nsuper_struct.setText(_translate("MainWindow", "1"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Structure"))
        self.bands_color.setItemText(0, _translate("MainWindow", "None"))
        self.bands_color.setItemText(1, _translate("MainWindow", "Sx"))
        self.bands_color.setItemText(2, _translate("MainWindow", "Sy"))
        self.bands_color.setItemText(3, _translate("MainWindow", "Sz"))
        self.bands_color.setItemText(4, _translate("MainWindow", "Valley"))
        self.bands_color.setItemText(5, _translate("MainWindow", "IPR"))
        self.label_9.setText(_translate("MainWindow", "# kpoints"))
        self.label_15.setText(_translate("MainWindow", "Operator"))
        self.nk_bands.setText(_translate("MainWindow", "100"))
        self.label_16.setText(_translate("MainWindow", "Colormap"))
        self.show_bands.setText(_translate("MainWindow", "Band structure"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Bands"))
        self.label_50.setText(_translate("MainWindow", "Number of kpoints"))
        self.dos_delta.setText(_translate("MainWindow", "0.01"))
        self.dos_ewindow.setText(_translate("MainWindow", "4.0"))
        self.label_51.setText(_translate("MainWindow", "Energy window"))
        self.label_48.setText(_translate("MainWindow", "Smearing"))
        self.dos_nk.setText(_translate("MainWindow", "1000"))
        self.show_dos.setText(_translate("MainWindow", "Density of states"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "DOS"))
        self.kdos_ewindow.setText(_translate("MainWindow", "0.5"))
        self.label_20.setText(_translate("MainWindow", "Energy window"))
        self.kdos_mesh.setText(_translate("MainWindow", "100"))
        self.label_21.setText(_translate("MainWindow", "# of points"))
        self.label_40.setText(_translate("MainWindow", "Colormap"))
        self.show_kdos.setText(_translate("MainWindow", "Show Surface DOS"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), _translate("MainWindow", "SDOS"))
        self.scf_initialization.setItemText(0, _translate("MainWindow", "antiferro"))
        self.scf_initialization.setItemText(1, _translate("MainWindow", "ferro"))
        self.scf_initialization.setItemText(2, _translate("MainWindow", "random"))
        self.label_22.setText(_translate("MainWindow", "Initialization"))
        self.label_23.setText(_translate("MainWindow", "Hubbard"))
        self.hubbard.setText(_translate("MainWindow", "2.0"))
        self.label_34.setText(_translate("MainWindow", "Filling"))
        self.filling_scf.setText(_translate("MainWindow", "0.5"))
        self.do_scf.setText(_translate("MainWindow", "Include mean field"))
        self.solve_scf.setText(_translate("MainWindow", "Solve SCF"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), _translate("MainWindow", "Basic"))
        self.label_32.setText(_translate("MainWindow", "Mixing"))
        self.label_14.setText(_translate("MainWindow", "# of kpoints"))
        self.nk_scf.setText(_translate("MainWindow", "10"))
        self.mix_scf.setText(_translate("MainWindow", "0.9"))
        self.label_33.setText(_translate("MainWindow", "Smearing"))
        self.smearing_scf.setText(_translate("MainWindow", "0.01"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("MainWindow", "Convergence"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "SCF"))
        self.show_magnetism.setText(_translate("MainWindow", "Show magnetism"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("MainWindow", "Magnetism"))
        self.nsuper.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Supercell"))
        self.label_8.setText(_translate("MainWindow", "Type of lattice"))
        self.lattice.setItemText(0, _translate("MainWindow", "Diamond"))
        self.lattice.setItemText(1, _translate("MainWindow", "Cubic"))
        self.lattice.setItemText(2, _translate("MainWindow", "Pyrochlore"))
        self.lattice.setItemText(3, _translate("MainWindow", "Hyperhoneycomb"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Geometry"))
        self.label_46.setToolTip(_translate("MainWindow", "This module allows to compute heterostructures consisting of two different films. You have to specify the parameters of the two films"))
        self.label_46.setText(_translate("MainWindow", "About"))
