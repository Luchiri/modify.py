def read_file(filename):
    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError:
        print(f"Error: The file {filename} could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the filename
filename = input("Enter the filename to read: ")

read_file(filename)
