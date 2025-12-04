from lineaire import linear_search
from dichotomie import dichotomie_search

if __name__ == "__main__":
    liste_sorted = [number for number in range(100_000_001)]

    index_linear, time_linear = linear_search(liste_sorted, 1_000_000_000)
    print(f"Linear Search: Index = {index_linear if index_linear else "Not Found"}, Time = {time_linear:.10f} seconds")

    index_dichotomie, time_dichotomie = dichotomie_search(liste_sorted, 1_000_000_000)
    print(f"Dichotomie Search: Index = {index_dichotomie if index_dichotomie else "Not Found"}, Time = {time_dichotomie:.10f} seconds")