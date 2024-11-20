# Ch.7, Ex.1
# Saba Feilizadeh
# This program reads an error log file, counts non-empty lines, 
# finds lines with 'error', 'Error', or 'ERROR',
# and writes the results to a report file.

# Constant for the width of the line for the output
LINE_WIDTH = 30
# --------------------------------------------------------------------------
def main():

      # Get the file name from the user
      file_name = input('Enter the name of the file: ') # 'ErrorLog.txt'

      try:
            # Try to open the file
            with open(file_name, 'r') as infile:
                  lines = infile.readlines()

                  # Counters
                  linesCount = 0
                  errorLinesCount = 0
                  # List to store the lines with error
                  errorLinesList = []

                  # Read from the file
                  for line in lines:
                        stripped_line = line.strip()
                        if stripped_line:  # Count non-empty lines
                              linesCount += 1
                              # Check for 'error', 'Error', or 'ERROR'
                              if "error" in stripped_line.lower():
                                    errorLinesCount += 1
                                    errorLinesList.append(stripped_line)

                  # Write results to the report file
                  with open("reportError.txt", 'w') as outfile:
                        outfile.write(f"Total non-empty lines: {linesCount}\n")
                        outfile.write(f"Lines with 'error', 'Error', or 'ERROR': {errorLinesCount}\n")
                        outfile.write("Error lines:\n")
                        outfile.write("\n".join(errorLinesList))

                  # Print results
                  print("-" * LINE_WIDTH)
                  print(f"Total non-empty lines: {linesCount}")
                  print(f"Lines with 'error', 'Error', or 'ERROR': {errorLinesCount}")
                  print("-" * LINE_WIDTH)
                  print("Error lines:")
                  for line in errorLinesList:
                        print(line)
                  print("-" * LINE_WIDTH)

      except FileNotFoundError:
            print(f'Error! {file_name} doesn\'t exist!')

# --------------------------------------------------------------------------
main()
print("Done!")

# --------------------------------------------------------------------------
'''
=============================================================
Output 1:
=============================================================


=============================================================
Output 2:
=============================================================


'''
