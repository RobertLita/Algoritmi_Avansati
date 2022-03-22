import random
import math

a = b = c = 0  # coeficientii polinomului de grad 2
dimPopulatie = 0
st = dr = 0  # domeniul de definitie al functiei
precizie = 0
pr = pm = 0  # probabilitatea de recombinare si mutatie
nrEtape = 0
lungime = 0  # lungimea unui cromozom


class Cromozom:
    numarCromozomi = 0

    def __init__(self):
        self.codificare = self.codifica()
        self.valoare = self.transforma10()
        self.fitness = self.calculeazaFitness()
        self.pSelectie = 0

    def calculeazaFitness(self):
        return a * self.valoare * self.valoare + b * self.valoare + c

    def transforma10(self):
        p = 1
        x = 0
        for i in range(lungime - 1, -1, -1):
            x += p * self.codificare[i]
            p *= 2
        x = (dr - st) / (pow(2, lungime) - 1) * x + st
        return x

    def __repr__(self):
        return f"{self.afisareCodificare()} x = {self.valoare} fitness = {self.fitness}"

    def afisareCodificare(self):
        return "".join(str(gena) for gena in self.codificare)

    def setPSelectie(self, F):
        self.pSelectie = self.fitness / F

    @staticmethod
    def genereazaValoare():
        return round(random.uniform(-1, 2), precizie)

    @staticmethod
    def codifica():
        cod = [random.randint(0, 1) for _ in range(lungime)]
        return cod


def lungimeCromozom():
    global lungime
    lungime = int(math.log2((dr - st) * pow(10, precizie))) + 1


def citire():
    global a, b, c, dimPopulatie, st, dr, precizie, pr, pm, nrEtape, lungime
    with open("input.txt") as f:
        dimPopulatie = int(f.readline())
        (st, dr) = (int(x) for x in f.readline().split())
        (a, b, c) = (int(x) for x in f.readline().split())
        precizie = int(f.readline())
        pr = float(f.readline())
        pm = float(f.readline())
        nrEtape = int(f.readline())
    lungimeCromozom()


class Populatie:

    def __init__(self, listaCromozomi=None):
        self.cromozomi = listaCromozomi or [Cromozom() for _ in range(dimPopulatie)]
        self.elitist = self.getElitist()
        self.intervalSelectie = []
        self.dupaSelectie = []
        self.elemGenerateSelectie = []

    def __repr__(self):
        return '\n'.join('   ' + str(i + 1) + ': ' + str(self.cromozomi[i]) for i in range(len(self.cromozomi)))

    def getElitist(self):
        mx = 0
        e = 0
        for cromozom in self.cromozomi:
            if cromozom.fitness > mx:
                mx = cromozom.fitness
                e = cromozom
        return e

    def asociazaPSelectie(self):
        s = 0
        for cromozom in self.cromozomi:
            s += cromozom.fitness
        for cromozom in self.cromozomi:
            cromozom.setPSelectie(s)

    def vectorProbabilitati(self):
        self.asociazaPSelectie()
        v = [0]
        sp = 0
        for cromzom in self.cromozomi:
            sp += cromzom.pSelectie
            v.append(sp)
        self.intervalSelectie = v

    def selectie(self):
        self.vectorProbabilitati()
        selectati = []
        for _ in range(dimPopulatie - 1):
            elem = random.uniform(0, 1)
            poz = Populatie.cautareBinara(self.intervalSelectie, elem) - 1
            self.elemGenerateSelectie.append((elem, poz))
            selectati.append(self.cromozomi[poz])
        self.dupaSelectie = selectati

    def incrucisare(self):
        pass

    def recombinare(self):
        pass

    def mutatie(self):
        pass

    def afisareDupaSelectie(self):
        return '\n'.join('   ' + str(i + 1) + ': ' + str(self.dupaSelectie[i]) for i in range(len(self.dupaSelectie)))

    def afisareIntervalSelectie(self):
        return '\n'.join(
            'C' + str(i + 1) + ': [' + str(self.intervalSelectie[i]) + ', ' + str(self.intervalSelectie[i + 1]) + ')'
            for i in range(len(self.intervalSelectie) - 1))

    def afisareElemGenerate(self):
        return '\n'.join('S-a generat numarul ' + str(self.elemGenerateSelectie[i][0]) + ' si a fost selectat C' + str(
            self.elemGenerateSelectie[i][1] + 1) for i in range(len(self.elemGenerateSelectie)))

    def afisarePSelectie(self):
        return '\n'.join('cromozom   ' + str(i + 1) + ' probabilitate ' + str(self.cromozomi[i].pSelectie) for i in
                         range(len(self.cromozomi)))

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
    print("Populatie initiala")
    p = Populatie()                         # generam populatia initiala
    print(p)                                # o afisam
    p.selectie()                            # aplicam criteriul de selectie
    print(p.afisarePSelectie())             # afisam probabilitatile de selectie
    print(p.afisareIntervalSelectie())      # afisam intervalele de selectie
    print(p.afisareElemGenerate())          # afisam elementele random generate de la "ruleta"
    print(p.afisareDupaSelectie())          # afisam cromozomii care au fost selectati


if __name__ == '__main__':
    rezolva()
