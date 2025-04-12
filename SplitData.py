import os
import shutil
import random
from tqdm import tqdm

def split_dataset(source_dir, target_dir, split_ratio=0.8):
    class_names = os.listdir(source_dir)
    
    for class_name in class_names:
        class_path = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_path):
            continue
        
        # Get image file list
        images = [f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        random.shuffle(images)
        
        split_point = int(len(images) * split_ratio)
        train_images = images[:split_point]
        test_images = images[split_point:]
        
        # Paths for train and test folders
        train_class_dir = os.path.join(target_dir, 'train', class_name)
        test_class_dir = os.path.join(target_dir, 'test', class_name)
        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(test_class_dir, exist_ok=True)
        
        # Copy files
        for img_name in tqdm(train_images, desc=f"Copying {class_name} - Train"):
            src = os.path.join(class_path, img_name)
            dst = os.path.join(train_class_dir, img_name)
            shutil.copy2(src, dst)
        
        for img_name in tqdm(test_images, desc=f"Copying {class_name} - Test"):
            src = os.path.join(class_path, img_name)
            dst = os.path.join(test_class_dir, img_name)
            shutil.copy2(src, dst)

# Example usage
source_directory = "FIELD IMAGES"
target_directory = "Field Data"
split_dataset(source_directory, target_directory, split_ratio=0.8)
