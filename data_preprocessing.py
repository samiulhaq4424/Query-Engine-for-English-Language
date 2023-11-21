import pandas as pd
import re

def preprocess_text(text):
    # Ensure text is a string
    text = str(text)
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and numbers
    text = re.sub(r'[\d\W]+', ' ', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    # Drop rows where the description is NaN
    data = data.dropna(subset=['description'])
    data['processed_description'] = data['description'].apply(preprocess_text)
    return data
