from flask import Flask,render_template,request
import json
app = Flask(__name__) 
FILE_NAME = "customers.json"
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/add-customer",    methods=["GET","POST"])
def add_customer():
    if request.method =="POST":
        name=request.form["name"]
        phone=request.form["phone"]
        item=request.form["item"]
        quantity=request.form["quantity"]
        amount=float(request.form["amount"])
       
        customer = {
            "name":name,
            "phone":phone,
            "item":item,
            "quantity":quantity,
            "amount":amount
        }

        try:
            with open(FILE_NAME,"r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {
                "borrowers":[],
                "paid_customers":[]
            }
        data["borrowers"].append(customer)
        with open(FILE_NAME,"w") as file:
            json.dump(data,file,indent=4)
        print("Customer saved successfully!")
    return     render_template("add_customer.html")

@app.route("/customers")
def view_customers():
    try:
        with open(FILE_NAME,"r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data ={
            "borrowers":[],
            "paid_customers":[]
        }
    borrowers = data.get("borrowers",[])
    return render_template("customers.html",    borrowers=borrowers)
@app.route("/dashboard")
def dashboard():
    try:
        with open(FILE_NAME,"r") as file:
            data=json.load(file)
    except FileNotFoundErorror:
        data={
            "borrowers":[],
            "paid_customers":[]
        }
    borrowers = data.get("borrowers",[])
    paid_customers =     data.get("paid_customers",[])
    pending_count = len(borrowers)
    total_pending = 0
    for borrower in borrowers:
        total_pending = total_pending+    borrower["amount"]

    total_collected = 0
    for customer in paid_customers:
        total_collected = total_collected +    customer["amount"]

    return render_template(    "dashboard.html",
           pending_count=pending_count,
           total_pending=total_pending,
           total_collected=total_collected,
           borrowers=borrowers
           )
if __name__ == "__main__":
    app.run(debug=True)