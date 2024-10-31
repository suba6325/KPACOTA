money_capital = 20000 # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

budget = money_capital
months = 0

while budget >= 0:
    budget += salary
    if months > 0:
        spend *= 1.05
    budget -= spend
    months += 1

months -= 1 #количество месяцев, за которое еще хватало денег

print("Количество месяцев, которое можно протянуть без долгов:", months)
