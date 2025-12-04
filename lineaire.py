#implementation of function dichotomie
import time

def linear_search(liste_sorted, value):     
    search_value = value

    start_time = time.perf_counter()
    for index_element,element in enumerate(liste_sorted):
        if element == search_value:
            end_time = time.perf_counter()
            return (index_element,end_time - start_time)
    else:
        end_time = time.perf_counter()
        return (None,end_time - start_time)



