# Write your code here
print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")
income_total = 202 + 118 + 2250 + 1680 + 1075 + 80
print(f'\nIncome: ${income_total}')

expense_staff = int(input('Staff expenses:'))
expense_other = int(input('Other expenses:'))

income_net = income_total - expense_staff - expense_other
print(f'Net income: ${income_net}')