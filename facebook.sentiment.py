import nltk 
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# Download NLTK data (run once)
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt_tab')

# Load comments
with open('kindle.txt', encoding='ISO-8859-2') as f:
    text = f.read()

# Preprocessing (optional printing)
sentences = sent_tokenize(text)
words = word_tokenize(text)
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Sentiment analysis
sid = SentimentIntensityAnalyzer()
compound_scores = []
comments = []

for line in text.split('\n'):
    line = line.strip()
    if not line:
        continue
    scores = sid.polarity_scores(line)
    comments.append(line)
    compound_scores.append(scores['compound'])

    # Print scores
    print(f"\nComment: {line}")
    for k, v in scores.items():
        print(f"{k}: {v}")

# 1️⃣ Bar chart
plt.figure(figsize=(10, 6))
colors = ['green' if s > 0 else 'red' if s < 0 else 'gray' for s in compound_scores]
plt.barh(comments, compound_scores, color=colors)
plt.xlabel("Compound Sentiment Score")
plt.title("Sentiment Analysis of Facebook Comments")
plt.tight_layout()
plt.show()

# 2️⃣ Pie chart summary
pos = sum(1 for s in compound_scores if s > 0)
neu = sum(1 for s in compound_scores if s == 0)
neg = sum(1 for s in compound_scores if s < 0)
plt.figure(figsize=(6, 6))
plt.pie([pos, neu, neg], labels=['Positive','Neutral','Negative'], autopct='%1.1f%%', startangle=90)
plt.title("Overall Sentiment Distribution")
plt.tight_layout()
plt.show()

# 3️⃣ Save results
df = pd.DataFrame({
    'Comment': comments,
    'Compound Score': compound_scores
})
df['Sentiment'] = df['Compound Score'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)
df.to_excel('sentiment_results.xlsx', index=False)
print("✅ Results saved to sentiment_results.xlsx")
