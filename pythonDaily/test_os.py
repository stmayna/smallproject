import os

my_file_path = 'C:/Users/Mayna/datavizz/sample.pdf'

# Extracting the filename from the file path
file_name = os.path.basename(my_file_path)

print("File name:", file_name)