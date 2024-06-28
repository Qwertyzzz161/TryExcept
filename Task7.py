import logging
import random

loggername="Task7"

logger2 = logging.getLogger(loggername)
logger2.setLevel(logging.INFO)


handler2 = logging.FileHandler(f"{loggername}.log", mode='w')
formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler2.setFormatter(formatter2)
logger2.addHandler(handler2)


def task7():
    rand_list = []
    n = 10
    try:
        a = int(input("Введите значение a : "))
        b = int(input("Введите значение b : "))
        logger2.info(f"Нижнее значение = {a}, верхнее значение = {b}")
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    try:
        for i in range(n):
            rand_list.append(random.randint(a,b))
            if a < 0 and b > 100:
                logger2.info("Оба значения не вошли в интервал")
                raise ValueError("Неверный диапазон. Введите еще раз")
            elif a < 0:
                logger2.info("Нижнее значение не вошло в допустимый интервал.")
                raise ValueError("Неверный диапазон. Введите еще раз")
            elif b > 100:
                logger2.info("Верхнее значение не вошло в допустимый интервал.")
                raise ValueError("Неверный диапазон. Введите еще раз")
            elif a >= b:
                logger2.info("Нижнее значение не может быть больше или равняться верхнему.")
                raise ValueError("Неверный диапазон. Введите еще раз")
        print(rand_list)
    except Exception as e:
        logger2.error(f"Произошла ошибка: {e}", exc_info=True)



task7()
logging.shutdown()