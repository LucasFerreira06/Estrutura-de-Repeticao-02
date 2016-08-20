PaísA = 80000
PaísB = 200000
Anos = 0

while (PaísA < PaísB):
    print("Pop. do País A:", PaísA,"e Pop. do País B:", PaísB,"em", Anos,"anos")
    PaísA = PaísA + PaísA * 0.03
    PaísB = PaísB + PaísB * 0.015
    Anos = Anos + 1
    continue
    if (PaisA >= PaisB):
        break
            
print("País A:",PaísA)
print("Pais B:",PaísB)     
print("Foram necessários",Anos,"anos para que a população do país A ultrapasse ou igualasse a população do país B")
 
