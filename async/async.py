import asyncio
import time

async def func_1(sec):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, time.sleep, sec)
    return "完了func1"

async def func_2(sec):
    await asyncio.sleep(sec)
    return "完了func2"


async def main():
    print(f"開始: {time.strftime('%X')}")
    task1 = asyncio.create_task(func_1(1))
    task2 = asyncio.create_task(func_2(2))

    tasks = asyncio.all_tasks()
    for t in tasks:
        print(f"タスク: {t}")

    await task1
    await task2

    print(task1.result())
    print(task2.result())

    for t in tasks:
        print(f"完了タスク: {t}")
    print(f"終了: {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())
