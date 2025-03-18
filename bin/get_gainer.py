""" Module auto-generated docstring """

import sys
from bin.gainers.factory import GainersFactory


def main():
    # Capture the source argument, default to 'yahoo' if not provided
    source = sys.argv[1] if len(sys.argv) > 1 else "yahoo"
    print(f"Source selected: {source}")

    try:
        # Initialize the GainersFactory with the chosen source
        factory = GainersFactory(source)
        # Fetch and process the data
        factory.fetch()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
