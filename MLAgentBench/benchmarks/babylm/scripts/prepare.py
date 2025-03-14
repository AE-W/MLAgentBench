import subprocess
import os
from datasets import load_dataset

taskname = "babylm"
download_dir = "../env/babylm_data"


os.makedirs(download_dir, exist_ok=True)


print("Downloading BabyLM dataset from Hugging Face...")
dataset = load_dataset("cambridge-climb/BabyLM", "strict_small", cache_dir=download_dir)


train_data = dataset["train"]
valid_data = dataset["validation"]


train_path = os.path.join(download_dir, "train.txt")
valid_path = os.path.join(download_dir, "valid.txt")

print(f"Saving training data to {train_path}...")
with open(train_path, "w") as f:
    for line in train_data["text"]:
        f.write(line + "\n")

print(f"Saving validation data to {valid_path}...")
with open(valid_path, "w") as f:
    for line in valid_data["text"]:
        f.write(line + "\n")

print("Dataset download and processing complete.")
