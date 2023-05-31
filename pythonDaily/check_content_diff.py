import filecmp
import difflib

file1 = "/home/mayns/smallproject/pythonDaily/xml_a.xml"
file2 = "/home/mayns/smallproject/pythonDaily/xml_b.xml"

# Read the contents of the files
with open(file1, 'r') as f1, open(file2, 'r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# Use difflib to compare the lines and print the differences
differ = difflib.Differ()
diff = differ.compare(lines1, lines2)
diff_lines = [line for line in diff if line.startswith(
    '-') or line.startswith('+')]

if not diff_lines:
    print("The files are identical.")
else:
    print("The files are different. Here are the differing lines:")
    for line in diff_lines:
        print(line.strip())
