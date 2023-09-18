import Calc_Cientifica , Calc_Convencional, Botoes
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QStackedWidget
from math import *

class Control:
    def __init__(self):
        #Botoes
        self.Dialog = QtWidgets.QDialog()
        self.ui = Botoes.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        

        self.ui.Cientifica.clicked.connect(self.abre_cientifica)
        self.ui.Convencional.clicked.connect(self.abre_convencional)
        
        #Convencional
        self.Dialog2 = QtWidgets.QDialog()
        self.ui2 = Calc_Convencional.Ui_Dialog()
        self.ui2.setupUi(self.Dialog2)
        self.ui2.DISPLAY.setText("")

        self.ui2.MENU.clicked.connect(self.volta_menu)
        self.ui2.AC.clicked.connect(self.escreve)
        self.ui2.DEL.clicked.connect(self.escreve)
        self.ui2.VEZES.clicked.connect(self.escreve)
        self.ui2.DIVISAO.clicked.connect(self.escreve)
        self.ui2.MAIS.clicked.connect(self.escreve)
        self.ui2.MENOS.clicked.connect(self.escreve)
        self.ui2.PONTO.clicked.connect(self.escreve)
        self.ui2.IGUAL.clicked.connect(self.escreve)
        self.ui2.RAIZ.clicked.connect(self.escreve)
        self.ui2.ZERO.clicked.connect(self.escreve)
        self.ui2.UM.clicked.connect(self.escreve)
        self.ui2.DOIS.clicked.connect(self.escreve)
        self.ui2.TRES.clicked.connect(self.escreve)
        self.ui2.QUATRO.clicked.connect(self.escreve)
        self.ui2.CINCO.clicked.connect(self.escreve)
        self.ui2.SEIS.clicked.connect(self.escreve)
        self.ui2.SETE.clicked.connect(self.escreve)
        self.ui2.OITO.clicked.connect(self.escreve)
        self.ui2.NOVE.clicked.connect(self.escreve)

        self.ui2.MENU.clicked.connect(self.volta_menu)
        #Cientifica
        self.Dialog3 = QtWidgets.QDialog()
        self.ui3 = Calc_Cientifica.Ui_Dialog()
        self.ui3.setupUi(self.Dialog3)
        self.ui3.DISPLAY.setText("")

        self.ui3.MENU.clicked.connect(self.volta_menu)
        self.ui3.AC.clicked.connect(self.escreve)
        self.ui3.DEL.clicked.connect(self.escreve)
        self.ui3.TANGENTE.clicked.connect(self.escreve)
        self.ui3.COS.clicked.connect(self.escreve)
        self.ui3.SENO.clicked.connect(self.escreve)
        self.ui3.VEZES.clicked.connect(self.escreve)
        self.ui3.DIVISAO.clicked.connect(self.escreve)
        self.ui3.MAIS.clicked.connect(self.escreve)
        self.ui3.MENOS.clicked.connect(self.escreve)
        self.ui3.PONTO.clicked.connect(self.escreve)
        self.ui3.IGUAL.clicked.connect(self.escreve)
        self.ui3.RAIZ.clicked.connect(self.escreve)
        self.ui3.EXPONENCIAL.clicked.connect(self.escreve)
        self.ui3.PORCENTAGEM.clicked.connect(self.escreve)
        self.ui3.ZERO.clicked.connect(self.escreve)
        self.ui3.UM.clicked.connect(self.escreve)
        self.ui3.DOIS.clicked.connect(self.escreve)
        self.ui3.TRES.clicked.connect(self.escreve)
        self.ui3.QUATRO.clicked.connect(self.escreve)
        self.ui3.CINCO.clicked.connect(self.escreve)
        self.ui3.SEIS.clicked.connect(self.escreve)
        self.ui3.SETE.clicked.connect(self.escreve)
        self.ui3.OITO.clicked.connect(self.escreve)
        self.ui3.NOVE.clicked.connect(self.escreve)
        
    
        #declarar todos botoes com funcao self escreve

    def abre_cientifica(self):
        self.Dialog.close()
        self.Dialog3.show()

    def abre_convencional(self):
        self.Dialog.close()
        self.Dialog2.show()

    def volta_menu(self):
        self.Dialog2.close()
        self.Dialog3.close()
        self.Dialog.show()

    def escreve(self):


        #colocar funcao isvisible
        if self.Dialog3.isVisible():
            sender = self.Dialog3.sender()
            if(sender.text() == "cos"):
                anterior = str(self.ui3.DISPLAY.text())
                resultado = eval(f'cos(({anterior}*pi)/180)')
                try:
                    print(self.ui3.DISPLAY.setText(str(round(resultado,5))))
                except:
                    print(self.ui3.DISPLAY.setText("Error"))

            
            elif(sender.text() == "sin"):
                anterior = str(self.ui3.DISPLAY.text())
                resultado = eval(f'sin(({anterior}*pi)/180)')
                try:
                    print(self.ui3.DISPLAY.setText(str(round(resultado,5))))
                except:
                    print(self.ui3.DISPLAY.setText("Error"))

            elif(sender.text() == "tan"):
                anterior = str(self.ui3.DISPLAY.text())
                resultado = eval(f'tan(({anterior}*pi)/180)')
                try:
                    print(self.ui3.DISPLAY.setText(str(round(resultado,5))))
                except:
                    print(self.ui3.DISPLAY.setText("Error"))

            elif(sender.text() == "√"):
                anterior = str(self.ui3.DISPLAY.text())
                resultado = eval(f'sqrt({anterior})')
                try:
                    print(self.ui3.DISPLAY.setText(str(round(resultado,5))))
                except:
                    print(self.ui3.DISPLAY.setText("Error"))

            elif(sender.text() == "%"):
                anterior = str(self.ui3.DISPLAY.text())
                resultado = eval(f'{anterior}/100')
                try:
                    print(self.ui3.DISPLAY.setText(str(round(resultado,5))))
                except:
                    print(self.ui3.DISPLAY.setText("Error"))

            elif(sender.text() == "exp"):
                anterior = str(self.ui3.DISPLAY.text())
                print(self.ui3.DISPLAY.setText(anterior + str("**")))

            elif(sender.text() == "AC"):
                print(self.ui3.DISPLAY.setText(""))

            elif(sender.text() == "DEL"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()[:-1]))

            elif(sender.text() == "+"):
                anterior = str(self.ui3.DISPLAY.text())
                if "+" in anterior:
                    print(self.ui3.DISPLAY.setText("Error"))
                else:
                    print(self.ui3.DISPLAY.setText(str(anterior) + "+"))

            elif(sender.text() == "-"):
                anterior = str(self.ui3.DISPLAY.text())
                if "-" in anterior:
                    print(self.ui3.DISPLAY.setText("Error"))
                else:
                    print(self.ui3.DISPLAY.setText(str(anterior) + "-"))

            elif(sender.text() == "X"):
                anterior = str(self.ui3.DISPLAY.text())
                if "*" in anterior:
                    print(self.ui3.DISPLAY.setText("Error"))
                else:
                    print(self.ui3.DISPLAY.setText(str(anterior) + "*"))

            elif(sender.text() == "÷"):
                anterior = str(self.ui3.DISPLAY.text())
                if "/" in anterior:
                    print(self.ui3.DISPLAY.setText("Error"))
                else:
                    print(self.ui3.DISPLAY.setText(str(anterior) + "/"))

            elif(sender.text() == "="):
                equacao = str(self.ui3.DISPLAY.text())
                resultado = eval(f'{equacao}')
                try:
                    print(self.ui3.DISPLAY.setText(str(round(resultado,5))))
                except:
                    print(self.ui3.DISPLAY.setText("Error"))

            elif(sender.text() == "."):
                anterior = str(self.ui3.DISPLAY.text())
                if "." in anterior:
                    print(self.ui3.DISPLAY.setText("Error"))
                else:
                    print(self.ui3.DISPLAY.setText(str(anterior) + "."))

            elif (sender.text() == "0"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "1"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "2"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "3"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "4"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "5"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "6"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "7"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "8"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "9"):
                print(self.ui3.DISPLAY.setText(self.ui3.DISPLAY.text()+ sender.text()))
        
        elif self.Dialog2.isVisible():
            sender = self.Dialog2.sender()
            if(sender.text() == "+"):
                anterior = str(self.ui2.DISPLAY.text())
                if "+" in anterior:
                    print(self.ui2.DISPLAY.setText("Error"))
                else:
                    print(self.ui2.DISPLAY.setText(str(anterior) + "+"))

            elif(sender.text() == "-"):
                anterior = str(self.ui2.DISPLAY.text())
                if "-" in anterior:
                    print(self.ui2.DISPLAY.setText("Error"))
                else:
                    print(self.ui2.DISPLAY.setText(str(anterior) + "-"))

            elif(sender.text() == " ÷"):
                anterior = str(self.ui2.DISPLAY.text())
                if "/" in anterior:
                    print(self.ui2.DISPLAY.setText("Error"))
                else:
                    print(self.ui2.DISPLAY.setText(str(anterior) + "/"))

            elif(sender.text() == "X"):
                anterior = str(self.ui2.DISPLAY.text())
                if "*" in anterior:
                    print(self.ui2.DISPLAY.setText("Error"))
                else:
                    print(self.ui2.DISPLAY.setText(str(anterior) + "*"))

            elif(sender.text() == "="):
                equacao = str(self.ui2.DISPLAY.text())
                resultado = eval(f'{equacao}')
                try:
                    print(self.ui2.DISPLAY.setText(str(round(resultado,5))))
                except:
                    print(self.ui2.DISPLAY.setText("Error"))

            elif(sender.text() == "."):
                anterior = str(self.ui2.DISPLAY.text())
                if "." in anterior:
                    print(self.ui2.DISPLAY.setText("Error"))
                else:
                    print(self.ui2.DISPLAY.setText(str(anterior) + "."))

            elif (sender.text() == "0"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "1"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "2"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "3"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "4"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "5"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "6"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "7"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "8"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif (sender.text() == "9"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()+ sender.text()))

            elif(sender.text() == "AC"):
                print(self.ui2.DISPLAY.setText(""))

            elif(sender.text() == "DEL"):
                print(self.ui2.DISPLAY.setText(self.ui2.DISPLAY.text()[:-1]))

            elif(sender.text() == "√"):
                anterior = str(self.ui2.DISPLAY.text())
                resultado = eval(f'sqrt({anterior})')
                try:
                    print(self.ui2.DISPLAY.setText(str(round(resultado,5))))
                except:
                    print(self.ui2.DISPLAY.setText("Error"))

                    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = Control()
    c.Dialog.show()
    sys.exit(app.exec_())