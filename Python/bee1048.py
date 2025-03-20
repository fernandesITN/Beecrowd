renda = float(input())

if renda > 0 and renda <= 400.00:
    ganho = renda * (0.15)
    total = renda + ganho
    print(f"Novo salario: {total:.2f}\nReajuste ganho: {ganho:.2f}\nEm percentual: 15 %")
elif renda >= 400.01 and renda <= 800.00:
    ganho1 = renda * (0.12)
    total1 = renda + ganho1
    print(f"Novo salario: {total1:.2f}\nReajuste ganho: {ganho1:.2f}\nEm percentual: 12 %")
elif renda >= 800.01 and renda <= 1200.00:
    ganho2 = renda * (0.10)
    total2 = renda + ganho2
    print(f"Novo salario: {total2:.2f}\nReajuste ganho: {ganho2:.2f}\nEm percentual: 10 %")
elif renda >= 1200.01 and renda <= 2000.00:
    ganho3 = renda * (0.07)
    total3 = renda + ganho3
    print(f"Novo salario: {total3:.2f}\nReajuste ganho: {ganho3:.2f}\nEm percentual: 7 %")
else:
    ganho4 = renda * (0.04)
    total4 = renda + ganho4
    print(f"Novo salario: {total4:.2f}\nReajuste ganho: {ganho4:.2f}\nEm percentual: 4 %")