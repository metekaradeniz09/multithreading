import multiprocessing
import math


def toplama(a, b):
    sonuc = a + b
    print(f"Toplama: {a} + {b} = {sonuc}")


def cikarma(a, b):
    sonuc = a - b
    print(f"Çıkarma: {a} - {b} = {sonuc}")


def carpma(a, b):
    sonuc = a * b
    print(f"Çarpma: {a} * {b} = {sonuc}")


def bolme(a, b):
    if b != 0:
        sonuc = a / b
        print(f"Bölme: {a} / {b} = {sonuc}")
    else:
        print("Bölme: Sıfıra bölme hatası")




def hesapla():

    a = float ( input("a: "))
    b = float ( input("b: "))

    # Süreçleri (processes) oluşturma
    process1 = multiprocessing.Process(target=toplama, args=(a, b))
    process2 = multiprocessing.Process(target=cikarma, args=(a, b))
    process3 = multiprocessing.Process(target=carpma, args=(a, b))
    process4 = multiprocessing.Process(target=bolme, args=(a, b))
    #başlatma
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    #bitmesini bekleme
    process1.join()
    process2.join()
    process3.join()
    process4.join()


    print("Tüm hesaplamalar tamamlandı.")


if __name__ == "__main__":
    hesapla()
