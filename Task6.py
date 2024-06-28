import logging
import math

loggername="Task6"

logger1 = logging.getLogger(loggername)
logger1.setLevel(logging.INFO)


handler1 = logging.FileHandler(f"{loggername}.log", mode='w')
formatter1 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler1.setFormatter(formatter1)
logger1.addHandler(handler1)


def task6():
    try:
        a = int(input("Введите значение a : "))
        b = int(input("Введите значение b : "))
        c = int(input("Введите значение c : "))
        logger1.info(f"Коэффициенты: a = {a}, b = {b}, c = {c}")
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    try:
        D= (b**2)-(4*a*c)
        if D < 0:
            logger1.info(f"Корней нет.")
            raise ValueError("Отрицательный дискриминант. Попробуйте другие коэффициенты")
        elif D == 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            logger1.info(f"Успешно. Корень уравнения: x = {x1}")
            return x1
        elif D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            logger1.info(f"Успешно. Корни уравнения: x1 = {x1}, x2 = {x2}")
            return x1, x2
    except Exception as e:
        logger1.error(f"Произошла ошибка: {e}", exc_info=True)

task6()
logging.shutdown()