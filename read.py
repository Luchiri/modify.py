def modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File has been modified and saved as {output_filename}.")

    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading or writing the file: {e}")

# Ask the user for the input and output file names
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the file to write the modified content: ")

modify_file(input_filename, output_filename)
