import sys
from datetime import datetime

def log_message(log_file, action, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    log_line = f"{timestamp} [{action}] {message}\n"
    with open(log_file, "a") as file:
        file.write(log_line)

def main():
    if len(sys.argv) != 2:
        print("Usage: python logger.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    while True:
        user_input = input()
        if user_input == "QUIT":
            break

        # split the input into action and message
        parts = user_input.split(None, 1)
        if len(parts) == 2:
            action, message = parts
            log_message(log_file, action, message)
        else:
            print("Invalid log message format. Use 'ACTION MESSAGE'.")

if __name__ == "__main__":
    main()

