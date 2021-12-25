import asyncio
from timeit import default_timer as timer
import aiohttp
import sys

if (
    sys.version_info[0] == 3
    and sys.version_info[1] >= 8
    and sys.platform.startswith("win")
):
    """
    Put this only for Windows, where you get "RuntimeError: Event loop is closed".

    """
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def get_data(s):
    """
    Important Notes:
    1. A function defined with is async/await called a coroutine.
    2. Coroutines are only preferred for long-running I/O bound tasks.
    3. Coroutines are single threaded, which means they can not not give any performance benefits over CPU bound tasks.
    4. This 'get_data()' coroutine gets data from Google's homepage concurrently.
    5. This is I/O bound task because it is waiting for the server to get the homepage data.
    6. While one task is waiting, coroutines allow other tasks to run. That's what coroutines are made for.

    """

    async with s.get("https://www.google.com") as resp:
        text = await resp.text()


async def main():
    async with aiohttp.ClientSession() as s:
        await asyncio.gather(*(get_data(s) for _ in range(100)))


if __name__ == "__main__":
    t = timer()
    asyncio.run(main())
    print(timer() - t)

    # Output: 0.8510 seconds(approx. 8510 milliseconds, depending on the response time of the server)
