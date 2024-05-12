def remove_comments(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            lines = infile.readlines()

        # Remove comments from each line
        cleaned_lines = []
        for line in lines:
            # Remove single-line comments
            if "#" in line:
                line = line.split("#", 1)[0]

            # Remove multi-line comments (if any)
            if '"""' in line:
                line = line.split('"""', 1)[0]

            cleaned_lines.append(line)

        # Write cleaned lines to the output file
        with open(output_file, "w") as outfile:
            outfile.writelines(cleaned_lines)

        print(f"Comments removed successfully. Output saved to {output_file}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

# Usage example
input_filename = "<yourfile.PY>"
output_filename = "<yourfileNoComments.PY>"
remove_comments(input_filename, output_filename)
