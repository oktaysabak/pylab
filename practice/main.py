class Insan:
    
    zam = 1.4
    
    def __init__(self, isim, soyisim): #constructor
        self.isim = isim
        self.soyisim = soyisim
    def setMaas(self, maas):
        self.maas = maas
    def getMaas(self):
        return self.maas
    def increaseMaas(self):
        self.maas = self.maas*self.zam
insan1 = Insan('oktay', 'sabak')
insan1.setMaas(500)
print(insan1.isim)
print(insan1.soyisim)
print(insan1.maas)
insan1.increaseMaas()
print(insan1.getMaas())