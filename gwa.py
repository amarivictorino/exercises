def find_highest_gwa(filename):
  """
  This function reads a file containing student names and GWAs,
  and returns a dictionary with the name and GWA of the student
  with the highest GWA.
  """
  highest_gwa_student = {"name": None, "gwa": 0.0}

  try:
    with open(filename, "r") as file:
      for line in file:
        name, gwa_str = line.strip().split()
        gwa = float(gwa_str)

        if gwa > highest_gwa_student["gwa"]:
          highest_gwa_student["name"] = name
          highest_gwa_student["gwa"] = gwa
          
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

  return highest_gwa_student

if __name__ == "__main__":
  filename = "C:/Users/GIGABYTE/Desktop/PYTHON PROJECTS/exercises/student_gwas.txt"

  highest_gwa_student = find_highest_gwa(filename)

  if highest_gwa_student["name"]:
    print(f"Student with the highest GWA: {highest_gwa_student['name']} ({highest_gwa_student['gwa']:.2f})")
  else:
    print("No student data found in the file.")


