from datetime import datetime
import json

borrowers = []
paid_customers = []

FILE_NAME = "customers.json"

def save_data():
    data = {
        "borrowers":borrowers,
        "paid_customers":paid_customers
    }

    with open(FILE_NAME,"w") as file:
        json.dump(data,file,indent=4)

def add_borrower():
    print("\n--- ADD BORROWER ---")

    name = input("Customer name:")
    phone = input("Phone number:")
    item = input("Item taken:")
    quantity = input("Quantity:")
    amount =float(input("Amount to return;"))

    borrower = {
        "name": name,
        "phone": phone,
        "item": item,
        "quantity": quantity,
        "amount": amount
    }
    borrowers.append(borrower)
    print("\nBorrower added successfully!")
    save_data()
def load_data():
    global borrowers,paid_customers
    try:
        with open(FILE_NAME,"r") as file:
            data = json.load(file)
        borrowers = data.get("borrowers",[])
        paid_customers = data.get("paid_customers",[])

    except FileNotFoundError:
        borrowers = []
        paid_customers = []
def search_customer():
    print("\n---- SEARCH CUSTOMER ----")
    search = input("Enter customer name:").strip().lower()
    found = False
    for i,borrower in enumerate(borrowers):
        name = str(borrower["name"]).strip().lower()
        if search == name:
             print("\nPending Customer",i+1)
             print("Name:",borrower["name"])
             print("Phone:",borrower["phone"])
             print("Item:",borrower["item"])
             print("Quantity:",borrower["quantity"])
             print("Amount Due:₹",borrower["amount"])
             found = True
    for i,customer in enumerate(paid_customers):
        name = str(customer["name"]).strip().lower()
        if search == name:
             print("\nPaid Customer",i+1)
             print("Name:",customer["name"])
             print("Phone:",customer["phone"])
             print("Item:",customer["item"])
             print("Quantity:",customer["quantity"])
             print("Amount paid:₹",customer["amount"])
             print("Payment Time:",customer["payment_time"])
             found = True
    if not found:
        print("Customer not found")



def mark_as_paid():
    print("\n--- MARK AS PAID---")
    if len(borrowers) == 0:
        print("No pending borrowers.")
        return
    for i,borrower in enumerate(borrowers):
        print(i+1,"-",borrower["name"],"-",borrower["amount"])
    choice = int(input("Enter borrower number:"))
    borrower = borrowers.pop(choice - 1)
    payment_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    borrower["payment_time"] = payment_time
    paid_customers.append(borrower)
    save_data()
    print(borrower["name"],"has been marked as paid ")

def dashboard():
    print("\n --- DASHBOARD ---")
    pending_count = len(borrowers)
    print("Pending Customers:",pending_count)
    print("\nPending Customer List:")
    for i ,borrower in enumerate(borrowers):
        print(
            i+1,"-",borrower["name"],"-",borrower["phone"]
        )
    total_pending = 0
    for borrower in borrowers:
        total_pending = total_pending + borrower["amount"]
    print("Total Amount Pending:₹",total_pending)
    total_collected = 0

    for customer in paid_customers:
        total_collected = total_collected + customer["amount"]
    print("Total Amount Collected :₹",total_collected)
def edit_customer():
    print("\n ---- EDIT CUSTOMER ----")
    if len(borrowers) == 0:
        print("No pending borrowers.")
        return
    for i,borrower in enumerate(borrowers):
        print(i+1,"-",borrower["name"],"-",borrower["amount"])
    choice = int(input("Enter borrower number to edit:"))
    borrower = borrowers[choice-1]
    new_name = input("Enter new customer name:")
    borrower["name"]=new_name
    new_phone = input("Enter new customer phone:")
    borrower["phone"]=new_phone
    new_item = input("Enter new customer item:")
    borrower["item"]=new_item
    new_quantity = input("Enter new customer quantity:")
    borrower["quantity"]=new_quantity
    new_amount=float(input("Enter new amount:"))
    borrower["amount"]=new_amount 
    
    save_data()
    print("Customer details updated successfully!")
    
def delete_customer():
    print("\n---- DELETE CUSTOMER ---")
    if len(borrowers)==0:
        print("No pending borrowers.")
        return
    for i,borrower in enumerate(borrowers):
        print(i+1,"-",borrower["name"],"-",borrower["amount"])
        choice=int(input("Enter borrower number to delete:"))
        borrower=borrowers[choice-1]
        confirm=input("Are you sure you want to delete "+borrower["name"]+"?(Yes / No):").lower()
        if confirm =="Yes":
            borrowers.pop(choice-1)
            save_data()
            print(borrower["name"],"Has been Deleted!")
        else:
            print("Delete Cancelled")
load_data()

while True:
        print("\n====================================")
        print("    SHOP CREDIT MANAGER")
        print("=====================================")
        print("1. Add Borrower")
        print("2. View Borrowers")
        print("3. Mark as Paid")
        print("4. View Paid Customers")
        print("5. Dashboard")
        print("6. Search Customer")
        print("7. Edit Customer")
        print("8.Delete Customer ")
        print("9.Exit")
        choice = input("Enter your choice :")
        if choice =="1":
            add_borrower()
        elif choice == "2":
            print("\n===== PENDING BORROWERS ====")
            if len(borrowers)== 0:
                print("No pending borrowers.")
            else:
                for i,borrower in  enumerate(borrowers):
                    print("\nBorrower",i+1)
                    print("Name:",borrower["name"])
                    print("Phone:",borrower["phone"])
                    print("Item:",borrower["item"])
                    print("Quantity:",borrower["quantity"])
                    print("Amount Due:₹",borrower["amount"])
        elif choice =="3":
            mark_as_paid()
        elif choice =="4":
           print("\n===== PAID CUSTOMERS ====")
           if len(paid_customers)== 0:
             print("No paid customers.")
           else:
            for i,customer in  enumerate(paid_customers):
                print("\nCustomer",i+1)
                print("Name:",customer["name"])
                print("Phone:",customer["phone"])
                print("Item:",customer["item"])
                print("Quantity:",customer["quantity"])
                print("Amount Paid:₹",customer["amount"])
                print("Payment time:",customer["payment_time"])
        elif choice == "5":
            dashboard()
        elif choice == "6":
            search_customer()
        elif choice == "7":
            edit_customer()
        elif choice == "8":
            delete_customer()
        elif choice == "9":
            print("Good Bye!!")
            break
        else:
            print("Invalid choice")
