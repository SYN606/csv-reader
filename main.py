import argparse
import os
import sys
import pandas as pd
from app import app  # Importing Flask app from app.py
from reader import add_row, update_row, delete_row, read_csv, write_csv


def main():
    parser = argparse.ArgumentParser(description="CSV CRUD Operations")

    parser.add_argument(
        'action',
        choices=['read', 'create', 'update', 'delete', 'add', 'help'],
        help="Action to perform or display help")
    parser.add_argument('file_name', help="CSV file name",
                        nargs='?')  # Optional for help
    parser.add_argument('--index',
                        type=int,
                        help="Index of the row to update/delete")
    parser.add_argument(
        '--data',
        type=str,
        help="Data for the new or updated row, comma-separated")
    parser.add_argument('--web',
                        action='store_true',
                        help="Launch web interface")

    args = parser.parse_args()

    # If --web flag is passed, handle it
    if args.web:
        if args.action == 'help':
            print("Starting web server to display the help page...")

            # Explicitly set the Flask environment and server name for /help
            app.config[
                "SERVER_NAME"] = "localhost:5000"  # Default localhost:5000
            with app.app_context():
                os.environ["FLASK_RUN_FROM_CLI"] = "false"
                print(
                    "Navigate to http://localhost:5000/help to see the help page."
                )
                app.run(debug=True)
            return
        else:
            print(f"Starting web server to display '{args.file_name}'...")
            if not os.path.exists(args.file_name):
                print(f"Error: The file '{args.file_name}' does not exist.")
                sys.exit(1)
            os.environ[
                "CSV_FILE"] = args.file_name  # Pass the CSV file to Flask
            app.run(debug=True)
            return

    # Handle CLI-based actions
    if args.action == 'read':
        df = read_csv(args.file_name)
        if df is not None:
            print(df)

    elif args.action == 'create':
        # Create the CSV file with the header if it doesn't exist
        write_csv(
            pd.DataFrame(columns=["name", "age", "salary", "department"]),
            args.file_name)

    elif args.action == 'add':
        # Add a new row to the CSV
        if args.data:
            data = args.data.split(',')
            if len(data) == 4:
                add_row(
                    args.file_name, {
                        "name": data[0],
                        "age": int(data[1]),
                        "salary": float(data[2]),
                        "department": data[3]
                    })
            else:
                print(
                    "Error: Invalid data format. Ensure you provide 4 values (name, age, salary, department)."
                )
        else:
            print("Error: Data argument is required for adding a new row.")

    elif args.action == 'update':
        # Update an existing row
        if args.index is not None and args.data:
            data = args.data.split(',')
            if len(data) == 4:
                update_row(
                    args.file_name, args.index, {
                        "name": data[0],
                        "age": int(data[1]),
                        "salary": float(data[2]),
                        "department": data[3]
                    })
            else:
                print(
                    "Error: Invalid data format. Ensure you provide 4 values (name, age, salary, department)."
                )
        else:
            print("Error: Index and data are required for updating.")

    elif args.action == 'delete':
        if args.index is not None:
            delete_row(args.file_name, args.index)
        else:
            print("Error: Index is required for deleting a row.")

    elif args.action == 'help':
        print("Use the following commands to interact with the application:")
        print(" - read <file_name>: Read the contents of the CSV file.")
        print(" - create <file_name>: Create a new CSV file.")
        print(
            " - add <file_name> --data 'name,age,salary,department': Add a new row."
        )
        print(
            " - update <file_name> --index <index> --data 'name,age,salary,department': Update an existing row."
        )
        print(" - delete <file_name> --index <index>: Delete a row.")
        print(" - help: Display this help message.")
        print(" - --web: Launch the web interface for the given action.")


if __name__ == "__main__":
    main()
