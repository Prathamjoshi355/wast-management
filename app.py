from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/submit_request', methods=['POST'])
def submit_request():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    waste_type = request.form['waste_type']
    details = request.form['details']

    print("Name:", name)
    print("Email:", email)
    print("Address:", address)
    print("Waste Type:", waste_type)
    print("Details:", details)

    # Render the thank you page
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
