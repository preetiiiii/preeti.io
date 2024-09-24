from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Your HTML file

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Define the CSV file path
    csv_file_path = 'contacts.csv'

    # Save data to CSV
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, message])

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
