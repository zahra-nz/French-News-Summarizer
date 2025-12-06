
from datasets import load_dataset

def load_french_news_dataset(split="train"):
# loading dataset MLSUM
dataset = load_dataset("mlsum", "fr", split=split)
return dataset

if **name** == "**main**":
data = load_french_news_dataset("train")
print("number:", len(data))
print("one:")
print(data[0])
