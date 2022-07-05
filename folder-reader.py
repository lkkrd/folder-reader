import os
mainFolder = os.listdir("C:/Users/Admin/Opolska eSzkola/Szkolenia2020 - Dokumentacja szkoleń EKSPERT 2022")

for i in range (0, len(mainFolder) - 1):
    mainFolder[i] = mainFolder[i].upper()

nauczyciel = input('podaj imię nauczyciela: ').upper()
szkolenia = []
bledneSzkolenia = []


for i in mainFolder:
    if nauczyciel in i:
        szkolenia.append(i)


countSzkolenia = len(szkolenia)

for i in range (0, countSzkolenia - 1):
    path = "C:/Users/Admin/Opolska eSzkola/Szkolenia2020 - Dokumentacja szkoleń EKSPERT 2022/" + szkolenia[i]
    print(path)
    print(os.listdir(path))
    print(len(os.listdir(path)))

