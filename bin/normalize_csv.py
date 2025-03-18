import csv
import os
import sys
import logging


def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )


def normalize_csv(input_file):
    """
    Reads a stock market CSV file from sample_data/ and transforms it into a standardized format.
    Saves the normalized CSV in sample_data/ with _norm appended.

    Args:
        input_file (str): Path to the raw CSV file.

    Returns:
        str: Path to the normalized CSV file.
    """
    assert isinstance(input_file, str), (
        f"Expected string for file path, got {type(input_file)}"
    )
    assert os.path.exists(input_file), f"File not found: {input_file}"

    output_file = input_file.replace(".csv", "_norm.csv")
    expected_headers = ["symbol", "price",
                        "price_change", "price_percent_change"]
    normalized_data = []

    logging.info(f"Processing file: {input_file}")

    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        headers = reader.fieldnames

        if headers is None:
            raise ValueError("Invalid CSV file: No headers found.")

        for row in reader:
            normalized_row = {
                "symbol": row.get("Symbol") or row.get("symbol"),
                "price": row.get("Last") or row.get("price"),
                "price_change": row.get("Change") or row.get("price_change"),
                "price_percent_change": row.get("% Change") or row.get("price_percent_change"),
            }

            assert all(normalized_row.values()), (
                f"Missing values in row: {normalized_row}"
            )
            normalized_data.append(normalized_row)

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=expected_headers)
        writer.writeheader()
        writer.writerows(normalized_data)

    logging.info(f"Normalized file saved: {output_file}")
    return output_file


def main():
    setup_logging()

    if len(sys.argv) != 2:
        logging.error(
            "Usage: python bin/normalize_csv.py sample_data/<csv_filename>")
        sys.exit(1)

    input_path = sys.argv[1]
    normalize_csv(input_path)


if __name__ == "__main__":
    main()
