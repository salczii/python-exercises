class InvalidConnectorError(Exception):
    def __str__(self):
        return "Number of connectors must be less than 10"


class InvalidFileSizeError(Exception):
    def __str__(self):
        return "File size is invalid!"


class InvalidFilePathError(Exception):
    def __str__(self):
        return "Provided path is invalid!"
