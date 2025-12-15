"""
Main application demonstrating the DataProcessor with metaclass.
This will trigger confusing errors for educational purposes.
"""

import sys

from data_processor import DataProcessor


def main():
    """Main function that exercises the DataProcessor."""
    processor = DataProcessor(config={"debug": True})

    print("Testing DataProcessor with metaclass magic...\n")

    # This works fine
    print("1. Testing get_user_info:")
    try:
        user = processor.get_user_info()
        print(f"   ✓ Success: {user}\n")
    except Exception as e:
        print(f"   ✗ Error: {e}\n")

    # This will cause a confusing KeyError
    print("2. Testing get_incomplete_data:")
    try:
        data = processor.get_incomplete_data()
        print(f"   ✓ Success: {data}\n")
    except Exception as e:
        print(f"   ✗ Error: {e}\n")
        import traceback

        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
