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
Enter the name of the file: ErrorLog.txt
------------------------------
Total non-empty lines: 108
Lines with 'error', 'Error', or 'ERROR': 5
------------------------------
Error lines:
[Sun Mar  7 21:16:17 2018] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome
[Mon Mar  8 07:27:36 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/_vti_bin/owssvr.dll
[Mon Mar  8 07:27:37 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/MSOffice/cltreq.asp
[Thu Mar 11 02:27:34 2018] [error] [client 200.174.151.3] File does not exist: /usr/local/mailman/archives/public/cipg/2018-november.txt
[Thu Mar 11 07:39:29 2018] [error] [client 140.113.179.131] File does not exist: /usr/local/apache/htdocs/M83A
------------------------------
Done!

=============================================================
Output:
=============================================================
Enter the name of the file: output.txt
Error! output.txt doesn't exist!
Done!

'''
