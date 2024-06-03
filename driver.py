import os
import sys
import subprocess

# initialize history and password variables
history = []
current_password = ""

# start the logger process
log_file = sys.argv[1]
logger_process = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE)

# start the encryption program process
encryption_process = subprocess.Popen(["python3", "encrypt.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

def log_message(action, message):
    log_line = f"{action} {message}"
    log_line_bytes = log_line.encode("utf-8")
    logger_process.stdin.write(log_line_bytes + b'\n')
    logger_process.stdin.flush()

def print_menu():
    print()
    print("MENU:")
    print("1. password - set the pasword for encryption/decryption")
    print("2. encrypt - encrypt a string")
    print("3. decrypt - decrypt a string")
    print("4. history - show history")
    print("5. quit - quit program")

def main():
    log_message("START", "Driver program started.")

    while True:
        print_menu()
        command = input("Enter a command: ").strip()

        if command == "password":
            print("Choose an option:")
            print("1. Enter a new password")
            print("2. Select a password from history")

            option = input("Option: ")
            if option == "1":
                current_password = input("Enter a new password: ")
                log_message("PASSWORD", "New password set.")
                # send the new password to the encryption process
                encryption_process.stdin.write(f"PASSKEY {current_password}\n")
                encryption_process.stdin.flush()
                result = encryption_process.stdout.readline().strip()
                print(result)
            elif option == "2":
                if history:
                    print("Select a password from history:")
                    for i, entry in enumerate(history, 1):
                        print(f"{i}. {entry}")
                    selection = int(input("Enter the number of the password to use: "))
                    if 1 <= selection <= len(history):
                        current_password = history[selection - 1]
                        log_message("PASSWORD", "Password selected from history.")
                        # send the selected password to the encryption process
                        encryption_process.stdin.write(f"PASSKEY {current_password}\n")
                        encryption_process.stdin.flush()
                        result = encryption_process.stdout.readline().strip()
                        print(result)
                    else:
                        print("Invalid selection.")
                else:
                    print("No password history available.")


        elif command == "encrypt":
            print("Choose an option:")
            print("1. Enter a new string to encrypt")
            print("2. Select a string from history")

            option = input("Option: ")
            if option == "1":
                message = input("Enter a string to encrypt: ")
                history.append(message)
                log_message("ENCRYPT", f"Encrypting: {message}")
                encryption_process.stdin.write(f"ENCRYPT {message}\n")
                encryption_process.stdin.flush()
                result = encryption_process.stdout.readline().strip()
                print(result)
            elif option == "2":
                if history:
                    print("Select a string from history:")
                    for i, entry in enumerate(history, 1):
                        print(f"{i}. {entry}")
                    selection = int(input("Enter the number of the string to use: "))
                    if 1 <= selection <= len(history):
                        message = history[selection - 1]
                        log_message("ENCRYPT", f"Encrypting: {message}")
                        encryption_process.stdin.write(f"ENCRYPT {message}\n")
                        encryption_process.stdin.flush()
                        result = encryption_process.stdout.readline().strip()
                        print(result)
                    else:
                        print("Invalid selection.")
                else:
                    print("No history available.")

        elif command == "decrypt":
            print("Choose an option:")
            print("1. Enter a new string to decrypt")
            print("2. Select a string from history")

            option = input("Option: ")
            if option == "1":
                message = input("Enter a string to decrypt: ")
                history.append(message)
                log_message("DECRYPT", f"Decrypting: {message}")
                encryption_process.stdin.write(f"DECRYPT {message}\n")
                encryption_process.stdin.flush()
                result = encryption_process.stdout.readline().strip()
                print(result)
            elif option == "2":
                if history:
                    print("Select a string from history:")
                    for i, entry in enumerate(history, 1):
                        print(f"{i}. {entry}")
                    selection = int(input("Enter the number of the string to use: "))
                    if 1 <= selection <= len(history):
                        message = history[selection - 1]
                        log_message("DECRYPT", f"Decrypting: {message}")
                        encryption_process.stdin.write(f"DECRYPT {message}\n")
                        encryption_process.stdin.flush()
                        result = encryption_process.stdout.readline().strip()
                        print(result)
                    else:
                        print("Invalid selection.")
                else:
                    print("No history available.")

        elif command == "history":
            if history:
                print("History:")
                for i, entry in enumerate(history, 1):
                    print(f"{i}. {entry}")
                print("Enter '0' to exit history.")
                input()
            else:
                print("No history available.")

        elif command == "quit":
            log_message("QUIT", "Driver program quitting.")
            encryption_process.terminate()
            encryption_process.wait()
            logger_process.terminate()
            logger_process.wait()
            break
        else:
            print("Invalid command. Please enter a valid command from the menu.")

if __name__ == "__main__":
    main()

