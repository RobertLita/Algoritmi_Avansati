import random
import math
from copy import deepcopy

a = b = c = 0  # coeficientii polinomului de grad 2
dimPopulatie = 0
st = dr = 0  # domeniul de definitie al functiei
precizie = 0
pi = pm = 0  # probabilitatea de recombinare si mutatie
nrEtape = 0
lungime = 0  # lungimea unui cromozom
elitist = None

fitness = []
pSelectie = []
intervalSelectie = []
elemGenerateSelectie = []
cromozomiIncrucisare = []
rezultatRecombinare = []
cromozomiMutatie = set()


def calculeazaFitness(x):
    if st <= x < dr:
        return a * x * x + b * x + c
    return 0


def lungimeCromozom():
    global lungime
    lungime = int(math.log2((dr - st) * pow(10, precizie))) + 1


def citire():
    global a, b, c, dimPopulatie, st, dr, precizie, pi, pm, nrEtape, lungime, elitist, fitness
    with open("input.txt") as f:
        dimPopulatie = int(f.readline())
        (st, dr) = (int(x) for x in f.readline().split())
        (a, b, c) = (int(x) for x in f.readline().split())
        precizie = int(f.readline())
        pi = float(f.readline())
        pm = float(f.readline())
        nrEtape = int(f.readline())
        elitist = True if int(f.readline()) == 1 else False
    lungimeCromozom()
    fitness = [0 for _ in range(dimPopulatie)]


def listTostring(l):
    return ''.join(map(str, l))


# functii pentru afisari
def afisareIntervalSelectie(g):
    s = '\n'.join(f"C{str(i + 1)}: [{str(intervalSelectie[i])}, {str(intervalSelectie[i + 1])})" for i in
                  range(len(intervalSelectie) - 1))
    g.write("Intervale probabilitatie selectie:\n")
    g.write(s + '\n')


def afisareElemGenerate(g):
    s = '\n'.join(
        f"S-a generat numarul {str(elemGenerateSelectie[i][0])} si a fost selectat C{str(elemGenerateSelectie[i][1] + 1)}"
        for i in range(len(elemGenerateSelectie)))
    g.write(s + '\n')


def afisarePSelectie(cromozomi, g):
    s = '\n'.join(f"cromozom   {str(i + 1)} probabilitate {str(pSelectie[i])}" for i in
                  range(len(cromozomi)))
    g.write("Probabilitati de selectie:\n")
    g.write(s + '\n')


def afisareCromozomiIncrucisare(g):
    s = '\n'.join(
        f"    {str(i + 1)}: {listTostring(cromozomiIncrucisare[i][0])} u = {cromozomiIncrucisare[i][1]} <{pi} participa" if
        cromozomiIncrucisare[i][1] < pi
        else f"    {str(i + 1)}: {listTostring(cromozomiIncrucisare[i][0])} u = {cromozomiIncrucisare[i][1]}" for i
        in range(len(cromozomiIncrucisare)))
    g.write(s + '\n')


def afisareRecombinari(g):
    s = '\n'.join(
        f"Recombinare dintre cromozomul {x[0][1] + 1} cu cromozomul {x[1][1] + 1}:\n"
        f"{listTostring(x[0][0])}  {listTostring(x[1][0])} punct {x[2]}\n"
        f"Rezultat    {listTostring(x[3])}   {listTostring(x[4])}" for x in rezultatRecombinare)
    g.write(s + '\n')


def afisareMutatie(g):
    if len(cromozomiMutatie) != 0:
        g.write("Au fost modificati cromozomii:\n")
        s = '\n'.join(str(x) for x in cromozomiMutatie)
        g.write(s + '\n')
    else:
        g.write("Nu a fost modificat niciun cromozom.\n")


class Cromozom:

    def __init__(self):
        self.valoare = round(random.uniform(st, dr), precizie)
        self.codificare = self.codificare()

    def decodificare(self):
        p = 1
        x = 0
        for i in range(lungime - 1, -1, -1):
            x += p * self.codificare[i]
            p <<= 1
        x = x / pow(10, precizie) + st
        return round(x, precizie)

    def codificare(self):
        cod = []
        v = self.valoare
        v = int((v - st) * pow(10, precizie))
        while v > 0 or len(cod) != lungime:
            gena = v & 1
            v >>= 1
            cod.append(gena)
        cod.reverse()
        return cod

    def __repr__(self):
        return f"{self.afisareCodificare()} x = {self.valoare} fitness = {calculeazaFitness(self.valoare)} "

    def afisareCodificare(self):
        return "".join(str(gena) for gena in self.codificare)


class Populatie:

    def __init__(self, listaCromozomi=None):
        self.cromozomi = listaCromozomi or [Cromozom() for _ in range(dimPopulatie)]
        self.elitist = None

    def __repr__(self):
        return '\n'.join('   ' + str(i + 1) + ': ' + str(self.cromozomi[i]) for i in range(len(self.cromozomi)))

    def getElitist(self):
        mx = 0
        e = 0
        for i in range(len(self.cromozomi)):
            if fitness[i] > mx:
                mx = fitness[i]
                e = self.cromozomi[i]
        return e

    def fitnessList(self):
        global fitness
        for i in range(len(self.cromozomi)):
            f = calculeazaFitness(self.cromozomi[i].valoare)
            fitness[i] = f

    def selectie(self):
        global intervalSelectie, elemGenerateSelectie
        intervalSelectie = []
        elemGenerateSelectie = []
        sumaFitness = sum(fitness)
        self.elitist = self.getElitist()
        sumaInterval = 0
        intervalSelectie.append(0)
        for i in range(len(self.cromozomi)):
            ps = fitness[i] / sumaFitness
            pSelectie.append(ps)
            sumaInterval += ps
            intervalSelectie.append(sumaInterval)
        selectati = []
        dimPopulatieSelectie = dimPopulatie - 1 if elitist else dimPopulatie
        for _ in range(dimPopulatieSelectie):
            u = random.uniform(0, 1)
            poz = Populatie.cautareBinara(intervalSelectie, u) - 1
            elemGenerateSelectie.append((u, poz))
            selectati.append(deepcopy(self.cromozomi[poz]))
        self.cromozomi = selectati

    def incrucisare(self):
        global cromozomiIncrucisare, rezultatRecombinare
        participaIncrucisare = []
        cromozomiIncrucisare = []
        rezultatRecombinare = []
        for i in range(len(self.cromozomi)):
            u = random.uniform(0, 1)
            cromozomiIncrucisare.append((self.cromozomi[i].codificare, u))
            if u < pi:
                participaIncrucisare.append((self.cromozomi[i].codificare, i))
        if len(participaIncrucisare) & 1 == 1:
            participaIncrucisare.append(participaIncrucisare[0])
        for i in range(0, len(participaIncrucisare) - 1, 2):
            self.recombinare(participaIncrucisare[i], participaIncrucisare[i + 1])

    def recombinare(self, c1, c2):
        global rezultatRecombinare
        punct = random.randrange(0, lungime)
        c11 = c1[0][0:punct]
        c12 = c1[0][punct:]
        c21 = c2[0][0:punct]
        c22 = c2[0][punct:]
        C1 = c21 + c12
        C2 = c11 + c22
        self.cromozomi[c1[1]].codificare = C1
        self.cromozomi[c1[1]].valoare = self.cromozomi[c1[1]].decodificare()
        self.cromozomi[c2[1]].codificare = C2
        self.cromozomi[c2[1]].valoare = self.cromozomi[c2[1]].decodificare()
        rezultatRecombinare.append((c1, c2, punct, C1, C2))

    def mutatie(self):
        global cromozomiMutatie
        cromozomiMutatie = set()
        for i in range(len(self.cromozomi)):
            for j in range(len(self.cromozomi[i].codificare)):
                u = random.uniform(0, 1)
                if u < pm:
                    if self.cromozomi[i].codificare[j] == 0:
                        self.cromozomi[i].codificare[j] = 1
                    else:
                        self.cromozomi[i].codificare[j] = 0
                    cromozomiMutatie.add(i + 1)
            if i + 1 in cromozomiMutatie:
                self.cromozomi[i].valoare = self.cromozomi[i].decodificare()
        if elitist:
            self.cromozomi.append(self.elitist)
        try:
            self.fitnessList()
        except AttributeError:
            pass

    @staticmethod
    def cautareBinara(lista, k):
        x = 0
        y = len(lista) - 1
        while x <= y:
            mij = (x + y) // 2
            if y - x == 1:
                return y
            if k < lista[mij]:
                y = mij
            else:
                x = mij


def rezolva():
    citire()
    g = open("output.txt", 'w')
    g.write("Populatie initiala\n")
    p = Populatie()  # generam populatia initiala
    p.fitnessList()
    g.write(str(p) + '\n')  # o afisam
    p.selectie()  # aplicam criteriul de selectie
    afisarePSelectie(p.cromozomi, g)  # afisam proabilitatile de selectie
    afisareIntervalSelectie(g)  # afisam intervalele de selectie
    afisareElemGenerate(g)  # afisam elementele random generate de la "ruleta"
    g.write("Dupa selectie:\n" + str(p) + '\n')  # afisam cromozomii care au fost selectati
    g.write("Probabilitatea de incrucisare " + str(pi) + '\n')
    p.incrucisare()
    afisareCromozomiIncrucisare(g)
    afisareRecombinari(g)
    g.write("Dupa recombinare:\n")
    g.write(str(p) + '\n')
    g.write("Probabilitatea de mutatie pentru fiecare gena " + str(pm) + '\n')
    p.mutatie()
    afisareMutatie(g)
    g.write("Dupa mutatie:\n" + str(p) + '\n')
    g.write("Evolutia maximului:\n")
    for _ in range(nrEtape - 1):
        g.write(str(calculeazaFitness(p.getElitist().valoare)) + '\n')
        p.selectie()
        p.incrucisare()
        p.mutatie()


if __name__ == '__main__':
    rezolva()
