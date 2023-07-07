var_1 = int(input('Введите первое число: '))
user_var_2 = int(input('Введите второе число: '))


def greetings():
  amount = int(input('Сколько раз вывести сфразу "Привет мир?"'))
  summ = var_1 + user_var_2
  if summ > 10:
    for var in range(amount):
      print('Hello world')
    


greetings()

