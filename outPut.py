import os
import subprocess

class output():
    def save_and_print_txt(data, filename="output.txt"):
        try:
            # Write fetched data to a .txt file (overwrites existing content)
            with open(filename, "w") as file:
                for row in data:
                    line = " | ".join(str(item) for item in row)
                    file.write(line + "\n")
            
            # Print the file using the default printer
            output.print_txt_file(filename)
        except Exception as e:
            print(f"Error occurred: {e}")

    def print_txt_file(filename):
        try:
            if os.name == 'nt':  # Windows
                os.startfile(filename, "print")
            elif os.name == 'posix':  # macOS and Linux
                subprocess.run(['lp', filename])
            else:
                print(f"Cannot print the file on this OS: {os.name}")
        except Exception as e:
            print(f"Error printing file: {e}")

    # Example usage:
    """data = [
        (1, "John Doe", "1234567890"),
        (2, "Jane Smith", "0987654321"),
        # Add more rows as needed
    ]"""

