import asyncio
import time
import aiohttp
import aiofiles
from concurrent.futures import ThreadPoolExecutor

import requests

URLS = [
    "https://cdn.pixabay.com/photo/2016/03/23/12/53/clock-1274699_960_720.jpg",
    "https://cdn.pixabay.com/photo/2014/12/04/15/21/tea-556777_960_720.jpg",
    "https://cdn.pixabay.com/photo/2023/04/11/10/44/chai-7916889_960_720.jpg"
]

proxy_url = "http://127.0.0.1"
proxies = {"http": proxy_url, "https": proxy_url}

start_time = time.time()


async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image_name = url.split("/")[-1] + ".jpg"
            content = await response.content.read()
            async with aiofiles.open(image_name, "wb") as f:
                await f.write(content)
    print(f"Downloaded {image_name}")

async def main():
    task =[asyncio.create_task(download_image(url)) for url in URLS]
    await asyncio.wait(task,timeout=10)

asyncio.run(main())
end_time = time.time()
print(f"Total time: {end_time - start_time}s")