money = float (input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
list_per_cent = list(per_cent.values())
deposit = [round(list_per_cent[0]/100*money), round(list_per_cent[1]/100*money), round(list_per_cent[2]/100*money), round(list_per_cent[3]/100*money)]
print("deposit=", deposit)
print("Максимальная сумма, которую вы можете заработать -", max(deposit))


