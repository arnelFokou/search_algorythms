#implementation of function dichotomie
import time


liste_sorted = [number for number in range(100_000_000)]
search_value = 1_000_000

start = time.perf_counter()
for element in liste_sorted:
    if element == search_value:
        print("value found")
        break
else:
    print("value not found")

end = time.perf_counter()
print("Execution time:", end - start)

