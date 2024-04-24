def process_file(source_file, even_file, odd_file):
  """
  This function reads an integer text file, separates even and odd numbers,
  and writes their squares and cubes to separate files.

  Args:
  source_file: The name of the source text file containing integers.
  even_file: The name of the output file for even numbers (squares).
  odd_file: The name of the output file for odd numbers (cubes).
  """
  with open(source_file, 'r') as infile, open(even_file, 'w') as even, open(odd_file, 'w') as odd:
    for line in infile:
      number = int(line.strip())
      if number % 2 == 0:
        even.write(str(number**2) + '\n')
      else:
        odd.write(str(number**3) + '\n')

source_file = "integers.txt"
even_file = "double.txt"
odd_file = "triple.txt"

# Call the function to process the file
process_file(source_file, even_file, odd_file)

print(f"Successfully processed {source_file} and created {even_file} and {odd_file}.")
