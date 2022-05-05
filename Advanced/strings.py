﻿"""
Дополнительные вещи для работы с вводом, выводом и строками.
Здесь будут рассматриваться функции print() и format()
"""

# Функция print() используется, что выводить какую-то информацию в консоль.

# Чтобы написать что-то между элементами, используется параметр sep - из-за него у нас будет не просто пробел между
# значениями, а конструкция "/-\".
# В конце строки вывода будут 3 знака - "!.?" - они там появились благодаря параметру end, который отвечает за описание
# конца строки и смещение курсора
# (если end не изменить, то из-за него курсор переместится на следующую строку, поэтому обычно несколько функций print()
# выписывают все в нескольких строках)
print("Какой-то текст", "Промежуточный текст", "Конец текста", sep="/-\\", end="!.?")
# Функция print() есть еще 2 параметра - file и flush. Они нужны для работы с файлами, но используются очень редко,
# так как помимо них есть аналогичная функция file.write()

# Иногда
