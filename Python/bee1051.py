renda = float(input())

if renda >= 0.00 and renda <= 2000.00:
    print("Isento")
elif renda >= 2000.01 and renda <= 3000.00:
    imposto = (renda - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")
elif renda >= 3000.01 and renda <= 4500.00:
    calc = 1000 * 0.08
    imposto1 = (renda - 3000.00) * 0.18
    total1 = imposto1 + calc
    print(f"R$ {total1:.2f}")
else:
    calc1 = 1000 * 0.08 + 1500 * 0.18
    imposto2 = (renda - 4500.00) * 0.28
    total2 = imposto2 + calc1
    print(f"R$ {total2:.2f}")