import asyncio
import time

import requests

# res = requests.get('http://127.0.0.1:8000/items?start=1&limit=2')
#
# print(res.status_code)
# print(res.headers)
# print(res.text)

# body = {
#     "name": "Item 4",
#     "description": "This is item 4",
#     "price": 15.5
# }
#
# res = requests.post(endpoint, json=body)
#
# print(res.status_code)
# print(res.headers)
# print(res.text)

async def sleep_time_func(sec):
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(
        None,
        requests.get,
        f'http://127.0.0.1:8000/sleep_time?sleep_time={sec}'
    )
    return res.text


async def main():
    print(f"main開始: {time.strftime('%X')}")
    result = await asyncio.gather(
        sleep_time_func(1),
        sleep_time_func(2),
    )
    print(result)
    print(f"main終了: {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())


