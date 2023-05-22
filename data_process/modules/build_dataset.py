import os
import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data = self.load_data()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        # Process the item as needed
        # ...

        return item

    def load_data(self):
        data = []
        # Load data from the data directory
        # You can customize this part based on your data format and structure

        # Example: Load image and label pairs from image files and a separate label file
        image_files = os.listdir(os.path.join(self.data_dir, 'images'))
        label_file = os.path.join(self.data_dir, 'labels.txt')
        
        with open(label_file, 'r') as f:
            labels = f.read().splitlines()

        for image_file, label in zip(image_files, labels):
            image_path = os.path.join(self.data_dir, 'images', image_file)
            data.append((image_path, label))

        return data
