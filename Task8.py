import logging
import math


loggername="Task8"

logger3 = logging.getLogger(loggername)
logger3.setLevel(logging.INFO)


handler3 = logging.FileHandler(f"{loggername}.log", mode='w')
formatter3 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler3.setFormatter(formatter3)
logger3.addHandler(handler3)


def task8():
    try:
        a = (input("Введите значение a : "))
        spis = a.split()
        logger3.info(f"Список: {spis}")
        if not isinstance(spis, list):
            logger3.info("Необходимо использовать список")
            raise TypeError("Неверный тип данных")
        for item in spis:
            if not item.isdigit():
                logger3.info("Необходимо вводить цифры")
                raise TypeError("Неверный тип данных")
        if len(spis) == 0:
            logger3.info("Необходимо заполнить список данными")
            raise ZeroDivisionError("Список пуст")
        spis = [int(elem) for elem in spis]
        avg = sum(spis) / len(spis)
        print(f"Среднее арифметическое суммы элементов списка = {avg}")
    except Exception as e:
        logger3.error(f"Произошла ошибка: {e}", exc_info=True)

task8()
logging.shutdown()