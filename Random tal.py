import random
guess = ""
a = random.randint(1, 100)
max_gissning = 10
antal_gissning = 0
print("Du har tio gissningar för att lista ut numret mellan 1 och 100, med higher/lower.")
while guess != a and antal_gissning<max_gissning:
    guess = int(input("Gissa på ett number:"))
    if a < guess:
        print("!LÄGRE!")
    elif guess < a:
        print("!HÖGRE!")
    antal_gissning+=1
    if antal_gissning > 9:
        print("Ajdå, du har slut på gissningar. You lost!!!")
    elif guess == a:
        print("Du hade rätt, talet var " + str(a))
# Lukas V