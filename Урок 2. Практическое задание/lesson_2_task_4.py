

def get_result(count, sum, num, i):
    if i == count:        # нулевой случай
        return print(f'Сумма чисел ряда: {sum}')
    else:
        sum = sum + num   # суммируем
        num = num/-2      # следующее число в ряду по известной формуле
        i += 1            # изменение счетчика итераций для выхода в нулевом случае
        return get_result(count, sum, num, i)


cnt = int(input('Введите количество элементов ряда: '))
get_result(cnt, 0, 1, 0)  # вызов функции с количеством элементов ряда, объявленной нулевой суммой, началом ряда
                          # и счетчиком итераций