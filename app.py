# flask app where users can add, view, and delete contacts

from flask import Flask, render_template, request

app = Flask(__name__)

contacts = []

@app.route("/")
def home():
    return render_template("/home.html")




@app.route("/show_contacts")
def showContacts():
    return render_template("/show_contacts.html", contacts = contacts)




@app.route("/add_contact")
def add_contact():
    return render_template("add_contact.html")

@app.route("/handleAddContact", methods=["POST"])
def handleAddContact(): #commit test2

    name = request.form.get("contact-name")
    number = request.form.get("contact-number")
    contacts.append([name,number])

    return render_template("/home.html")




@app.route("/delete_contact")
def delete_contact():

    return render_template("/delete_contact.html", contacts = contacts)

@app.route("/handleDeleteContact", methods=["POST"])
def handleDeleteContact():

    contact_number_input = request.form.get("contact-number")
    if not contact_number_input.isdigit():
        return render_template("/delete_contact.html", contacts=contacts, error="Please enter a valid number")

    contact_number = int(contact_number_input)

    # Checks if contacts list is empty - if empty prompt user no contact to delete
    if not contacts:
        return render_template("/delete_contact.html", contacts=contacts, error="No contacts you silly goose.")
    
    # Check if contact_number is within range - if contact number is not within range return page until user enters appropriate number
    if contact_number < 1 or contact_number > len(contacts):
        return render_template("/delete_contact.html", contacts=contacts, error="Add a number first!!")


    contacts.pop(contact_number-1)

    return render_template("/home.html")
 

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
