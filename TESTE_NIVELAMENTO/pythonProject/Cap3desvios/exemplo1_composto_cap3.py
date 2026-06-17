tc = int(input("Digite seu tempo de casa: "))
sal = float(input("Digite seu salário: "))

if tc < 3:
    aumt = sal * 0.05
else:
    aumt = sal * 0.1

nsal = sal + aumt

print(f"Seu salário foi de {sal:.2f} para {nsal:.2f}")