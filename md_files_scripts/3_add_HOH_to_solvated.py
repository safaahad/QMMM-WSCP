# Define the file names
original_file_name = 'original_HOH.ndx'
destination_file_name = 'solvated.ndx'

# Read the content of the original file
with open(original_file_name, 'r') as original_file:
    lines = original_file.readlines()

# Find the start and end indices of the "HOH" section
start_index = lines.index('[ HOH ]\n')
end_index = lines.index('[', start_index + 1) if '[ ' in lines[start_index + 1] else len(lines)

# Extract the "HOH" section
hoh_section = lines[start_index:end_index]

# Open the destination file in append mode and write the "HOH" section
with open(destination_file_name, 'a') as destination_file:
    destination_file.writelines(hoh_section)

