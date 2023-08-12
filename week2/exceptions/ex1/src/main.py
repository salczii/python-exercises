from file_handler.file_handler import FileHandler

from file_handler.exception import (
    InvalidConnectorError,
    InvalidFileSizeError,
    InvalidFilePathError,
)


def main():
    new_file_handler = None
    try:
        new_file_handler = FileHandler("/valid", 2, 7250)
    except InvalidConnectorError as e:
        print(e)
    except InvalidFileSizeError as e:
        print(e)
    except InvalidFilePathError as e:
        print(e)

    if new_file_handler is None:
        return
    try:
        new_file_handler.read_content()
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except IOError as e:
        print(f"IO error: {e}")
    except AttributeError as e:
        print(f"object wasn't assign properly to variable: {e}")
    else:
        print("everything all right. Your file was read")


if __name__ == "__main__":
    main()
