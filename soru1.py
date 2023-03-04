import random
import time

randomList = [random.randint(1,10000) for i in range(10000)]

def linearSearch(liste):
    enBuyukSayi = liste[0]
    for i in range(len(liste)):
        if liste[i] > enBuyukSayi :
            enBuyukSayi = liste[i]
    
    return enBuyukSayi

start_time = time.time()
print("en büyük sayı :", linearSearch(randomList))
end_time = time.time()
print("linear searchten dönüştürdüğümüz fonksiyonun çalışma süresi : ", end_time - start_time)


def bruteForceSearch(liste):
    enBuyukSayi = 0
    for i in range(len(liste)):
        if liste[i] > enBuyukSayi :
            enBuyukSayi = liste[i]
    
    return enBuyukSayi
    

start_time2 = time.time()
print("en büyük sayı :", bruteForceSearch(randomList))
end_time2 = time.time()

print("bruteforce fonksiyonun çalışma süresi : ", end_time2 - start_time2)
