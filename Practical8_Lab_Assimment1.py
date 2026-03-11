def copy_to_uppercase(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        uppercase_content = content.upper()
        with open(output_file, 'w') as outfile:
            outfile.write(uppercase_content)
        print(f"Contents of '{input_file}' have been written to '{output_file}' in uppercase.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_to_uppercase("input.txt", "output.txt")
