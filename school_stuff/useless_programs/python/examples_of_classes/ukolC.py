#!/usr/bin/env python

# Skupina C

class Zviratko:
    def __init__(self, jmeno, vek, vaha):
        self.jmeno = jmeno
        self.vek = vek
        self.vaha = vaha
        self.cisloChlivku = None
    def __str__(self):
        return "Jsem {}, mám {} roky a vážím {} kg.".format(self.jmeno, self.vek, self.vaha)
    
class Dvorecek:
    def __init__(self, zviratko1, zviratko2):
        self.zviratko1 = zviratko1
        self.zviratko2 = zviratko2
    def ubytujZviratka(self):
        if self.zviratko1.vaha > self.zviratko2.vaha:
            self.zviratko1.cisloChlivku = 2
            self.zviratko2.cisloChlivku = 1
        elif self.zviratko1.vaha < self.zviratko2.vaha:
            self.zviratko1.cisloChlivku = 1
            self.zviratko2.cisloChlivku = 2
        elif self.zviratko1.vaha == self.zviratko2.vaha:
            if self.zviratko1.vek < self.zviratko2.vek:
                self.zviratko1.cisloChlivku = 1
                self.zviratko2.cisloChlivku = 2
            elif self.zviratko1.vek > self.zviratko2.vek:
                self.zviratko2.cisloChlivku = 1
                self.zviratko1.cisloChlivku = 2
        return "{} Bydlím v chlívku číslo {}.\n{} Bydlím v chlívku číslo {}.".format(self.zviratko1, self.zviratko1.cisloChlivku, self.zviratko2, self.zviratko2.cisloChlivku)
    def __str__(self):
        return self.ubytujZviratka()

prasatko = Zviratko("prasátko", 2, 60)
telatko = Zviratko("telátko", 1, 70)
dvorecek = Dvorecek(prasatko, telatko)
print(dvorecek)
