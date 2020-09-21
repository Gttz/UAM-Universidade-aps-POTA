from random import sample
import timeit


def Bubblesort(vetor):
    qntdComparacoes = 0
    for i in range(0, len(vetor)):
        for j in range(0, len(vetor) - 1):
            qntdComparacoes += 1
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    listaComparacoesB.append(qntdComparacoes)


def Insertionsort(vetor):
    qntdComparacoes = 0
    for i in range(1, len(vetor)):
        key = vetor[i]
        j = i - 1
        qntdComparacoes += 1
        while j >= 0 and vetor[j] > key:
            qntdComparacoes += 1
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = key
    listaComparacoesI.append(qntdComparacoes)


def Selectionsort(vetor):
    qntdComparacoes = 0
    for i in range(0, len(vetor)):
        menor = i
        for j in range(i + 1, len(vetor)):
            qntdComparacoes += 1
            if vetor[j] < vetor[menor]:
                menor = j
        temp = vetor[i]
        vetor[i] = vetor[menor]
        vetor[menor] = temp
    listaComparacoesS.append(qntdComparacoes)


def Mergesort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor)
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        Mergesort(vetor, inicio, meio)
        Mergesort(vetor, meio, fim)
        particao(vetor, inicio, meio, fim)


def particao(vetor, inicio, meio, fim, qntdComparacoes=0):
    esq = vetor[inicio:meio]
    dire = vetor[meio:fim]
    i = j = 0
    for k in range(inicio, fim):
        qntdComparacoes += 1
        if i >= len(esq):
            vetor[k] = dire[j]
            j += 1
        elif j >= len(dire):
            vetor[k] = esq[i]
            i += 1

        elif esq[i] < dire[j]:
            vetor[k] = esq[i]
            i += 1
        else:
            vetor[k] = dire[j]
            j += 1
    listaComparacoesM.append(qntdComparacoes)


def QuickSort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1
    if inicio < fim:
        p = intercalar(vetor, inicio, fim)
        QuickSort(vetor, inicio, p - 1)
        QuickSort(vetor, p + 1, fim)


def intercalar(vetor, inicio, fim):
    qntdComparacoes = 0
    pivo = vetor[inicio]
    i = inicio + 1
    j = fim
    while i <= j:
        qntdComparacoes += 1
        if vetor[i] < pivo:
            i += 1
        else:
            if vetor[j] > pivo:
                j -= 1
            else:
                temp = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = temp
                i += 1
                j -= 1
    vetor[inicio] = vetor[j]
    vetor[j] = pivo
    listaComparacoesQ.append(qntdComparacoes)
    return j


def HeapSort(vetor):
    tamanho = len(vetor)
    i = int(tamanho / 2 - 1)
    while i >= 0:
        transformaEmHeap(vetor, tamanho, i)
        i -= 1

    i = int(tamanho - 1)
    while i > 0:
        temp = vetor[0]
        vetor[0] = vetor[i]
        vetor[i] = temp
        transformaEmHeap(vetor, i, 0)
        i -= 1


def transformaEmHeap(vetor, tamanho, raiz, qntdComparacoes=0):
    esq = 2 * raiz + 1
    dire = 2 * raiz + 2
    maior = raiz
    qntdComparacoes += 1
    if esq < tamanho and vetor[esq] > vetor[maior]:
        maior = esq
    qntdComparacoes += 1
    if dire < tamanho and vetor[dire] > vetor[maior]:
        maior = dire

    if maior != raiz:
        temp = vetor[maior]
        vetor[maior] = vetor[raiz]
        vetor[raiz] = temp
        transformaEmHeap(vetor, tamanho, maior)
    listaComparacoesH.append(qntdComparacoes)


listaComparacoesB = list()
listaComparacoesI = list()
listaComparacoesS = list()
listaComparacoesM = list()
listaComparacoesQ = list()
listaComparacoesH = list()
