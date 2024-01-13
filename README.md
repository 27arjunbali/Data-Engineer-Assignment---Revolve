# Data-Engineer-Assignment---Revolve
# Project Title

Brief description of your project.

## Table of Contents

- [Getting Started](#getting-started)
- [Functions](#functions)
  - [get_params](#get_params)
  - [load_csv](#load_csv)
  - [load_jsonl_directory](#load_jsonl_directory)
  - [preprocess_data](#preprocess_data)
  - [calculate_loyalty_score](#calculate_loyalty_score)
  - [find_product_category](#find_product_category)
  - [generate_output_json](#generate_output_json)
  - [write_output_to_file](#write_output_to_file)
  - [main](#main)

## Getting Started

Brief instructions on how to get the project up and running.

## Functions

### get_params

**Description:** This function retrieves command-line parameters using argparse. It returns a dictionary containing the values of various input locations such as customers, products, transactions, and output.

### load_csv

**Description:** Loads data from a CSV file and returns a list of dictionaries where each dictionary represents a row in the CSV.

### load_jsonl_directory

**Description:** Loads data from JSON Lines files in a directory and returns a list of dictionaries.

### preprocess_data

**Description:** The preprocess_data function takes three inputs: customer data, transaction data, and product data. It processes this data to generate an output containing information for each customer. It calculates loyalty scores based on purchase counts and combines the relevant details, including customer ID, loyalty score, product ID, product category, and purchase count, into a structured format. The resulting output is a list of dictionaries representing the processed data for each customer. This function is a key step in preparing the data for downstream algorithms, making it more usable for analysis and insights.

### calculate_loyalty_score

**Description:** Calculates a loyalty score based on the given purchase count. It provides a simple loyalty score calculation example.

### find_product_category

**Description:** Finds the product category in the products_data based on the given product_id.

### generate_output_json

**Description:** Generates a JSON string from the preprocessed data.

### write_output_to_file

**Description:** Writes the generated JSON string to a specified output file.

### main

**Description:** The main function that orchestrates the entire process. It loads data, preprocesses it, generates output, and writes it to a file.
