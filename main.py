import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from calculate_word_frequency import calculate_word_frequency
from generate_histogram import generate_histogram
from preprocess_text import preprocess_text

if __name__ == '__main__':
  # Load the data.
  data = pd.read_csv('data.csv')

  # Preprocess the text.
  data['review_processed'] = data['review'].apply(preprocess_text)

  # Generate a histogram of the distribution of words in the review text.
  generate_histogram(data, 'review_processed')

  # Calculate the frequency of words in the review text.
  word_frequencies = calculate_word_frequency(data, 'review_processed')

  # Print the top 10 most frequent words.
  print(word_frequencies[:10])
