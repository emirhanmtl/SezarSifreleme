def sezar(mesaj, sayı):

    sifrelenmis_mesaj = ''

    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in mesaj:

        if i not in alfabe:

            sifrelenmis_mesaj += i

        else:

            sifrelenmis_mesaj += alfabe[(alfabe.index(i)+sayı) % len(alfabe)]
        
    print("Şifrelenmiş mesaj:", sifrelenmis_mesaj)

mesaj = input("Mesajı giriniz: ")
sayı = int(input("Atlama sayısını giriniz: "))

sezar(mesaj, sayı)