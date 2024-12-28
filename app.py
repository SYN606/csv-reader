from flask import Flask, render_template, flash
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = os.urandom(24)


# Function to read CSV data into a DataFrame
def read_csv(file_name):
    if not os.path.exists(file_name):
        flash(f"Error: The file '{file_name}' does not exist.", 'error')
        return None
    return pd.read_csv(file_name)


# Route to display the CSV file in a web page
@app.route('/')
def index():
    filename = os.getenv('CSV_FILE',
                         'myfile.csv')  # Default to 'myfile.csv' if not set
    file_path = os.path.join(os.getcwd(), filename)

    if not os.path.exists(file_path):
        flash(f"The file '{filename}' does not exist.", 'error')
        return render_template('index.html', data=None, filename=filename)

    # Read the CSV file
    df = read_csv(file_path)

    if df is not None:
        return render_template(
            'index.html',
            data=df.to_html(classes='table table-bordered table-striped'),
            filename=filename)
    else:
        return render_template('index.html', data=None, filename=filename)


# New Route for '/help' to display the help page for CLI commands
@app.route('/help')
def help_page():
    return render_template('cmd.html')


if __name__ == "__main__":
    app.run(debug=True)
