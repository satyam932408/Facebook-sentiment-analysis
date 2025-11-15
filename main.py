import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import string

# Sample text for NLP
text = """
Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and human (natural) languages. It enables computers to understand, interpret, and generate human language, making it a critical component of many applications, such as language translation, sentiment analysis, and chatbots.
"""

# Download necessary NLTK data files (only the first time)
nltk.download('punkt')

# Tokenize the text into words
words = word_tokenize(text.lower())

# Remove punctuation from the tokens
words = [word for word in words if word not in string.punctuation]

# Frequency distribution of words
fdist = FreqDist(words)

# Show the most common words
print("Most Common Words:")
print(fdist.most_common(10))

# Plot the frequency distribution
fdist.plot(30, cumulative=False)
