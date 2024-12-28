  CSV CRUD Flask CLI - Available Commands 

Available Commands
==================

### Create Command

**The `create` command allows you to create a new CSV file with predefined columns.**

**Usage:**

    python main.py create <file_name.csv>

**Arguments:**

*   `<file_name.csv>`: The name of the CSV file to be created. The file will be created with the columns: `name`, `age`, `salary`, and `department`.

**Example:**

    python main.py create myfile.csv

This will create a new CSV file named `myfile.csv` with the columns `name`, `age`, `salary`, and `department`.

### Read Command

**The `read` command is used to read and display the contents of the CSV file in the terminal.**

**Usage:**

    python main.py read <file_name.csv>

**Arguments:**

*   `<file_name.csv>`: The name of the CSV file to read and display.

**Example:**

    python main.py read myfile.csv

This will print the contents of `myfile.csv` to the terminal.

### Add Command

**The `add` command allows you to add a new row to the CSV file.**

**Usage:**

    python main.py add <file_name.csv> --data "<name>,<age>,<salary>,<department>"

**Arguments:**

*   `<file_name.csv>`: The name of the CSV file to add the row to.
*   `--data`: A comma-separated string representing the new row's values. You need to provide data for all columns: `name`, `age`, `salary`, and `department`.

**Example:**

    python main.py add myfile.csv --data "John,30,60000,HR"

This will add a new row with the data `John, 30, 60000, HR` to `myfile.csv`.

### Update Command

**The `update` command allows you to update an existing row in the CSV file at a specific index.**

**Usage:**

    python main.py update <file_name.csv> --index <index> --data "<name>,<age>,<salary>,<department>"

**Arguments:**

*   `<file_name.csv>`: The name of the CSV file to update.
*   `--index`: The index of the row to update (zero-based).
*   `--data`: A comma-separated string representing the new values for the row.

**Example:**

    python main.py update myfile.csv --index 1 --data "Jane,32,65000,Finance"

This will update the row at index `1` in `myfile.csv` with the new data `Jane, 32, 65000, Finance`.

### Delete Command

**The `delete` command allows you to delete a row from the CSV file at a specific index.**

**Usage:**

    python main.py delete <file_name.csv> --index <index>

**Arguments:**

*   `<file_name.csv>`: The name of the CSV file to delete the row from.
*   `--index`: The index of the row to delete (zero-based).

**Example:**

    python main.py delete myfile.csv --index 1

This will delete the row at index `1` in `myfile.csv`.

### Web Command

**The `--web` flag allows you to launch the web interface to view the CSV data in a browser.**

**Usage:**

    python main.py read <file_name.csv> --web

**Arguments:**

*   `<file_name.csv>`: The name of the CSV file to display.
*   `--web`: The flag to start the Flask web server and render the CSV file in a web browser.

**Example:**

    python main.py read myfile.csv --web

This will start the Flask web server and display the contents of `myfile.csv` in a tabular format in a web browser.