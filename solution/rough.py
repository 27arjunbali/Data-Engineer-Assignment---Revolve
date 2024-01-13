# solution_start.py

import argparse
import json
from typing import List, Dict

def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="output_data/outputs/")
    return vars(parser.parse_args())

def load_csv(file_path: str) -> List[Dict]:
    """Load data from CSV file."""
    # Implementation to load data from CSV
    pass

def load_jsonl(file_path: str) -> List[Dict]:
    """Load data from JSON Lines file."""
    # Implementation to load data from JSON Lines
    pass

def preprocess_data(customers_data: List[Dict], transactions_data: List[Dict], products_data: List[Dict]) -> List[Dict]:
    """Preprocess data to generate the required output."""
    # Implementation for data preprocessing
    pass

def calculate_loyalty_score(purchase_count: int) -> int:
    """Calculate loyalty score based on purchase count."""
    # Implementation to calculate loyalty score
    pass

def generate_output_json(preprocessed_data: List[Dict]) -> str:
    """Generate output JSON string."""
    # Replace the following line with your actual implementation
    return json.dumps(preprocessed_data, indent=2)

def write_output_to_console(output_json: str) -> None:
    """Write output JSON to the console."""
    print(output_json)

import os

def load_jsonl_directory(directory_path: str) -> List[Dict]:
    """Load data from JSON Lines files in a directory."""
    data = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            print(file)
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

    print("Customers Data:", customers_data)
    print("Transactions Data:", transactions_data)
    print("Products Data:", products_data)

    # Rest of the code...


if __name__ == "__main__":
    main()
