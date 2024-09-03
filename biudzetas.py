import pickle


class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma} (siuntėjas - {self.siuntejas}, info - {self.info})"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymas, isigyta):
        super().__init__(suma)
        self.atsiskaitymas = atsiskaitymas
        self.isigyta = isigyta

    def __str__(self):
        return f"Išlaidos: {self.suma} (atsiskaitymo būdas - {self.atsiskaitymas}, įsigyta - {self.isigyta})"


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_faila()

    def nuskaityti_faila(self):
        try:
            with open("biudzeto_zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_faila(self):
        with open("biudzeto_zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self):
        suma = abs(float(input("Suma: ")))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_faila()

    def prideti_islaidu_irasa(self):
        suma = abs(float(input("Suma: ")))
        atsiskaitymas = input("Atsiskaitymo būdas: ")
        isigyta = input("Įsigyta prekė/paslauga: ")
        irasas = IslaiduIrasas(suma, atsiskaitymas, isigyta)
        self.zurnalas.append(irasas)
        self.irasyti_faila()

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            if type(irasas) is IslaiduIrasas:
                balansas -= irasas.suma
        return balansas

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)


biudzetas = Biudzetas()

while True:
print("Pasirinkite veiksmą")
    veiksmas = int(input("""
1 - įvesti pajamas
2 - įvesti išlaidas
3 - parodyti žurnalą
4 - parodyti balansą
0 - išeiti
"""))
    match veiksmas:
        case 1:
            biudzetas.prideti_pajamu_irasa()
        case 2:
            biudzetas.prideti_islaidu_irasa()
        case 3:
            biudzetas.parodyti_ataskaita()
        case 4:
            print(biudzetas.gauti_balansa())
        case 0:
            print("Viso gero")
            break
