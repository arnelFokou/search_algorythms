#implementation of function dichotomie
import time


liste_sorted = [1,2,3,4,5,6,7,8,9,10]
search_value = 10

for element in liste_sorted:
    if element == search_value:
        print("value found")
        break
else:
    print("value not found")

