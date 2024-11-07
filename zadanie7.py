import random


pogoda = random.choice([0, 1])


while True:
    odpowiedz = input("Czy pada deszcz? (tak/nie): ").strip().lower()
    
 
    if odpowiedz == "tak" and pogoda == 1:
        print("Brawo! Zgadłeś poprawnie!")
        break
    elif odpowiedz == "nie" and pogoda == 0:
        print("Brawo! Zgadłeś poprawnie!")
        break
    else:
        print("Niestety, spróbuj ponownie!")
