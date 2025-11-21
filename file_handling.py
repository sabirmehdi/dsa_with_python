def txt_to_binary(txt_path, bin_path):
    # Read text file
    with open(txt_path, 'r', encoding='utf-8') as f:
        text_data = f.read()
    
    # Convert text to bytes (UTF-8) and write to binary file
    with open(bin_path, 'wb') as f:
        f.write(text_data.encode('utf-8'))

    print(f"Text file '{txt_path}' successfully saved as binary '{bin_path}'.")


def binary_to_txt(bin_path, txt_path):
    # Read bytes from binary file
    with open(bin_path, 'rb') as f:
        binary_data = f.read()
    
    # Convert bytes back to text
    text_data = binary_data.decode('utf-8')

    # Write text back to a .txt file
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text_data)

    print(f"Binary file '{bin_path}' converted back to text '{txt_path}'.")


# Example usage:
if __name__ == "__main__":
    txt_to_binary("input.txt", "output.bin")
    binary_to_txt("output.bin", "restored.txt")
