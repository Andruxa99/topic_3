working_hours: int = int(input("Введите кол-во отработанных часов в месяц: "))

hourly_rate: int = 176

salary: int = hourly_rate * working_hours

print("Ваша почасовая ставка:", hourly_rate)
print("Заработная плата в месяц:", salary)
