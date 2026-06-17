# EXEMPLO - CÁLCULO DE IMPOSTO DE RENDA

sal = float(input("Digite seu salário: "))

if sal <= 1900:
    ir = 0
elif sal <=2800:
    ir = sal * 0.15
else:
        ir = sal * 0.275

sal_liq = sal - ir

print(f"IR: {ir:.2f}")
print(f"Salário Líquido: {sal_liq:.2f}")

# OUTRA FORMA DE FAZER, ALÉM DO ELIF (MAIS PRÁTICO)
# if sal <= 1900:
#    ir = 0
#else: -----------> NO LUGAR DO ELIF
#    if sal <=2800:
#        ir = sal * 0.15
#    else:
#        ir = sal * 0.275