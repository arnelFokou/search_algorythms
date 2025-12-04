#implementation of function dichotomie
import time

def dichotomie_search(liste_sorted,value):
    start,mid = 0,0
    end = len(liste_sorted) -1
    search_value = value

    start_time = time.perf_counter()
    while start <= end :
        mid =(start + end )//2
        if liste_sorted[mid] == search_value:
            break
        else:
            if liste_sorted[mid] < search_value:
                start = mid + 1 
            else:
                end = mid - 1
    end_time = time.perf_counter()

    if liste_sorted[mid] == search_value:
        return (mid,end_time - start_time)
    else:
        return (None,end_time - start_time)

