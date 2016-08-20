PaísA = int(input("Digite o número de habitantes do país A:"))
PaísB = int(input("Digite o número de habitantes do país B:"))
TaxaA = int(input("Digite a taxa de crescimento do país A:%"))
TaxaB = int(input("Digite a taxa de crescimento do país B:%"))
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
 
