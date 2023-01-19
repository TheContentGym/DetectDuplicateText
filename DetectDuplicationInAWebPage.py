from bs4 import BeautifulSoup
import requests
import re
from nltk.tokenize import sent_tokenize
from collections import Counter

import nltk
nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'[^\w\s]','',text) # Remove punctuation
    text = text.lower() # Convert to lowercase
    return text

url = "https://thecontentgym.wordpress.com/2022/05/09/a-non-engineer-attending-a-marathon-5-full-days-python-training-with-experienced-programmers/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()

#Tokenize text into sentences
sentences = sent_tokenize(text)

# Clean the text and create a Counter for each sentence
sentence_counter = Counter(map(clean_text, sentences))

# Find duplicate sentences
duplicate_sentences = [sent for sent, count in sentence_counter.items() if count > 1]

print("Duplicate sentences:", duplicate_sentences)
