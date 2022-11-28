import random;
durum = True;
while durum:
 print("Seçim yapınız");
 print("1 : Taş");
 print("2 : Kağıt");
 secim = input("3 : Makas");
 botsecim = random.randint(1,3);

#Berabere Durumları
 if secim == "1" and botsecim == 1:
   print("RAKIP : TAŞ");
   print("SEN : TAŞ");
   print("Sonuç : Berabere");
 elif secim == "2" and botsecim == 2:
   print("RAKIP : KAĞIT");
   print("SEN : KAĞIT");
   print("Sonuç : Berabere");
 elif secim == "3" and botsecim == 3:
   print("RAKIP : MAKAS");
   print("SEN : MAKAS");
   print("Sonuç : Berabere");
 #Kazanma Durumları
 elif secim == "1" and botsecim == 3:
   print("RAKIP : MAKAS");
   print("SEN : TAŞ");
   print("Sonuç : Kazandın");
 elif secim == "2" and botsecim == 1:
   print("RAKIP : TAŞ");
   print("SEN : KAĞIT");
   print("Sonuç : Kazandın");
 elif secim == "3" and botsecim == 2:
   print("RAKIP : KAĞIT");
   print("SEN : MAKAS");
   print("Sonuç : Kazandın");
 #Kaybetme durumları
 elif secim == "1" and botsecim == 2:
   print("RAKIP : KAĞIT");
   print("SEN : TAŞ");
   print("Sonuç : Kaybettin");
 elif secim == "2" and botsecim == "3":
   print("RAKIP : MAKAS");
   print("SEN : KAĞIT");
   print("Sonuç : Kaybettin");
 elif secim == "3" and botsecim == 1:
   print("RAKIP : TAŞ");
   print("SEN : MAKAS");
   print("Sonuç : Kaybettin");
