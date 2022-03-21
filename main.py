import numpy as np
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
        Cromozom.numarCromozomi += 1
        self.id = Cromozom.numarCromozomi

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
        return f"{self.id}: {self.afisareCodificare()} x = {self.valoare} fitness = {self.fitness}"

    def afisareCodificare(self):
        return "".join(str(gena) for gena in self.codificare)

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

    def __init__(self):
        self.cromozomi = [Cromozom() for _ in range(dimPopulatie)]

    def __repr__(self):
        return '\n'.join(str(cromozom) for cromozom in self.cromozomi)

    def selectie(self):
        pass

    def incrucisare(self):
        pass

    def recombinare(self):
        pass

    def mutatie(self):
        pass

if __name__ == '__main__':
    citire()
    p = Populatie()
    print(p)
