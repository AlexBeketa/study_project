var_1 = int(input('Введите первое число: '))
user_var_2 = int(input('Введите второе число: '))
user_var_3 = int(input(' и это будет противоречить другой ветке'))

summ = var_1 + user_var_2

def greetings():
  print('Hello world')

greetings()
print(f'Сумма введенных чисел равна: {summ}')
