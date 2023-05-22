import asyncio
import time
import aiohttp
import aiofiles

async def download_image(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                image_name = url.split("/")[-1] + ".jpg"
                content = await response.content.read()
                async with aiofiles.open(image_name, "wb") as f:
                    await f.write(content)
        return image_name  # 返回下载的图像文件名
    except Exception as e:
        print(f"Download failed for {url}: {str(e)}")
        return None  # 返回None表示下载失败


async def download_images(urls):
    start_time = time.time()
    tasks = [download_image(url) for url in urls]
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total time: {end_time - start_time}s")
    return results  # 返回下载结果列表

if __name__ == "__main__":
    URLS = [
        "https://cdn.pixabay.com/photo/2016/03/23/12/53/clock-1274699_960_720.jpg",
        "https://cdn.pixabay.com/photo/2014/12/04/15/21/tea-556777_960_720.jpg",
        "https://cdn.pixabay.com/photo/2023/04/11/10/44/chai-7916889_960_720.jpg"
    ]
    downloaded_files = asyncio.run(download_images(URLS))
    print("Downloaded files:", downloaded_files)
