from dataclasses import dataclass


from .exception import (
    InvalidConnectorError,
    InvalidFileSizeError,
    InvalidFilePathError,
)


@dataclass
class FileHandler:
    _file_path: str
    _no_connectors: int
    _max_file_size: int

    def __post_init__(self):
        if self._no_connectors >= 10:
            raise InvalidConnectorError("Number of connectors must be less than 10")
        if self._max_file_size >= 10000 or self._max_file_size < 1000:
            raise InvalidFileSizeError(
                "Max file size must contain between 1000 and 9999"
            )
        if self._file_path == "":
            raise InvalidFilePathError("File path cannot be empty")

    @property
    def file_path(self):
        print("getter method called")
        return self._file_path

    @file_path.setter
    def file_path(self, path_name):
        print("setter method called")
        self._file_path = path_name

    @property
    def no_connectors(self):
        print("getter method called")
        return self._no_connectors

    @no_connectors.setter
    def no_connectors(self, no_connectors):
        print("setter method called")
        self._no_connectors = no_connectors

    @property
    def max_file_size(self):
        print("getter method called")
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        print("setter method called")
        self._max_file_size = max_file_size

    def read_content(self):
        print("content reading in progress", self)
        raise FileNotFoundError("File not found")

    def save_to_file(self):
        print("saving to file is processing", self)
        raise IOError("There was an error while saving the file")
