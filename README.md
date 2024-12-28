CSV CRUD Operations with Flask and CLI
======================================

This project provides a command-line interface (CLI) and a web interface for performing CRUD (Create, Read, Update, Delete) operations on CSV files. It utilizes **Python**, **Flask**, and **Pandas** for handling CSV file data and rendering it in a web browser.

### Table of Contents

*   [Project Overview](#project-overview)
*   [Technologies Used](#technologies-used)
*   [Setup Instructions](#setup-instructions)
*   [Commands](#commands)
*   [Dependencies](#dependencies)
*   [Contributing](#contributing)
*   [License](#license)

Project Overview
----------------

This project provides a simple interface to manage CSV files. It allows users to:

*   Create a new CSV file with predefined columns.
*   Add, update, or delete rows in the CSV file.
*   View the contents of the CSV file in a terminal or in a web browser via a Flask web interface.

You can interact with the CSV file either via the command line or through a web interface for easy visualization of the data.

Technologies Used
-----------------

*   **Python**: The primary programming language for the project.
*   **Flask**: A lightweight web framework used to render CSV data in a browser.
*   **Pandas**: Used for reading, writing, and manipulating CSV data.
*   **argparse**: Handles command-line arguments for CRUD operations.
*   **JS and Bootstrap**: Beautifying the web interface.

Setup Instructions
------------------

### 1\. Clone the Repository

Start by cloning the repository to your local machine:

git clone https://github.com/yourusername/csv-crud-flask-cli.git

Then navigate to the project directory:

cd csv-crud-flask-cli

### 2\. Create a Virtual Environment (optional but recommended)

It’s recommended to use a virtual environment to isolate project dependencies.

python3 -m venv venv

Activate the virtual environment:

On Linux/Mac:

source venv/bin/activate

On Windows:

venv\\Scripts\\activate

### 3\. Install Dependencies

Install the required Python packages listed in `requirements.txt`:

pip install -r requirements.txt

Alternatively, you can manually install Flask and Pandas:

`pip install Flask pandas`


Commands
--------

For a detailed breakdown of each command and its usage, please refer to the [COMMANDS](COMMANDS) file.

Dependencies
------------

The following dependencies are required to run this project:

*   **Flask**: Web framework for rendering CSV data in the browser.
*   **Pandas**: Library for reading, writing, and manipulating CSV data.
*   **argparse**: Used to handle the command-line interface and parsing commands.

To install the dependencies, you can run:

pip install -r requirements.txt

Contributing
------------

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Clone your fork to your local machine.
3.  Create a new branch (`git checkout -b feature-branch`).
4.  Make your changes.
5.  Commit your changes (`git commit -m "Add new feature"`).
6.  Push to your fork (`git push origin feature-branch`).
7.  Open a pull request to the main repository.

Please ensure your code follows the style guidelines, and write tests where applicable.

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Created by SYN 606
