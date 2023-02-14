kitoblar = {}

belgi = True

while belgi:
    
    kitob = input(f"Kitob nomi: ")
    muallif = input(f"Muallif ismi:  ")
    
    kitoblar[muallif] = kitob  # lug'atga element qo'shish
    
    javob = input("yana kitob qo'shamizmi? (ha/y, yo'q/n  ") 
    
    if javob == "n":
        belgi = False
