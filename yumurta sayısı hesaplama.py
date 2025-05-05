
yumurta_sayisi = int(input("Bu sabah kaç yumurta topladınız? (100-150 arası): "))


kutu_12 = yumurta_sayisi // 12
kalan_yumurta = yumurta_sayisi % 12


kutu_6 = kalan_yumurta // 6
kalan_yumurta = kalan_yumurta % 6


print("\n12'lik kutu sayısı: {kutu_12}")
print("6'lık kutu sayısı: {kutu_6}")
print("Kahvaltı için kalan yumurta sayısı: {kalan_yumurta}")