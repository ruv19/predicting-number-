from random import randint

rand = randint(1,100)
sayac = 0

print('SAYİ TAHMİN OYUNUNA HOSGELDİNİZ!')

while True:
    sayac+= 1
    sayi1 = int(input('1 ile 100 arasindan bir sayi tahmin ediniz'))
    if (sayi1 == rand):
        print('sayiyi bildiniz:)')
        print('secilen sayi= {}'.format(sayi1))
        break
    elif sayi1>rand:
        print('girdiginiz sayi secilen sayidan buyuktur!')
        continue
    elif sayi1<rand:
        print('girdiginiz sayi secilen sayidan kucuktur!') 
        continue
