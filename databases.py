import tkinter as tk
from PIL import ImageTk, Image
import sqlite3

root = tk.Tk()
root.geometry("400x400")

#Create a database or connect to one
db = sqlite3.connect("adress_book.sqlite")

#Create cursor
c = db.cursor()

#Create table
#c.execute("""
#
#        CREATE TABLE adresses (
#            first_name text, 
#            last_name text,
#            adress text,
#            city text,
#            state text,
#            zipcode integer
 #       )
#
#""")

#create submit function
def submit():
    #Create a database or connect to one
    db = sqlite3.connect("adress_book.sqlite")
    #Create cursor
    c = db.cursor()

    #insert into table
    c.execute("INSERT INTO  adresses VALUES (:f_name, :l_name, :adress, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'adress': adress.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            }    
    )

    #Commit changes
    db.commit()

    #Close connection
    db.close()

    #Clear The Text Boxes
    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    adress.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zipcode.delete(0, tk.END)

#Create Query function
def query():
    #Create a database or connect to one
    db = sqlite3.connect("adress_book.sqlite")
    #Create cursor
    c = db.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM adresses")
    records = c.fetchall()

    #Loop through results
    print_records = ''
    for record in records:
        print_records += f"{record} \n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    #Commit changes
    db.commit()

    #Close connection
    db.close()

#Create text boxes
f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

adress = tk.Entry(root, width=30)
adress.grid(row=2, column=1, padx=20)

city = tk.Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = tk.Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

#Create Text Boy Labels
f_name_label = tk.Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = tk.Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

adress_label = tk.Label(root, text="Adress")
adress_label.grid(row=2, column=0)

city_label = tk.Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = tk.Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = tk.Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

#Create Submit Button
submit_btn = tk.Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create a Query Button
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx= 137)

#Commit changes
db.commit()

#Close connection
db.close()


root.mainloop()