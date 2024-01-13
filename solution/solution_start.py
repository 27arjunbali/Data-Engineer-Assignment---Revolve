# solution_start.py

import argparse
import csv
import json
import os
from typing import List, Dict

# Function to get command-line parameters
def get_params() -> dict:
    """Get command-line parameters."""
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="./input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="./input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="./input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    return vars(parser.parse_args())

# Function to load data from CSV file
def load_csv(file_path: str) -> List[Dict]:
    """Load data from CSV file."""
    data = []

    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
    except Exception as e:
        print(f"Error loading CSV file {file_path}: {e}")

    return data

# Function to load data from JSON Lines files in a directory
def load_jsonl_directory(directory_path: str) -> List[Dict]:
    """Load data from JSON Lines files in a directory."""
    data = []

    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file == 'transactions.json':
                    file_path = os.path.join(root, file)
                    print(f"Loading data from: {file_path}")
                    with open(file_path, 'r') as json_file:
                        for line in json_file:
                            try:
                                transaction = json.loads(line)
                                data.append(transaction)
                            except json.JSONDecodeError as e:
                                print(f"Error decoding JSON in {file_path}: {e}")
    except Exception as e:
        print(f"Error loading JSON files in directory {directory_path}: {e}")

    return data

# Function to preprocess data and generate the required output
def preprocess_data(customers_data: List[Dict], transactions_data: List[Dict], products_data: List[Dict]) -> List[Dict]:
    """Preprocess data to generate the required output."""
    processed_data = []

    try:
        # Example logic: Group transactions by customer_id
        transactions_by_customer = {}
        for transaction in transactions_data:
            customer_id = transaction.get('customer_id')
            if customer_id:
                if customer_id not in transactions_by_customer:
                    transactions_by_customer[customer_id] = []
                transactions_by_customer[customer_id].append(transaction)

        # Example logic: Calculate purchase_count for each customer
        purchase_count_by_customer = {customer_id: len(transactions) for customer_id, transactions in transactions_by_customer.items()}

        # Example logic: Calculate loyalty_score based on purchase_count
        loyalty_score_by_customer = {customer_id: calculate_loyalty_score(purchase_count) for customer_id, purchase_count in purchase_count_by_customer.items()}

        # Example logic: Combine all information into the final output format
        for customer in customers_data:
            customer_id = customer.get('customer_id')
            loyalty_score = loyalty_score_by_customer.get(customer_id, 0)

            # Example logic: Assuming products_data has information about each product's category
            for transaction in transactions_by_customer.get(customer_id, []):
                product_basket = transaction.get('basket', [])

                # Example logic: Create a record for each product in the basket
                for index, product_info in enumerate(product_basket, start=1):
                    product_id = product_info.get('product_id')
                    price = product_info.get('price')

                    # Find product information in products_data
                    product_category = find_product_category(products_data, product_id)

                    # Example logic: Create a record for each product purchased by the customer
                    processed_data.append({
                        'customer_id': customer_id,
                        'loyalty_score': loyalty_score,
                        f'product_id_{index}': product_id,
                        f'product_category_{index}': product_category,
                        f'price_{index}': price,
                        'purchase_count': purchase_count_by_customer.get(customer_id, 0),
                    })
    except Exception as e:
        print(f"Error during data preprocessing: {e}")

    return processed_data

# Function to calculate loyalty score based on purchase count
def calculate_loyalty_score(purchase_count: int) -> int:
    """Calculate loyalty score based on purchase count."""
    # Your implementation to calculate loyalty score (you can replace this with your own logic)
    return min(purchase_count // 2, 10)

# Function to find product category in products_data
def find_product_category(products_data: List[Dict], product_id: str) -> str:
    """Find product category in products_data."""
    try:
        product_info = next((product for product in products_data if product.get('product_id') == product_id), {})
        return product_info.get('product_category', 'Unknown')
    except Exception as e:
        print(f"Error finding product category for product_id {product_id}: {e}")
        return 'Unknown'

# Function to generate output JSON string
def generate_output_json(preprocessed_data: List[Dict]) -> str:
    """Generate output JSON string."""
    return json.dumps(preprocessed_data)

# Function to write output to a file
def write_output_to_file(output_json: str, output_file_path: str) -> None:
    """Write output JSON to a file."""
    try:
        with open(output_file_path, 'w') as output_file:
            output_file.write(output_json)
    except Exception as e:
        print(f"Error writing output to file {output_file_path}: {e}")

# Main function
def main():
    try:
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

        # Write output to a file using command line parameter
        output_file_path = os.path.join(params['output_location'], 'output.json')
        write_output_to_file(output_json, output_file_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
