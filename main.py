'''
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! 
A program tartalmazza a függvény hívását is!
'''


def paros_e(*nums):
    lista =  [ num for num in nums ]
     
    for i in lista:
        vissza = True
        if i % 2 != 0:
            vissza = False
    return vissza
print(paros_e(1,3,5))

