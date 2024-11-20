# flask app where users can add, view, and delete contacts

from flask import Flask, render_template, request

app = Flask(__name__)

contacts = []

@app.route("/")
def home():
    return render_template("homepage.html")




####################################################################################
"""
Contact Book Routes:
"""
####################################################################################
#contact book homepage
@app.route("/contact/home")
def contact_home():
    return render_template("home_contact.html")

@app.route("/contact/show")
def show_contacts():
    return render_template("show_contacts.html", contacts = contacts)

@app.route("/contact/add", methods=["GET", "POST"])
def add_contact():

    # if statement occurs when form submission is hit
    if request.method =="POST":
        # Handle form submission
        name = request.form.get("contact-name")
        number = request.form.get("contact-number")

        # Handle missing input
        if not name or not number:
            return render_template("add_contact.html", error = "Please fill out both fields.")

        contacts.append([name, number])
        return render_template("home_contact.html")
    
    return render_template("add_contact.html")

@app.route("/contact/delete", methods=["GET", "POST"])
def delete_contact():

    if request.method == "POST":
        contact_number_input = request.form.get("contact-number")
        if not contact_number_input.isdigit():
            return render_template("delete_contact.html", contacts=contacts, error="Enter a number bucko")

        contact_number = int(contact_number_input)

        # Checks if contacts list is empty - if empty prompt user no contact to delete
        if not contacts:
            return render_template("delete_contact.html", contacts=contacts, error="No contacts you silly goose.")
    
        # Check if contact_number is within range - if contact number is not within range return page until user enters appropriate number
        if contact_number < 1 or contact_number > len(contacts):
            return render_template("delete_contact.html", contacts=contacts, error="Add a contact first!!")

        contacts.pop(contact_number-1)

    return render_template("delete_contact.html", contacts = contacts)

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
