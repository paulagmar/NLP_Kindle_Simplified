def generate_histogram(df, column):
  """Generate histogram of the distribution of words in a column.

  Args:
    df: The DataFrame containing the data.
    column: The column to generate the histogram for.

  Returns:
    The histogram.
  """
  # Get the values in the column.
  values = df[column].values

  # Plot the histogram.
  plt.hist(values)
  plt.title('Distribution of Words in Column {}'.format(column))
  plt.xlabel('Word')
  plt.ylabel('Frequency')
  plt.show()

