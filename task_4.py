""" Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). """


def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


coordinate = input_numbers("Введите число: ")

if coordinate == 1:
  print ('Значения по координате Х больше нуля, по координате Y больше нуля')
elif coordinate == 2:
  print ('Значения по координате Х меньше нуля, по координате Y больше нуля')
elif coordinate == 3:
  print ('Значения по координате Х меньше нуля, по координате Y меньше нуля')
elif coordinate == 4:
  print ('Значения по координате Х больше нуля, по координате Y меньше нуля')
else:
  print ('Введено неверное значение четверти')