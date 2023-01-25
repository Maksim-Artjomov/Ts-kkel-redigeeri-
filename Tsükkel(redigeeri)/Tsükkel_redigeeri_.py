from re import T
import time

print("Ülesanne 0-1")

i=(int)
while i!=72:
    print("please enter 72: ")
    i=(int(input("Sisestage täisarv => ")))
    if i == 72: print("Aitäh")

print("Ülesanne 0-2") 
time.sleep(1)
print("Palun oodake numbrit 100")
for i in range (60,101):
    print (i)
    print("please wait for 72 ")
    if i == 100: print("Aitäh")
    time.sleep(1)


#=====================================================================================================
print("Ülesanne 23")  

for i in range(1,20):
    vanus=int(input(f"Õpilase number {i}, sisestage oma vanus: "))

    if vanus >= 18:
        print("See on täiskasvanu inimene")
    else:
        print("See on alaealine inimene")