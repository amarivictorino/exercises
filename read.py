def seperate_even_odd(filename):
  """
  Reads an integer text file, separates even and odd numbers,
  and writes them to separate files.

  Args:
      filename: The name of the text file containing integers.
  """

  with open(filename, 'r') as infile:
    numbers = [int(line.strip()) for line in infile]

  even_numbers = [num for num in numbers if num % 2 == 0]
  odd_numbers = [num for num in numbers if num % 2 !=0]

  with open('even.txt', 'w') as even_file:
    even_file.writelines([str(num) + '\n' for num in even_numbers])

  with open('odd.txt', 'w') as odd_file:
    odd_file.writelines([str(num) + '\n' for num in odd_numbers])

# Call the function with the actual filename
seperate_even_odd('numbers.txt')  

print("Even and odd numbers separated successfully!")

