"""Шаг 2. Переписываем на asyncio.

Задание 2а:
  1. Сделайте work корутиной (async def).
  2. Замените time.sleep на await asyncio.sleep.
  3. Сделайте main корутиной и вызовите в ней work через await в цикле.
  4. Запустите через asyncio.run.

Замерьте время. Изменилось ли оно по сравнению с шагом 1? Почему?

Задание 2б:
  Перепишите main так, чтобы все 10 задач ждали одновременно.
  Подсказка: asyncio.gather. Что изменилось в порядке вывода?
"""

import asyncio

from timer import print_time


async def work(n: int) -> None:
    print(f"start {n}")
    await asyncio.sleep(1)
    print(f"done {n}")


async def main() -> None:
    tasks = [work(i) for i in range(1, 11) ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    with print_time():
        asyncio.run(main())


# start 1
# start 2
# start 3
# start 4
# start 5
# start 6
# start 7
# start 8
# start 9
# start 10
# done 1
# done 2
# done 3
# done 4
# done 5
# done 6
# done 7
# done 8
# done 9
# done 10
# Time elapsed: 1.00s
