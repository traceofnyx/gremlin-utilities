# Mini Script Session: Binary to ASCII DECODER
# What it does:
# Accepts user input
# Decodes or encodes in perfect 8-bit fashion
# Logs every input/output


from datetime import datetime

def log_result(input_data, output_data, mode):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] MODE: {mode} | INPUT: {input_data} | OUTPUT: {output_data}\n"

    with open("log.txt", "a") as file:
        file.write(log_entry)


def binary_to_text(binary_string):
    binary_values = binary_string.split()

    # Check all values are 8 bits
    for b in binary_values:
        if len(b) != 8 or not set(b).issubset({'0', '1'}):
            return "Invalid Input: Each chunk must be 8 bits of 0s and 1s only."

    characters = [chr(int(b, 2)) for b in binary_values]
    return ''.join(characters)


def text_to_binary(text_string):
    text_chars = [char for char in text_string]

    #changing characters into binary
    binary_coded = [bin(ord(char))[2:].zfill(8) for char in text_chars]
    return ' '.join(binary_coded)


def main():
    while True:
        which_mode = input("Text or Binary? T/B ").upper()

        if which_mode == 'T':
            user_input = input("Tell me your message: ")
            result = text_to_binary(user_input)
            print("Binary text:", result)
            log_result(user_input, result, "Text-to-Binary")

        elif which_mode.upper() == 'B':
            user_input = input("Tell me your binary message: ")
            result = binary_to_text(user_input)
            print("Decoded text:", result)

        if_continue = input("Do you want to put a new message? Y/n ").lower()
        if if_continue == 'n':
            print('Goodbye')
            break



if __name__ == "__main__":
    main()

# Example usage
# binary_input = "01000010 01110010 01100101 01100001 01110100 01101000 00101100 00100000 01000010 01100001 01100010 01111001"
# sample_text = 'Love you, James'