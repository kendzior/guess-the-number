import random

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("\nSpróbuj ją odgadnąć w dziesięciu próbach.\n")

the_number = random.randint(1, 100)
guess = int(input("Ta liczba to: "))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Za duża...")
    else:
        print("Za mała...")

    guess = int(input("Ta liczba to: "))
    tries += 1
   
print("Odgadłeś! Ta liczba to", the_number)
print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!")

input("\n\nAby zakończyć program, naciśnij klawisz enter.")
