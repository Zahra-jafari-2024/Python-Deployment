import time
import random
import asyncio


async def marriage(name):
    random_year = random.randint(0,10)
    await asyncio.sleep(random_year)
    print(f"{name}: {random_year}")


async def main():
    await asyncio.gather(marriage("maryam"), marriage("mahsa"), marriage("javad"), marriage("shahryar"))
   

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    total_time = time.perf_counter() - start_time
    print(f"Total Time IS: {total_time}")