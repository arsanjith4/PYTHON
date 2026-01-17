input_file = "input.txt"
output_file = "output.txt"

infile = open(input_file, "r")
content = infile.read()
infile.close()

outfile = open(output_file, "w")
outfile.write(content)
outfile.close()

print("Content copied successfully")
