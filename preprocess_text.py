
def preprocess_text(text):
  """Preprocess text.

  Args:
    text: The text to preprocess.

  Returns:
    The preprocessed text.
  """
  # Tokenize the text.
  tokens = text.split()

  # Remove stopwords.
  stopwords = set(stopwords.words('english'))
  tokens = [token for token in tokens if token not in stopwords]

  # Lemmatize the tokens.
  lemmatizer = nltk.WordNetLemmatizer()
  tokens = [lemmatizer.lemmatize(token) for token in tokens]

  # Return the preprocessed text.
  return ' '.join(tokens)

