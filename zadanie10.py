n = int(input("Podaj liczbę całkowitą n (1 <= n <= 100): "))

if 1 <= n <= 100:
    suma = 0  
    
    
    for i in range(1, n + 1):
        if i % 2 == 0:  
            suma += i
    
 
    print("Suma liczb parzystych od 1 do", n, "wynosi:", suma)
else:
    print("Podana liczba nie mieści się w dozwolonym zakresie.")
