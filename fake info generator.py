from random import choice, randint
from time import sleep

erkekad = ["Ahmet", "Ali" "Mehmet", "Can", "Yusuf", "Efe", "Doruk", "Ömer", "Faruk", "Arda", "Murat", "Mehmet", "Tuna", "Alp", "Recep", "Berat", "Kayra", "Görkem", "Utku", "Kaan", "Eymen", "Aras", "Miraç", "Hamza", "Emir"]
kizad = ["Ayşe", "Fatma", "Elif", "Zeynep", "Defne", "Rabia", "Eylül", "Ecrin", "Aslı", "Bahar", "Betül" "Büşra", "Dilara", "Tuğba", "Yağmur", "Ebru", "Ece", "Hande", "Selin", "Irmak", "Kübra", "Leyla", "Melek" "Müge", "Nazlı", "Nehir"]
soyad = ["Yılmaz", "Yıldız", "Kılıç", "Güneş", "Akyol", "Bademci", "Yazıcı", "Bakırcı", "Bayraktar", "Bozkurt", "Kaya", "Demir", "Ekici", "Yıldırım", "Öztürk", "Çetin", "Şimşek", "Korkmaz", "Erdoğan", "Çakır", "Çakıcı"]
il = ["Adana", "İstanbul", "Kırıkkale", "Ankara", "Kırşehir", "Bingöl", "Konya", "Bursa", "İzmir", "Muğla", "Antalya", "Erzurum", "Sivas", "Van", "Tunceli", "Hatay", "Trabzon", "Eskişehir", "Adıyaman", "Kahramanmaraş", "Gaziantep"]

while True:
  print("[=================================]")
  print("      TCW Fake İnfo Generator      ")
  print("         Made by Howert          ")
  print("[=================================]")
  cinsiyet = int(input("Oluşturacağınız fake info cinsiyetini girin \n1- Erkek\n2- Kız\n3- Rastgele\n >> "))
  if cinsiyet == 1:
     maxyas = int(input("Fake info max yaşını girin >> "))
     minyas = int(input("Fake info min yaşını girin >> "))
     print("Random info oluşturuluyor...")
     isim = choice(erkekad)
     soyadd = choice(soyad)
     şehir = choice(il)
     yas = randint(minyas, maxyas)
     sleep(2)
     print(f"Fake info oluşturuldu :\n Ad : {isim} \n Soyad : {soyadd}, \n Şehir : {şehir} \n Yaş : {yas}")
     secim = input("Tekrar bir info üretmek ister misiniz? E/H \n >> ")
     if secim == "E":
         pass
     else:
         print("Programdan çıkılıyor...")
         sleep(1.5)
         break
  if cinsiyet == 2:
      maxyas = int(input("Fake info max yaşını girin >> "))
      minyas = int(input("Fake info min yaşını girin >> "))
      print("Random info oluşturuluyor...")
      isim = choice(kizad)
      soyadd = choice(soyad)
      şehir = choice(il)
      yas = randint(minyas, maxyas)
      sleep(2)
      print(f"Fake info oluşturuldu :\n Ad : {isim} \n Soyad : {soyadd}, \n Şehir : {şehir} \n Yaş : {yas}")
      secim = input("Tekrar bir info üretmek ister misiniz? E/H \n >> ")
      if secim == "E":
          pass
      else:
          print("Programdan çıkılıyor...")
          break
  if cinsiyet == 3:
      print("Rastgele cinsiyet seçiliyor...")
      sleep(1.5)
      cinsiyet = ["Kız", "Erkek"]
      randomcinsiyet = choice(cinsiyet)
      if randomcinsiyet == "Kız":
          print("Seçilen cinsiyet : Kız")
          maxyas = int(input("Fake info max yaşını girin >> "))
          minyas = int(input("Fake info min yaşını girin >> "))
          print("Random info oluşturuluyor...")
          isim = choice(kizad)
          soyad = choice(soyad)
          şehir = choice(il)
          yas = randint(minyas, maxyas)
          sleep(2)
          print(f"Fake info oluşturuldu :\n Ad : {isim} \n Soyad : {soyad}, \n Şehir : {şehir} \n Yaş : {yas}")
          secim = input("Tekrar bir info üretmek ister misiniz? E/H \n >> ")
          if secim == "E":
              pass
          else:
              print("Programdan çıkılıyor...")
              sleep(1.5)
              break
      if randomcinsiyet == "Erkek":
          print("Seçilen cinsiyet : Erkek")
          maxyas = int(input("Fake info max yaşını girin >> "))
          minyas = int(input("Fake info min yaşını girin >> "))
          print("Random info oluşturuluyor...")
          isim = choice(erkekad)
          soyadd = choice(soyad)
          şehir = choice(il)
          yas = randint(minyas, maxyas)
          sleep(2)
          print(f"Fake info oluşturuldu :\n Ad : {isim} \n Soyad : {soyadd}, \n Şehir : {şehir} \n Yaş : {yas}")
          secim = input("Tekrar bir info üretmek ister misiniz? E/H \n >> ")
          if secim == "E":
              pass
          else:
              print("Programdan çıkılıyor...")
              sleep(1.5)
              break
      else:
          print("Hatalı işlem.")
          sleep(1)
  else:
      print("Hatalı işlem.")




