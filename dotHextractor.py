import os
#This will extract all (.h) files from a folder, and will give it out in a (.txt) file.
def find_header_files(directory):
    header_paths = set()  # Use a set to store unique parent paths
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".h"):
                header_paths.add(os.path.dirname(os.path.join(root, file)))  # Add parent path to set
    return header_paths

def write_to_txt(paths_set, output_file):
    with open(output_file, "w") as f:
        for path in paths_set:
            f.write(path + "\n")

# Specify the directory where you want to search for .h files
directory = "D:\git\MnM\AWC_BEV_APP"

# Call the function to find .h files in the specified directory
header_paths = find_header_files(directory)

# Specify the output file name
output_file = "header_paths.txt"

# Call the function to write the list of parent paths to a text file
write_to_txt(header_paths, output_file)

print("List of parent paths of header files written to", output_file)
