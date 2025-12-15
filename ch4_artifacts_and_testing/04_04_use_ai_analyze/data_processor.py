"""
A deliberately confusing class using metaclass magic that creates
hard-to-decipher stack traces for educational purposes.
"""


class MetaClass(type):
    """
    Metaclass that wraps methods to add automatic data extraction.
    """

    def __new__(mcs, name, bases, attrs):
        # Wrap any method that starts with 'get_'
        for attr_name, attr_value in list(attrs.items()):
            if attr_name.startswith("get_") and callable(attr_value):
                original = attr_value

                def wrapper(self, _original=original):
                    result = _original(self)
                    return result[0]["data"]["value"]

                attrs[attr_name] = wrapper

        return super().__new__(mcs, name, bases, attrs)


class DataProcessor(metaclass=MetaClass):
    """
    A data processor that uses metaclass magic for automatic data extraction.
    The metaclass automatically unwraps results from get_* methods.
    """

    def __init__(self, config=None):
        self.config = config or {}

    def get_user_info(self):
        """Returns user information in the expected nested format."""
        return [{"data": {"value": "John Doe"}}]

    def get_incomplete_data(self):
        """
        Returns data that doesn't match the metaclass expectations.
        """
        return [{"data": {}}]  # Missing 'value' key

    def get_empty_list(self):
        """
        Returns an empty list.
        """
        return []

    def get_malformed_structure(self):
        """
        Returns data with wrong structure.
        """
        return [{"wrong_key": "some_value"}]

    def process_safely(self, data_type="user"):
        """A method that doesn't get wrapped (doesn't start with 'get_')"""
        if data_type == "user":
            return self.get_user_info()
        return None
