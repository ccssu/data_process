import torch
from transformers import MarianMTModel, MarianTokenizer

class TranslationModule:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-en-zh"):
        self.model = MarianMTModel.from_pretrained(model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
    
    def translate(self, texts):
        inputs = self.tokenizer.prepare_seq2seq_batch(texts, return_tensors="pt")
        translated = self.model.generate(**inputs)
        translated_texts = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
        return translated_texts

# Example usage
translation_module = TranslationModule()
texts = ["Hello, how are you?", "What time is it?"]
translations = translation_module.translate(texts)
print(translations)
