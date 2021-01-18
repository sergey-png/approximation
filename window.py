import sys
import math
import pylab
from matplotlib import mlab
#Импортируем наш интерфейс из файла
from base import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Здесь прописываем событие нажатия на кнопку
        self.ui.earse.clicked.connect(self.earse_b)
        self.ui.start.clicked.connect(self.start_b)
        self.ui.check1.clicked.connect(self.check1)
        self.ui.check2.clicked.connect(self.check2)
        self.ui.check3.clicked.connect(self.check3)
        self.ui.check4.clicked.connect(self.check4)
        self.ui.drow_graph.clicked.connect(self.drow_graph)
        self.ui.print_y.clicked.connect(self.print_y)
    #Функции которые выполняются при нажатии на кнопки
    def earse_b(self):
        global pn,n,xmin,xmax,dx,delta
        self.ui.check1.setEnabled(False)
        self.ui.check2.setEnabled(False)
        self.ui.check3.setEnabled(False)
        self.ui.check4.setEnabled(False)
        self.ui.print_y.setEnabled(False)
        self.ui.earse.setEnabled(False)
        self.ui.start.setEnabled(True)
        self.ui.drow_graph.setEnabled(False)
        self.ui.progressBar.setValue(0)
        n=int()
        delta=float()
        pn=[]
        xmin=float()
        dx=float()
        xmax=float()
        xlist=[]
        ylist=[]
        self.ui.check1.setText('Check')
        self.ui.check2.setText('Check')
        self.ui.check3.setText('Check')
        self.ui.check4.setText('Check')
        
    def start_b(self):
        self.ui.textBrowser.setText('Старт программы!\n\nЗдесь будет выводиться полезная информация об ошибках и примечания к заполнению форм')
        self.ui.textBrowser_2.setText('F(x) = ')
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_4.setText('')
        self.ui.lineEdit_5.setText('')
        self.ui.textEdit.setText('')
        self.ui.check1.setEnabled(True)
        self.ui.start.setEnabled(False)
        self.ui.earse.setEnabled(True)

    def check1(self):
        global pn,n,xmin,xmax,dx,delta
        n = self.ui.lineEdit.text()
        #print(isint(n))
        if isint(n)==True:
            if int(n)>1:
                self.ui.textBrowser.setText('OK!\n\nЗаполните следующую форму ниже...')
                self.ui.check1.setText('OK!')
                n = int(n)
                pn = [[0]*(n+1) for i in range(n)]
                self.ui.check2.setEnabled(True)
                self.ui.progressBar.setValue(25)
                self.ui.check1.setEnabled(False)
            else:
                self.ui.textBrowser.setText('Error!\n\nКол-во пар должно быть больше 2!')
        else:
            self.ui.textBrowser.setText('Error!\n\nЗаполните форму натуральным числом!\n\nКол-во пар должно быть больше 2!')

    def check2(self):
        global pn,n,xmin,xmax,dx,delta
        xmin = self.ui.lineEdit_2.text()
        xmax = self.ui.lineEdit_5.text()
        if isfloat(xmin)==True and isfloat(xmax)==True:
            xmin = float(xmin)
            xmax = float(xmax)
            if xmin<xmax:
                self.ui.textBrowser.setText('OK!\n\nЗаполните следующую форму ниже...')
                self.ui.check2.setText('OK!')
                self.ui.check3.setEnabled(True)
                self.ui.progressBar.setValue(50)
                self.ui.check2.setEnabled(False)
                dx=(xmax-xmin)/20
            else:
                self.ui.textBrowser.setText('Error!\n\nПервое число должно быть меньше второго!')
        else:
            self.ui.textBrowser.setText('Error!\n\nЗаполните формы числами!\n\nТакже первое число должно быть меньше второго!')

    def check3(self):
        global pn,n,xmin,xmax,dx,delta
        delta = self.ui.lineEdit_3.text()
        if isfloat(delta)==True:
            delta = float(delta)
            if delta>0:
                self.ui.textBrowser.setText('OK!\n\nЗаполните следующую форму ниже...')
                self.ui.check3.setText('OK!')
                self.ui.check3.setEnabled(False)
                self.ui.progressBar.setValue(75)
                self.ui.check4.setEnabled(True)
            else:
                self.ui.textBrowser.setText('Error!\n\nЧисло должно быть положительным!')
        else:
            self.ui.textBrowser.setText('Error!\n\nЗаполните форму числом!\n\nЧисло должно быть положительным!')


    def check4(self):
        global pn,n,xmin,xmax,dx,delta,xlist,ylist
        stroki=self.ui.textEdit.toPlainText()
        mas=stroki.split('\n')
        lent = len(mas)
        d=0
        if lent==n:
            for i in range(lent):
                c = mas[i].count(' ')
                if c!=1:
                    self.ui.textBrowser.setText('Error!\n\nЗаполните каждую строку правильно!\n\nНапример:\n45 90\n50 100\n55 110')
                    d=0
                    return 0
                else:
                    x, y = mas[i].split(' ')
                    if isfloat(x)==True and isfloat(y)==True:
                        x = float(x)
                        y = float(y)
                        if i>0 and x-pn[i-1][0]==delta:
                            
                            d=1
                        elif i>0 and x-pn[i-1][0]!=delta:
                            d=0
                            break
                        pn[i][0], pn[i][1] = x, y
                    else:
                        self.ui.textBrowser.setText('Error!\n\nЗаполните каждую строку только цифрами!')
                        break
            if d==1:
                self.ui.textBrowser.setText('Все данные успешно введены!\n\nПриступаю к вычислениям...\n\nВыполено! Теперь можно построить график функции, а также посчитать значение F(x) в любой точке')
                self.ui.check4.setText('OK!')
                self.ui.check4.setEnabled(False)
                self.ui.progressBar.setValue(100)
                self.ui.print_y.setEnabled(True)
                self.ui.drow_graph.setEnabled(True)
                append_interpolation(pn, n)
                xlist = []
                x=xmin
                while x<=xmax:
                    xlist.append(x)
                    x+=dx
                ylist = [solve_interpolation(pn, n, x) for x in xlist]
            else:
                self.ui.textBrowser.setText('Error!\n\nПроверьте шаг между точками X\nВ записи шаг должен совпадать со значением в условии!')
        else:
            self.ui.textBrowser.setText('Error!\n\nСтрок должно быть столько же, сколько пар (X,Y) было введено!\nСтрока не должна быть пустой!')


    def drow_graph(self):
        pylab.plot(xlist, ylist)
        pylab.show()

    def print_y(self):
        global pn,n,xmin,xmax,dx,delta
        xx = self.ui.lineEdit_4.text()
        stroka = 'F(x) = '
        if isfloat(xx)==True:
            xx = float(xx)
            f = solve_interpolation_find_y(pn, n, xx)
            stroka+=str(f)
            self.ui.textBrowser_2.setText(stroka)
            self.ui.textBrowser.setText('OK!\n\nПолучено значение функции F('+str(xx)+'):')
        else:
            self.ui.textBrowser.setText('Error!\n\nЗаполните форму числом!')



def isint(s): #проверка на целостность числа
    try:
        int(s)
        return True
    except ValueError:
        return False

def isfloat(s): #проверка на число
    try:
        float(s)
        return True
    except ValueError:
        return False
n=int()
delta=float()
pn=[]
xmin=float()
dx=float()
xmax=float()
xlist = []
ylist = []

def append_interpolation(a, n):     #k - номер эл-та в столбце от нуля, l - номер столбца от нуля
    k=n-1
    for i in range(2,n+1):
        for j in range(k):
            a[j][i]=solving(a, j, i)
        k-=1
    return 0

def solving(a, index_1, index_2):    #index_1 - номер порядка, index_2 - индекс, который хотим посчитать
    solve = (a[index_1+1][index_2-1]-a[index_1][index_2-1])/(a[index_2-1][0]-a[0][0])
    return solve

def solve_interpolation(a, n, x):
    summa = 0
    for i in range(n):
        k=1
        for j in range(i):
            k*=(x-a[j][0])
            #print('a[j][0] = ', a[j][0])
        summa+=a[0][i+1]*k
        #print('a[0][i+1] = ', a[0][i+1])
    return summa

def solve_interpolation_find_y(a, n, x):
    summa = 0
    for i in range(n):
        k=1
        for j in range(i):
            k*=(x-a[j][0])
            #print('a[j][0] = ', a[j][0])
        summa+=a[0][i+1]*k
        #print('a[0][i+1] = ', a[0][i+1])
    return summa



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
