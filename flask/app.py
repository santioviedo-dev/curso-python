from flask import Flask, render_template, redirect
from clientDAO import ClientDAO
from client import Client
from client_form import ClientForm

app = Flask(__name__) # Name of the current file

app.config["SECRET_KEY"] = "secret_key"

app_title = "Fit Zone GYM"

@app.route("/") # http://127.0.0.1:5000/
@app.route("/index.html") # response from two routes with the same function
def start():
    app.logger.debug("Entry to the init path /")
    clients_db = ClientDAO.select()
    
    client = Client()
    client_form = ClientForm(obj=client)
    
    return render_template("index.html", title=app_title, clients= clients_db, form=client_form)

@app.route("/save", methods=["POST"])
def save():
    client = Client()
    client_form = ClientForm(obj=client)
    if client_form.validate_on_submit():
        client_form.populate_obj(client)
        if not client.id:
            ClientDAO.insert(client)
        else:
            ClientDAO.update(client)
    return redirect("/")

@app.route("/reset")
def reset():
    return redirect("/")

@app.route("/edit/<int:id>") # if the data is string, we can skip define the type
def edit(id):
    client = ClientDAO.select_by_id(id)
    client_form = ClientForm(obj=client)
    clients_db = ClientDAO.select()
    return render_template("index.html", title=app_title, clients=clients_db, form=client_form)

@app.route("/delete/<int:id>")
def delete(id):
    ClientDAO.delete(id)
    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True)