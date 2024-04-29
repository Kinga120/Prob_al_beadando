#<-------------------------------------------->
# Alap mátrix(sodoku) megadása
# Validálás
megoldandoMatrix= [[0,0,6,0,0,4],
                   [0,2,0,6,0,0],
                   [0,4,0,0,0,5],
                   [2,0,0,0,6,0],
                   [0,0,4,0,5,0],
                   [5,0,0,3,0,0]]

def valid(matrix, sor, oszlop, szam):
    #Sor
    for i in range(len(matrix)):
        if matrix[sor][i] == szam:
            return False
    #Oszlop
    for i in range(len(matrix)):
        if matrix[i][oszlop] == szam:
            return False

    # Átló ellenőrzése
    if sor == oszlop:
        for i in range(len(matrix)):
            if matrix[i][i] == szam:
                return False

    if sor + oszlop == len(matrix) - 1:
        for i in range(len(matrix)):
            if matrix[i][len(matrix) - 1 - i] == szam:
                return False

    # 3x2-es méretű blokk ellenörzése, mivel nem csak a sor és oszlopban szerepelhet 6 különböző szám
    start_sor, start_oszlop = 2 * (sor // 2), 3 * (oszlop // 3)
    for i in range(start_sor, start_sor + 2):
        for j in range(start_oszlop, start_oszlop + 3):
            if matrix[i][j] == szam:
                return False

    return True
#<-------------------------------------------->
# Rekurzió, vizsgálat, megoldás


#<-------------------------------------------->
#Eredmény kiiratás
# Függvények meghívása
