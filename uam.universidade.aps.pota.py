import PyQt5
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QMainWindow, QAction, QMessageBox, \
    QComboBox, QVBoxLayout, QGroupBox
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import sorting
from random import sample
import timeit


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.setGeometry(480, 225, 300, 150)
        self.setWindowTitle('Análise de ordenações')
        self.setWindowIcon(QIcon("semicone.png"))
        self.Components()
        style.use('ggplot')
        self.Menu()

    def Menu(self):
        mainMenu = self.menuBar()

        InfoMenu = mainMenu.addMenu('Informações')
        ButtonInfo = QAction(QIcon('info.jpg'), 'Créditos', self)
        ButtonInfo.setShortcut('Ctrl+A')
        ButtonInfo.triggered.connect(self.Creditos_Clicked)
        InfoMenu.addAction(ButtonInfo)

        SairMenu = mainMenu.addMenu('Outros')
        ButtonSair = QAction(QIcon("icon.sair.png"), 'Sair', self)
        ButtonSair.setShortcut('Ctrl+E')
        ButtonSair.triggered.connect(self.close)
        SairMenu.addAction(ButtonSair)

    def Creditos_Clicked(self):
        QMessageBox.information(self, 'Creditos', "Criador: Lucas Araújo\nCurso: Ciências da Computação\nMatéria: "
                                                  "POTA 4º Semestre\nProfessor: Marvin")

    def Components(self):

        self.label_ordenacao = QLabel(self)
        self.label_ordenacao.setText('Selecionar Sort:')
        self.label_ordenacao.setStyleSheet('QLabel {font:bold;font-size:20;color:"White"}')
        self.label_ordenacao.move(2, 35)
        self.label_ordenacao.resize(125, 20)

        self.label_tipo = QLabel(self)
        self.label_tipo.setText('Selecionar tipo:')
        self.label_tipo.setStyleSheet('QLabel {font:bold;font-size:20;color:"White"}')
        self.label_tipo.move(2, 75)
        self.label_tipo.resize(125, 20)

        self.combo_ordenacao = QComboBox(self)
        vetoresO = ['BubbleSort', 'InsertionSort', 'SelectionSort', 'MergeSort', 'QuickSort', 'HeapSort', 'Todos']
        for i in vetoresO:
            self.combo_ordenacao.addItem(i)
        self.combo_ordenacao.move(100, 35)
        self.combo_ordenacao.resize(100, 20)

        self.combo_tipo = QComboBox(self)
        vetoresT = ["Comparações", 'Tempo']
        for i in vetoresT:
            self.combo_tipo.addItem(i)
        self.combo_tipo.move(100, 75)
        self.combo_tipo.resize(100, 20)

        self.button_solicitar = QPushButton('Solicitar', self)
        self.button_solicitar.move(100, 125)
        self.button_solicitar.resize(87, 20)
        self.button_solicitar.clicked.connect(self.solicitar_clicked)

    def solicitar_clicked(self):
        if self.combo_ordenacao.currentText() == 'BubbleSort':
            listaBubble = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                           sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lt = []
            lo = []
            if self.combo_tipo.currentText() == 'Comparações':
                for i in range(0, 5):
                    sorting.Bubblesort(listaBubble[i])
                    print(f'Quantidade de comparações BubbleSort: {sorting.listaComparacoesB}')
                    lt.append(len(listaBubble[i]))
                    lo.append(sorting.listaComparacoesB[i])

                plt.plot(lt, lo)
                plt.title("BubbleSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Quantidade Comparações")
                plt.show()
                plt.close()
            elif self.combo_tipo.currentText() == 'Tempo':
                tempoB = []
                for i in range(0, 5):
                    inicioBubbleSort = timeit.default_timer()
                    sorting.Bubblesort(listaBubble[i])
                    fimBubbleSort = timeit.default_timer()
                    tempo = fimBubbleSort - inicioBubbleSort
                    print("Tempo de execução BubbleSort : %f4 " % (fimBubbleSort - inicioBubbleSort))
                    tempoB.append(tempo)
                    lt.append(len(listaBubble[i]))
                    lo.append(tempoB[i])

                plt.plot(lt, lo)
                plt.title("BubbleSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Tempo(t)")
                plt.show()
                plt.close()

        elif self.combo_ordenacao.currentText() == 'InsertionSort':
            listaInsertion = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                              sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lt = []
            lo = []
            if self.combo_tipo.currentText() == 'Comparações':
                for i in range(0, 5):
                    sorting.Insertionsort(listaInsertion[i])
                    print(f'Quantidade de comparações InsertionSort: {sorting.listaComparacoesI}')
                    lt.append(len(listaInsertion[i]))
                    lo.append(sorting.listaComparacoesI[i])

                plt.plot(lt, lo)
                plt.title("InsertionSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Quantidade Comparações")
                plt.show()
            elif self.combo_tipo.currentText() == 'Tempo':
                tempoI = []
                for i in range(0, 5):
                    inicioInsertionSort = timeit.default_timer()
                    sorting.Insertionsort(listaInsertion[i])
                    fimInsertionSort = timeit.default_timer()
                    print("Tempo de execução InsertionSort : %f4 " % (fimInsertionSort - inicioInsertionSort))
                    tempo = fimInsertionSort - inicioInsertionSort
                    tempoI.append(tempo)
                    lt.append(len(listaInsertion[i]))
                    lo.append(tempoI[i])

                plt.plot(lt, lo)
                plt.title("InsertionSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Tempo(t)")
                plt.show()

        elif self.combo_ordenacao.currentText() == 'SelectionSort':
            listaSelection = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                              sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lt = []
            lo = []
            if self.combo_tipo.currentText() == 'Comparações':
                for i in range(0, 5):
                    sorting.Selectionsort(listaSelection[i])
                    print(f'Quantidade de comparações SelectionSort: {sorting.listaComparacoesS}')
                    print()
                    lt.append(len(listaSelection[i]))
                    lo.append(sorting.listaComparacoesS[i])

                plt.plot(lt, lo)
                plt.title("SelectionSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Quantidade Comparações")
                plt.show()

            elif self.combo_tipo.currentText() == 'Tempo':
                tempoS = []
                for i in range(0, 5):
                    inicioSelectionSort = timeit.default_timer()
                    sorting.Selectionsort(listaSelection[i])
                    fimSelectionSort = timeit.default_timer()
                    print("Tempo de execução SelectionSort : %f4 " % (fimSelectionSort - inicioSelectionSort))
                    tempo = fimSelectionSort - inicioSelectionSort
                    tempoS.append(tempo)
                    lt.append(len(listaSelection[i]))
                    lo.append(tempoS[i])

                plt.plot(lt, lo)
                plt.title("SelectionSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Tempo(t)")
                plt.show()

        elif self.combo_ordenacao.currentText() == 'MergeSort':
            listaMerge = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                          sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lt = []
            lo = []
            if self.combo_tipo.currentText() == 'Comparações':
                listaComparacoes2M = []
                for i in range(0, 5):
                    sorting.Mergesort(listaMerge[i])
                    listaComparacoes2M.append(sum(sorting.listaComparacoesM))
                    print(f'Quantidade de comparações MergeSort: {listaComparacoes2M}')
                    print()
                    lt.append(len(listaMerge[i]))
                    lo.append(listaComparacoes2M[i])
                plt.plot(lt, lo)
                plt.title("MergeSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Quantidade Comparações")
                plt.show()

            elif self.combo_tipo.currentText() == 'Tempo':
                tempoM = []
                for i in range(0, 5):
                    inicioMergeSort = timeit.default_timer()
                    sorting.Mergesort(listaMerge[i])
                    fimMergeSort = timeit.default_timer()
                    print("Tempo de execução MergeSort : %f4 " % (fimMergeSort - inicioMergeSort))
                    tempo = fimMergeSort - inicioMergeSort
                    tempoM.append(tempo)
                    lt.append(len(listaMerge[i]))
                    lo.append(tempoM[i])

                plt.plot(lt, lo)
                plt.title("MergeSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Tempo(t)")
                plt.show()

        elif self.combo_ordenacao.currentText() == 'QuickSort':
            listaQuick = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                          sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lt = []
            lo = []
            if self.combo_tipo.currentText() == 'Comparações':
                listaComparacoes2Q = []
                for i in range(0, 5):
                    sorting.QuickSort(listaQuick[i])
                    listaComparacoes2Q.append(sum(sorting.listaComparacoesQ))
                    print(f'Quantidade de comparações QuickSort: {listaComparacoes2Q}')
                    lt.append(len(listaQuick[i]))
                    lo.append(listaComparacoes2Q[i])

                plt.plot(lt, lo)
                plt.title("QuickSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Quantidade Comparações")
                plt.show()
            elif self.combo_tipo.currentText() == 'Tempo':
                tempoQ = []
                for i in range(0, 5):
                    inicioQuickSort = timeit.default_timer()
                    sorting.QuickSort(listaQuick[i])
                    fimQuickSort = timeit.default_timer()
                    print("Tempo de execução QuickSort : %f4 " % (fimQuickSort - inicioQuickSort))
                    tempo = fimQuickSort - inicioQuickSort
                    tempoQ.append(tempo)
                    lt.append(len(listaQuick[i]))
                    lo.append(tempoQ[i])

                plt.plot(lt, lo)
                plt.title("QuickSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Tempo(t)")
                plt.show()

        elif self.combo_ordenacao.currentText() == 'HeapSort':
            listaHeap = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                         sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lt = []
            lo = []
            if self.combo_tipo.currentText() == 'Comparações':
                listaComparacoes2H = []
                for i in range(0, 5):
                    sorting.HeapSort(listaHeap[i])
                    listaComparacoes2H.append(sum(sorting.listaComparacoesH))
                    print(f'Quantidade de comparações HeapSort: {listaComparacoes2H}')
                    lt.append(len(listaHeap[i]))
                    lo.append(listaComparacoes2H[i])

                plt.plot(lt, lo)
                plt.title("HeapSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Quantidade Comparações")
                plt.show()
            elif self.combo_tipo.currentText() == 'Tempo':
                tempoH = []
                for i in range(0, 5):
                    inicioHeapSort = timeit.default_timer()
                    sorting.HeapSort(listaHeap[i])
                    fimHeapSort = timeit.default_timer()
                    print("Tempo de execução HeapSort : %f4 " % (fimHeapSort - inicioHeapSort))
                    tempo = fimHeapSort - inicioHeapSort
                    tempoH.append(tempo)
                    lt.append(len(listaHeap[i]))
                    lo.append(tempoH[i])

                plt.plot(lt, lo)
                plt.title("HeapSort")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Tempo(t)")
                plt.show()

        elif self.combo_ordenacao.currentText() == 'Todos':
            listaBubble = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                           sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lbx = []
            lby = []
            listaInsertion = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                              sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lix = []
            liy = []
            listaSelection = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                              sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            lsx = []
            lsy = []
            listaMerge = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                          sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            listaComparacoes2M = []
            lmx = []
            lmy = []
            listaQuick = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                          sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            listaComparacoes2Q = []
            lqx = []
            lqy = []
            listaHeap = [sample(range(0, 5), 5), sample(range(0, 10), 10), sample(range(0, 50), 50),
                         sample(range(0, 100), 100), sample(range(0, 1000), 1000)]
            listaComparacoes2H = []
            lhx = []
            lhy = []
            if self.combo_tipo.currentText() == 'Comparações':
                for i in range(0, 5):
                    # BubbleSort
                    sorting.Bubblesort(listaBubble[i])
                    print(f'Quantidade de comparações BubbleSort: {sorting.listaComparacoesB}')
                    lbx.append(len(listaBubble[i]))
                    lby.append(sorting.listaComparacoesB[i])
                    # InsertionSort
                    sorting.Insertionsort(listaInsertion[i])
                    print(f'Quantidade de comparações InsertionSort: {sorting.listaComparacoesI}')
                    lix.append(len(listaInsertion[i]))
                    liy.append(sorting.listaComparacoesI[i])
                    # SelectionSort
                    sorting.Selectionsort(listaSelection[i])
                    print(f'Quantidade de comparações SelectionSort: {sorting.listaComparacoesS}')
                    lsx.append(len(listaSelection[i]))
                    lsy.append(sorting.listaComparacoesS[i])
                    #MergeSort
                    sorting.Mergesort(listaMerge[i])
                    listaComparacoes2M.append(sum(sorting.listaComparacoesM))
                    print(f'Quantidade de comparações MergeSort: {listaComparacoes2M}')
                    lmx.append(len(listaMerge[i]))
                    lmy.append(listaComparacoes2M[i])
                    #QuickSort
                    sorting.QuickSort(listaQuick[i])
                    listaComparacoes2Q.append(sum(sorting.listaComparacoesQ))
                    print(f'Quantidade de comparações QuickSort: {listaComparacoes2Q}')
                    lqx.append(len(listaQuick[i]))
                    lqy.append(listaComparacoes2Q[i])
                    #HeapSort
                    sorting.HeapSort(listaHeap[i])
                    listaComparacoes2H.append(sum(sorting.listaComparacoesH))
                    print(f'Quantidade de comparações HeapSort: {listaComparacoes2H}')
                    lhx.append(len(listaHeap[i]))
                    lhy.append(listaComparacoes2H[i])

                plt.plot(lbx, lby, label='BubbleSort')
                plt.plot(lix, liy, label='InsertionSort')
                plt.plot(lsx, lsy, label='SelectionSort')
                plt.plot(lmx, lmy, label='MergeSort')
                plt.plot(lqx, lqy, label='QuickSort')
                plt.plot(lhx, lhy, label='HeapSort')
                plt.title("Ordenações por Comparação")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Quantidade Comparações")
                plt.legend()
                plt.show()
                plt.close()
            elif self.combo_tipo.currentText() == 'Tempo':
                tempoB = []
                tempoI = []
                tempoS = []
                tempoM = []
                tempoQ = []
                tempoH = []
                for i in range(0, 5):
                    # BubbleSort
                    inicioBubbleSort = timeit.default_timer()
                    sorting.Bubblesort(listaBubble[i])
                    fimBubbleSort = timeit.default_timer()
                    tempob = fimBubbleSort - inicioBubbleSort
                    print("Tempo de execução Bublesort : %f4 " % (fimBubbleSort - inicioBubbleSort))
                    tempoB.append(tempob)
                    lbx.append(len(listaBubble[i]))
                    lby.append(tempoB[i])
                    # InsertionSort
                    inicioInsertionSort = timeit.default_timer()
                    sorting.Insertionsort(listaInsertion[i])
                    fimInsertionSort = timeit.default_timer()
                    tempoi = fimInsertionSort - inicioInsertionSort
                    print("Tempo de execução InsertionSort : %f4 " % (fimInsertionSort - inicioInsertionSort))
                    tempoI.append(tempoi)
                    lix.append(len(listaInsertion[i]))
                    liy.append(tempoI[i])
                    # SelectionSort
                    inicioSelectionSort = timeit.default_timer()
                    sorting.Selectionsort(listaSelection[i])
                    fimSelectionSort = timeit.default_timer()
                    tempos = fimSelectionSort - inicioSelectionSort
                    tempoS.append(tempos)
                    print("Tempo de execução SelectionSort : %f4 " % (fimSelectionSort - inicioSelectionSort))
                    lsx.append(len(listaSelection[i]))
                    lsy.append(tempoS[i])
                    # MergeSort
                    inicioMergeSort = timeit.default_timer()
                    sorting.Mergesort(listaMerge[i])
                    fimMergeSort = timeit.default_timer()
                    tempom = fimMergeSort - inicioMergeSort
                    tempoM.append(tempom)
                    print("Tempo de execução MergeSort : %f4 " % (fimMergeSort - inicioMergeSort))
                    lmx.append(len(listaMerge[i]))
                    lmy.append(tempoM[i])
                    # QuickSort
                    inicioQuickSort = timeit.default_timer()
                    sorting.QuickSort(listaQuick[i])
                    fimQuickSort = timeit.default_timer()
                    tempoq = fimQuickSort - inicioQuickSort
                    tempoQ.append(tempoq)
                    print("Tempo de execução QuickSort : %f4 " % (fimQuickSort - inicioQuickSort))
                    lqx.append(len(listaQuick[i]))
                    lqy.append(tempoQ[i])
                    # HeapSort
                    inicioHeapSort = timeit.default_timer()
                    sorting.HeapSort(listaHeap[i])
                    fimHeapSort = timeit.default_timer()
                    tempoh = fimHeapSort - inicioHeapSort
                    tempoH.append(tempoh)
                    print("Tempo de execução HeapSort : %f4 " % (fimHeapSort - inicioHeapSort))
                    print()
                    lhx.append(len(listaHeap[i]))
                    lhy.append(tempoH[i])

                plt.plot(lbx, lby, label='BubbleSort')
                plt.plot(lix, liy, label='InsertionSort')
                plt.plot(lsx, lsy, label='SelectionSort')
                plt.plot(lmx, lmy, label='MergeSort')
                plt.plot(lqx, lqy, label='QuickSort')
                plt.plot(lhx, lhy, label='HeapSort')
                plt.title("Ordenações por Tempo")
                plt.xlabel("Tamanho do vetor")
                plt.ylabel("Tempo(T)")
                plt.legend()
                plt.show()
                plt.close()


def main():
    app = QApplication(sys.argv)
    ex = GUI()
    # Dark Mode
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor(240, 240, 240))

    palette.setColor(QPalette.Base, QColor(45, 45, 45))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QPalette.Text, QColor(200, 200, 200))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(200, 200, 200))
    palette.setColor(QPalette.BrightText, QtCore.Qt.red)

    palette.setColor(QPalette.Highlight, QColor(37, 110, 217))
    palette.setColor(QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
