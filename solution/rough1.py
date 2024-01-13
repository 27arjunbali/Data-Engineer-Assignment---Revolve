import os
import argparse
import json
from typing import List, Dict

def load_jsonl_directory(directory_path: str) -> List[Dict]:
    """Load data from JSON Lines files in a directory."""
    data = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file == 'transactions.json':
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    # Assuming each file contains a list of transactions
                    transactions = json.load(json_file)
                    data.extend(transactions)

    return data

def main():
    # Get parameters from command line
    params = get_params()

    # Load data from input files using command line parameters
    customers_data = load_csv(params['customers_location'])
    transactions_data = load_jsonl_directory(params['transactions_location'])
    products_data = load_csv(params['products_location'])

    # Preprocess data
    preprocessed_data = preprocess_data(customers_data, transactions_data, products_data)

    # Generate output JSON
    output_json = generate_output_json(preprocessed_data)

    # Write output to the console
    write_output_to_console(output_json)

if __name__ == "__main__":
    main()
