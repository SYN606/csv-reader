import os
import pandas as pd


# Function to read CSV data into a DataFrame
def read_csv(file_name):
    if not os.path.exists(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return None
    return pd.read_csv(file_name)


# Function to write DataFrame to CSV
def write_csv(df, file_name):
    df.to_csv(file_name, index=False)
    print(f"Data successfully written to '{file_name}'.")


# Function to update a row in CSV
def update_row(file_name, index, new_data):
    df = read_csv(file_name)
    if df is not None and index < len(df):
        df.loc[index] = new_data
        write_csv(df, file_name)
        print(f"Row {index} updated successfully.")
    else:
        print("Invalid index or error reading file.")


# Function to delete a row in CSV
def delete_row(file_name, index):
    df = read_csv(file_name)
    if df is not None and index < len(df):
        df.drop(index, inplace=True)
        write_csv(df, file_name)
        print(f"Row {index} deleted successfully.")
    else:
        print("Invalid index or error reading file.")


# Function to add a new row to CSV
def add_row(file_name, data):
    # If the file doesn't exist, create it with the headers
    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist. Creating new file...")
        df = pd.DataFrame(columns=["name", "age", "salary", "department"])
        write_csv(df, file_name)  # Create file with column headers

    # Read the existing CSV file
    df = read_csv(file_name)
    if df is not None:
        # Add the row to the DataFrame
        df = df.append(data, ignore_index=True)
        write_csv(df, file_name)
        print(f"New row added to '{file_name}'.")
