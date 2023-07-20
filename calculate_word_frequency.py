def calculate_word_frequency(df, column):
  """Calculate the frequency of words in a column.

  Args:
    df: The DataFrame containing the data.
    column: The column to calculate the frequency for.

  Returns:
    A list of tuples of (word, frequency).
  """
  # Get the values in the column.
  values = df[column].values

  # Calculate the frequency of each word.
  frequencies = np.unique(values, return_counts=True)[1]

  # Return a list of tuples of (word, frequency).
  return zip(frequencies.index, frequencies)
