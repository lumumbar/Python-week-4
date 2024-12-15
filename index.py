def modify_file(input_file, output_file):
    """
    Reads the content of the input_file, modifies it, and writes the result to output_file.
    Parameters:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
    """
    try:
        # Open the input file and read its content
        with open(input_file, 'r') as infile:
            content = infile.read()
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        print(f"File has been modified and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError as e:
        print(f"I/O error occurred: {e}")
# Example usage
if __name__ == "__main__":
    while True:
        try:
            input_path = input("Enter the path to the input file: ")
            with open(input_path, 'r') as test_file:
                break  # File exists and can be read, exit loop
        except FileNotFoundError:
            print(f"Error: The file {input_path} does not exist. Please try again.")
        except IOError as e:
            print(f"Error: Cannot read the file {input_path}. {e}")
    output_path = input("Enter the path to save the modified file: ")
    modify_file(input_path, output_path)