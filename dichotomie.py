#implementation of function dichotomie
import time

liste_sorted = [number for number in range(100_000_000)]

start,mid = 0,0
end = len(liste_sorted) -1
search_value = 100_000_000

start_time = time.perf_counter()
while start <= end :
    mid =(start + end )//2
    if liste_sorted[mid] == search_value:
        print("value found")
        break
    else:
        if liste_sorted[mid] < search_value:
            start = mid +1 
        else:
            end = mid - 1

if liste_sorted[mid] == search_value:
    print("le nombre a ete trouve")
else:
    print("le nombre n'a pas ete trouve")

end_time = time.perf_counter()
print("Execution time:", end_time - start_time)