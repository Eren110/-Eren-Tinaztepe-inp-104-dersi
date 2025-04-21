sozcuk = str(input("bir sözcük girin: "))
sayi = int(input("bir sayi girin: "))
harf = str(input("bir harf girin: "))

if sayi < len(sozcuk):
  cevap= sozcuk[:sayi-1] + harf + sozcuk[sayi:]
  print(cevap)
