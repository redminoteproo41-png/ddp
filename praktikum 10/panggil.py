import bangunRuang as br
import bangunDatar as bd


print("~~~~ BANGUN RUANG ~~~~")
print(f"Volum Kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volum Balok adalah {br.balok(4, 5, 2)}")
print(f"Volum Prisma Segitiga adalah {br.prisma(5,4,5)}")
print(f"Volum Tabung adalah {br.tabung (3, 5)}")
print(f"Volum Kerucut adalah {br.kerucut (5, 8)}")

print("~~~~ BANGUN DATAR ~~~~")
print(f"Luas Persegi adalah {bd.persegi(5)} ")
print(f"Luas Persegi Panjang adalah {bd.Persegi_Panjang(5, 3)} ")
print(f"Luas Segitiga adalah {bd.Segitiga(3, 5)}")
print(f"Luas Lingkaran adalah {bd.Lingkaran(5)} ")
print(f"Luas JajarGenjang adalah {bd.JajarGenjang(4,7)}")