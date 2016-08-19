Nome = str(input("Digite um nome:"))
Idade = int(input("Digite uma idade:"))
Salário = eval(input("Digite um salário:"))
Sexo = str(input("Digite um sexo:"))
EstadoCivil = str(input("Digite um estado civil:"))

while (len(Nome)<= 3):
    print("Valor inválido")
    Nome = str(input("Digite um nome:"))

while (Idade < 0 and Idade > 150):
    print("Valor inválido")
    Idade = int(input("Digite uma idade:"))

while (Salário < 0):
    print("Valor inválido")
    Salário = eval(input("Digite um salário:"))

while (Sexo != "F" and Sexo != "M"):
     print("Valor inválido")
     Sexo = str(input("Digite um sexo:"))

while (EstadoCivil != "S" and EstadoCivil != "C" and EstadoCivil != "V" and EstadoCivil != "D"):
    print("Valor inválido")
    EstadoCivil = str(input("Digite um estado civil:"))
    
    
    
    
       
