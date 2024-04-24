def write_multiple_lines(filename, lines):
  """
  Writes multiple lines of text to a file.

  Args:
    filename: The name of the file to write to.
    lines: A list of strings, where each string is a line of text to write.
  """

  with open(filename, 'w') as f:
    f.writelines(lines)

# Example usage
lines = [
  "Black is Beautiful. \n",
  "Be your own kind of beautiful.\n",
  "You are your own priority. \n",
]

write_multiple_lines("mylife.txt", lines)
