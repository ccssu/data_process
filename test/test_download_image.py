import asyncio
import sys
sys.path.append('../data_process')

from modules.download_image import download_images

URLS = [
    "https://cdn.pixabay.com/photo/2016/03/23/12/53/clock-1274699_960_720.jpg",
    "https://cdn.pixabay.com/photo/2014/12/04/15/21/tea-556777_960_720.jpg",
    "https://cdn.pixabay.com/photo/2023/04/11/10/44/chai-7916889_960_720.jpg"
]
downloaded_files = asyncio.run(download_images(URLS))
print("Downloaded files:", downloaded_files)