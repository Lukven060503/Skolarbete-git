svar = input("Vill du räkna: ")
while svar == "yes":
   type = input("Addition(+)(1)\nSubtraktion(-)(2)\nDivision(/)(3)\nMultiplikation(*)(4)\nUpphöjt(^)(5)\nRoten ur(√)(6)\nVilket räknesät ska räknas: ")
   if type == "3":
       type2 = input("Vanlig Division (1)\nDivision till närmaste heltal (2)\nDivision och tar med resten (3)\nVilken typ av division: ")
   if type == "1":
       addition1 = int(input("Skriv ett tal: "))
       addition2 = int(input("Vad ska " + str(addition1) + " adderas med: "))
       svar1 = addition1 + addition2
       print(str(addition1) + " + " + str(addition2) + " = " + str(svar1))
       svar = input("Vill du fortsätta: ")
   if type == "2":
       addition1 = int(input("Skriv ett tal: "))
       addition2 = int(input("Vad ska " + str(addition1) + " subtraheras med: "))
       svar1 = addition1 - addition2
       print(str(addition1) + " - " + str(addition2) + " = " + str(svar1))
       svar = input("Vill du fortsätta: ")
   if type == "3" and type2 == "1":
       addition1 = int(input("Skriv ett tal: "))
       addition2 = int(input("Vad ska " + str(addition1) + " delas med: "))
       svar1 = addition1 / addition2
       print(str(addition1) + " / " + str(addition2) + " = " + str(svar1))
       svar = input("Vill du fortsätta: ")
   if type == "3" and type2 == "2":
       addition1 = int(input("Skriv ett tal: "))
       addition2 = int(input("Vad ska " + str(addition1) + " delas med: "))
       svar1 = addition1 // addition2
       print(str(addition1) + " / " + str(addition2) + " = " + str(svar1))
       svar = input("Vill du fortsätta: ")
   if type == "3" and type2 == "3":
       addition1 = int(input("Skriv ett tal: "))
       addition2 = int(input("Vad ska " + str(addition1) + " delas med: "))
       svar1 = addition1 % addition2
       print(str(addition1) + " % " + str(addition2) + " = " + str(addition1 // addition2) + " och " + str(svar1) + " i rest")
       svar = input("Vill du fortsätta: ")
   if type == "4":
       addition1 = int(input("Skriv ett tal: "))
       addition2 = int(input("Vad ska " + str(addition1) + " multipliceras med: "))
       svar1 = addition1 * addition2
       print(str(addition1) + " * " + str(addition2) + " = " + str(svar1))
       svar = input("Vill du fortsätta: ")
   if type == "5":
       addition1 = int(input("Skriv ett tal: "))
       addition2 = int(input("Vad ska " + str(addition1) + " höjas upp med: "))
       svar1 = addition1**addition2
       print(str(addition1) + " ^ " + str(addition2) + " = " + str(svar1))
       svar = input("Vill du fortsätta: ")
   if type == "6":
       addition1 = int(input("Skriv ett tal: "))
       svar1 = addition1**0.5
       print(str(addition1) + " √ " + " = " + str(svar1))
       svar = input("Vill du fortsätta: ")
if svar == "no":
   print("Okej, ha en bra dag :)")
