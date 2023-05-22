import asyncio
import aiohttp
import aiofiles
import torch
import io
import os 
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

class CLIPImageTextSimilarity:
    def __init__(self, model_name="openai/clip-vit-base-patch16"):
        self.model = CLIPModel.from_pretrained(model_name)
        self.processor = CLIPProcessor.from_pretrained(model_name)
    
    async def process_image_text_pair(self, texts, image_path):
        try:
            async with aiofiles.open(image_path, "rb") as file:
                image_content = await file.read()
                image = Image.open(io.BytesIO(image_content))
                inputs = self.processor(text=texts, images=image, return_tensors="pt", padding=True)
                outputs = self.model(**inputs)
                probs = outputs.logits_per_image.softmax(dim=1)
                probs = probs.detach().cpu().numpy().tolist()
                return probs
        except Exception as e:
            print(f"Error occurred during similarity calculation: {e}")
            return None

    async def get_similarity(self, texts_list, urls_list):
        tasks = []
        for texts, url in zip(texts_list, urls_list):
            similarity_task = asyncio.create_task(self.process_image_text_pair(texts, url))
            tasks.append(similarity_task)

        similarity_results = await asyncio.gather(*tasks)
        return similarity_results


    
if __name__ == "__main__":
    # Run the asyncio event loop
    # Example usage
    async def main():
        clip_similarity = CLIPImageTextSimilarity()
        urls = [
            "/root/code/data_process/data_process/modules/000000039769.jpg.jpg",
            "/root/code/data_process/data_process/modules/000000040036.jpg.jpg",
        ]
        texts = [
            ["a photo of a cat", "a photo of a dog"],
            ["a photo of a car", "a photo of a bicycle"],
        ]
        similarity_results = await clip_similarity.get_similarity(texts, urls)
        print(similarity_results)
        
    asyncio.run(main())
