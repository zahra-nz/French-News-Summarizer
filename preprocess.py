#cleaning and pre-processing the code
import re

def clean_text(text):
# حذف فاصله‌های غیر ضروری
text = text.strip()

```
# removing spaces after eachother
text = re.sub(r"\s+", " ", text)

#removing:
text = re.sub(r"[^\w\s\.\,\!\?\-\']", " ", text)

return text
```

def preprocess_dataset(dataset):
# cleanup on the article and summary columns
articles = []
summaries = []

```
for item in dataset:
    article_clean = clean_text(item["text"])
    summary_clean = clean_text(item["summary"])
    articles.append(article_clean)
    summaries.append(summary_clean)

return articles, summaries
```

if **name** == "**main**":
# a quick test
from data_loader import load_french_news_dataset
ds = load_french_news_dataset("train").select(range(3))
arts, sums = preprocess_dataset(ds)
print("نمونه مقاله:", arts[0][:300])
print("summerisedه:", sums[0])
