import random
import time

randomList = [random.randint(1,10000) for i in range(10000)]
print("sıralanmamış liste : ", randomList)
def merge_sort(liste, sol, orta, sag):
    #sol ve sağdaki dizilern boyutlarını n1 ve n2 değişkenlerinde tutuyoruz
    n1 = orta - sol + 1
    n2 = sag - orta
    
    #burada da sol ve sağ dizileri oluşturuyoruz ve alt dizileri birlştiriyoruz
    sol_dizi = [liste[sol + i] for i in range(n1)]
    sag_dizi = [liste[orta + 1 + i] for i in range(n2)]
    i, j, k = 0, 0, sol
    
    while i < n1 and j < n2:
        if sol_dizi[i] <= sag_dizi[j]:
            liste[k] = sol_dizi[i]
            i += 1
        else:
            liste[k] = sag_dizi[j]
            j += 1
        k += 1
        
    #kalan elemanları ekliyoruz
    while i < n1:
        liste[k] = sol_dizi[i]
        i += 1
        k += 1
        
    while j < n2:
        liste[k] = sag_dizi[j]
        j += 1
        k += 1
        
def merge_sort_yardimci(liste, sol, sag): 
    ### bu fonksiyon  
    ### bir alt dizi tek elemanlı hale gelene kadar kendini 
    ### çağıran özyinelemeli bir işlem gerçekleştirir.
    if sol < sag:
        orta = (sol + sag) // 2
        
        merge_sort_yardimci(liste, sol, orta)
        merge_sort_yardimci(liste, orta+1, sag)
        
        merge_sort(liste, sol, orta, sag)


  
def merge_sort_cagir(liste): ##merge sort çağırıyoruz, bundan ötürü süre ölçümünü burada yaapcağız
    merge_sort_yardimci(liste, 0, len(liste)-1)
    return liste

start_time = time.time()
print("sıralı liste", merge_sort_cagir(randomList))
end_time = time.time()


def selection_sort(liste):#brute force algoritmalardan selectionu tercih ediyoruz
    n = len(liste)
    for i in range(n):
        en_kucuk_index = i
        for j in range(i + 1, n):
            if liste[en_kucuk_index] > liste[j]:
                en_kucuk_index = j
        liste[i], liste[en_kucuk_index] = liste[en_kucuk_index], liste[i]
    return liste

start_time2 = time.time()
print("sıralı liste", selection_sort(randomList))
end_time2 = time.time()

print("mergesort çalışma zamanı : ", end_time - start_time)
print("selection sort - bruteforce çalışma zamanı : ", end_time2 - start_time2)