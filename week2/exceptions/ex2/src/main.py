from file_handler.file_handler import FileHandler

from file_handler.exceptions import (
    InvalidConnectorError,
    InvalidFileSizeError,
    InvalidFilePathError,
)


def main():

    new_file_handler = None
    try:
        new_file_handler = FileHandler("/not_empty", 5, 1001)
    except InvalidConnectorError:
        print("Invalid number of connectors provided.")
    except InvalidFileSizeError:
        print("Invalid file size provided.")
    except InvalidFilePathError:
        print("Invalid file path provided.")

    try:
        new_file_handler.read_content()
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except IOError as e:
        print(f"IO error: {e}")
    else:
        print("everything all right. Your file was read")


if __name__ == "__main__":
    main()
