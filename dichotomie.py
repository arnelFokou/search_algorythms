#implementation of function dichotomie

liste_sorted = [1,2,3,4,5,6,7,8,9,10]

start,mid = 0,0
end = len(liste_sorted)
search_value = 12
while start != end :
    mid =(start + end )//2
    if liste_sorted[mid] == search_value:
        print("value found")
        break
    else:
        if liste_sorted[mid] < search_value:
            start =mid +1 
        else:
            end = mid -1
    print(mid)

if liste_sorted[mid] == search_value:
    print("le nombre a ete trouve")
else:
    print("le nombre n'a pas ete trouve")