import random
class Hasta():
    def __init__(self,hast_ad,hast_yaşı,kan_değ):
        self.hast_ad=hast_ad
        self.hast_yaşı=hast_yaşı
        self.kan_değ=kan_değ
    def saglık_puan_hesapla(self):
        sum = 0
        for i in self.kan_değ:
            sum += self.kan_değ[i]
        return sum / 3
    def kontrol(self):
        if self.saglık_puan_hesapla()<=40:
            return True
        else:
            return False
    def bilgi_ver(self):
        print("Hasta Bilgileri: \n {} \n {} \n {} ".format(self.hast_ad,self.hast_yaşı,self.kan_değ))
class Doktor():
    def __init__(self, dok_ad, dok_branşı="Enfeksiyon Uzmanı"):
        self.dok_ad = dok_ad
        self.dok_branşı = dok_branşı
    def bilgi_ver(self):
        print("Doktor Bilgileri: \n {} \n {}".format(self.dok_ad, self.dok_branşı))
    def iyileştir(self, other):
        if other.kontrol():
            print("Sağlığınızla ilgili bir probleminiz yok !")
        else:
            other.saglık_puan_hesapla() == random.uniform(20,40)
            print(self.dok_ad + " isimli doktor " + other.hast_ad + " isimli hastayı iyileştirdi ")
class Hastane(Hasta,Doktor):
    def __init__(self,hast_ad,hast_yaşı,kan_değ,dok_ad, dok_branşı,hastane_adı):
        Hasta.__init__(self, hast_ad, hast_yaşı, kan_değ)
        Doktor.__init__(self, dok_ad, dok_branşı)
        self.hastane_adı=hastane_adı
    def bilgi_ver(self):
        Hasta.bilgi_ver(self)
        Doktor.bilgi_ver(self)
        print("Hastane: {}".format(self.hastane_adı))
hastane1=Hastane("Ali",23,{"HGM":13,"CRP":3,"ÜRE":35},"Kemal Kılınç","Enfeksiyon Uzmanı","Medipol")
hastane1.bilgi_ver()