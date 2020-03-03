import string
import random
def passwd_olusturma(level,leght,output=[]):
    if level==1:
        chars=string.digits
    elif level==2:
        chars=string.ascii_letters
    elif level==3:
        chars=string.hexdigits
    else:
        print("Yanlıs seviye girdiniz...")
        exit()
    for i in range(0,leght):
        output.append(random.choice(chars))
    return "".join(output)
print("*" *80 +"\nSIFRENIZIN SAYILARDAN OLUSMASINI ISTIYORSANIZ 1 E BASIN")
print("SIFRENIZIN HARFLERDEN OLUSMASINI ISTIYORSANIZ 2 E BASINIZ")
print("SIFRENIZIN SAYILARDAN VE HARFLERDEN OLUSMASINI ISTIYORSANIZ 3 E BASINIZ\n")
print("*"*80)
seviye=int(input("Seviyeyi giriniz:"))
uzunluk=int(input("Olusturmak istediginiz sifre uzunlugunu giriniz:"))
print(passwd_olusturma(seviye,uzunluk))
