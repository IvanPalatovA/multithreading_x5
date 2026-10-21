"""Шаг 1. Синхронная программа.

Задание: реализуйте функцию work(n), которая
  1. печатает "start n"
  2. ждёт 1 секунду (time.sleep)
  3. печатает "done n"

и функцию main(), которая вызывает work для n от 1 до 10.
Запустите с замером времени. Сколько секунд заняла программа?
"""

import time

from timer import print_time


def work(n: int) -> None:
    print(f"start {n}")
    time.sleep(1)
    print(f"done {n}")


def main() -> None:
    for i in range(1, 11):
        work(i)


if __name__ == "__main__":
    with print_time():
        main()

# start 1
# done 1
# start 2
# done 2
# start 3
# done 3
# start 4
# done 4
# start 5
# done 5
# start 6
# done 6
# start 7
# done 7
# start 8
# done 8
# start 9
# done 9
# start 10
# done 10
# Time elapsed: 10.03s
