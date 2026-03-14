import re

input_file = input("enter input file name: ")
output_file = input("enter output file name: ")

f = open(input_file, "r")
lines = f.readlines()
f.close()

out = open(output_file, "w")

for line in lines:
    mail = re.search("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}", line)

    if mail:
        temp = line.replace(mail.group(), "")
        name = re.sub("[^a-zA-Z ]", "", temp).strip()

        if name == "":
            name = "unknown"

        out.write(name + " -> " + mail.group() + "\n")

out.close()

print("✅ emails extracted and stored successfully")
