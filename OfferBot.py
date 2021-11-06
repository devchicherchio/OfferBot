import pyautogui
import time
from PyQt5 import uic, QtWidgets
import threading



def chama_segunda_tela():
    primeira_tela.close()
    segunda_tela.show()

def testarclick():
    def testarclick1():
        segunda_tela.label_16.setText("5")
        time.sleep(1)
        segunda_tela.label_16.setText("4")
        time.sleep(1)
        segunda_tela.label_16.setText("3")
        time.sleep(1)
        segunda_tela.label_16.setText("2")
        time.sleep(1)
        segunda_tela.label_16.setText("1")
        time.sleep(1)
        posição = pyautogui.position()
        posição1 = str(posição)
        segunda_tela.label_16.setText(posição1)

    tarefa = threading.Thread(target=testarclick1)
    tarefa.daemon = True
    tarefa.start()




def automatizar():
    def automatizar1():

        n = 0
        valor = segunda_tela.spinBox.value()
        nu = float(valor)
        x1 = segunda_tela.lineEdit.text()
        x11 = float(x1)
        x2 = segunda_tela.lineEdit_2.text()
        x22 = float(x2)
        x3 = segunda_tela.lineEdit_3.text()
        x33 = float(x3)
        x4 = segunda_tela.lineEdit_4.text()
        x44 = float(x4)

        y1 = segunda_tela.lineEdit_8.text()
        y11 = float(y1)
        y2 = segunda_tela.lineEdit_6.text()
        y22 = float(y2)
        y3 = segunda_tela.lineEdit_7.text()
        y33 = float(y3)
        y4 = segunda_tela.lineEdit_5.text()
        y44 = float(y4)



        while n < nu:
            time.sleep(1)
            pyautogui.click(x=x11, y=y11)
            time.sleep(1)
            pyautogui.click(x=x22, y=y22)
            time.sleep(1)
            pyautogui.click(x=x33, y=y33)
            time.sleep(1)
            pyautogui.click(x=x44, y=y44)
            time.sleep(1)
            pyautogui.hotkey('Ctrl', 'w')
            n = n + 1
            ns = str(n)
            if n == 1:
               segunda_tela.label_17.setText((ns)+" post denunciado com sucesso. Bom trabalho!")
            else:
                segunda_tela.label_17.setText((ns) + " posts denunciado com sucesso. Bom trabalho!")

    tarefa = threading.Thread(target=automatizar1)
    tarefa.daemon = True
    tarefa.start()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton_2.clicked.connect(automatizar)
segunda_tela.pushButton.clicked.connect(testarclick)
x1 = segunda_tela.lineEdit.text()
x2 = segunda_tela.lineEdit_2.text()
x3 = segunda_tela.lineEdit_3.text()
x4 = segunda_tela.lineEdit_4.text()
y1 = segunda_tela.lineEdit_8.text()
y2 = segunda_tela.lineEdit_6.text()
y3 = segunda_tela.lineEdit_7.text()
y4 = segunda_tela.lineEdit_5.text()

primeira_tela.show()
app.exec()
