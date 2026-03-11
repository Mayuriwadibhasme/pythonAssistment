def remove_comments_and_copy(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            lines = src.readlines()

        filtered_lines = []
        for line in lines:
            stripped = line.strip()
            # Skip full-line comments and empty lines
            if stripped.startswith("#") or stripped == "":
                continue
            # Remove inline comments if present
            if "#" in line:
                line = line.split("#", 1)[0].rstrip()
            filtered_lines.append(line + "\n")

        with open(destination_file, 'w') as dest:
            dest.writelines(filtered_lines)

        print("\n--- Source File Content ---")
        with open(source_file, 'r') as src:
            print(src.read())

        print("\n--- Destination File Content (without comments) ---")
        with open(destination_file, 'r') as dest:
            print(dest.read())

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")



src_file = input("Enter the source Python file name: ")
dest_file = input("Enter the destination file name: ")

remove_comments_and_copy(src_file, dest_file)
