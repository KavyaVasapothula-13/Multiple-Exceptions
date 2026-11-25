# Define the filename to work with
filename = "demo_file.txt"

# 1. Write Mode - 'w'
print("1. Mode: 'w' (write mode)")
with open(filename, 'w') as f:
    f.write("This is write mode.\n")
print("-> Written to file (overwrites if exists)\n")

# 2. Read Mode - 'r'
print("2. Mode: 'r' (read mode)")
try:
    with open(filename, 'r') as f:
        content = f.read()
    print("-> File Content Read:\n", content)
except FileNotFoundError:
    print("-> File not found (must exist before using 'r')\n")

# 3. Append Mode - 'a'
print("3. Mode: 'a' (append mode)")
with open(filename, 'a') as f:
    f.write("Appended line.\n")
print("-> Appended to file without deleting old content\n")

# 4. Read and Write Mode - 'r+'
print("4. Mode: 'r+' (read and write)")
with open(filename, 'r+') as f:
    data = f.read()
    print("-> Original content:\n", data)
    f.seek(0)
    f.write("Modified using r+ mode.\n")
print("-> Modified beginning of the file\n")

# 5. Write and Read Mode - 'w+'
print("5. Mode: 'w+' (write and read)")
with open(filename, 'w+') as f:
    f.write("New content in w+ mode.\n")
    f.seek(0)
    print("-> Content after writing:\n", f.read())
print("-> Overwrites the file and allows reading\n")

# 6. Append and Read Mode - 'a+'
print("6. Mode: 'a+' (append and read)")
with open(filename, 'a+') as f:
    f.write("Appended using a+ mode.\n")
    f.seek(0)
    print("-> All file content:\n", f.read())
print("-> Adds data and reads all content\n")
