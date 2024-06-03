def vigenere_cipher(text, key, mode):
    result = []
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')
            if char.isupper():
                if mode == 'ENCRYPT':
                    shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                elif mode == 'DECRYPT':
                    shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                if mode == 'ENCRYPT':
                    shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                elif mode == 'DECRYPT':
                    shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            result.append(shifted_char)
        else:
            result.append(char)

    return ''.join(result)

def main():
    password_set = False
    password = ""

    while True:
        user_input = input().split()
        command = user_input[0]

        if command == "ENCRYPT" or command == "DECRYPT":
            if not password_set:
                print("ERROR: Password not set")
            else:
                message = " ".join(user_input[1:])
                result = vigenere_cipher(message, password, command)
                print(f"RESULT {result}")
        elif command == "PASSKEY":
            password = user_input[1]
            password_set = True
            print("RESULT")
        elif command == "QUIT":
            break
        else:
            print("ERROR: Invalid command")

if __name__ == "__main__":
    main()

