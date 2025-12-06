
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer
from datasets import Dataset

from preprocess import preprocess_dataset
from data_loader import load_french_news_dataset

def prepare_data():
# loading dataset and cleaning
dataset = load_french_news_dataset("train").select(range(1000))
articles, summaries = preprocess_dataset(dataset)

```
data_dict = {
    "article": articles,
    "summary": summaries
}
return Dataset.from_dict(data_dict)
```

def tokenize_function(example, tokenizer, max_input=512, max_output=128):
# tokenization
model_inputs = tokenizer(example["article"], max_length=max_input, truncation=True)
with tokenizer.as_target_tokenizer():
labels = tokenizer(example["summary"], max_length=max_output, truncation=True)
model_inputs["labels"] = labels["input_ids"]
return model_inputs

def train_model():
# model
model_name = "google/mt5-small"

```
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#preparing data
dataset = prepare_data()
dataset_tokenized = dataset.map(
    lambda x: tokenize_function(x, tokenizer),
    batched=True
)

# training
training_args = TrainingArguments(
    output_dir="./models/abstractive",
    per_device_train_batch_size=2,
    num_train_epochs=1,
    learning_rate=2e-4,
    save_strategy="epoch",
    logging_steps=50
)

# making trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset_tokenized
)

# start of training
trainer.train()

# saving model
trainer.save_model("./models/abstractive")
```

if **name** == "**main**":
train_model()
