import math
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

allspend = 0

for month in range(0, months):
    allspend += spend * (1.05 ** month)

money_capital =  math.ceil(allspend - months * salary)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
