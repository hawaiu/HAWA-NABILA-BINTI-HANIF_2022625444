import tkinter as tk
import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="night_movie"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def submit():
    student_name = student_name_entry.get()
    student_id = student_id_entry.get()
    set_type = package_var.get()
    packs = int(packs_entry.get())
    
    #  the price below is to defined the value from selections
    prices = {
        "Set A": 6,
        "Set B": 9,
        "Set C": 13,
  
    }
    
    # Calculate the total price. This will be derived from selection (Package, Pack).
    total_price = (prices[set_type] * packs)
    
    # To insert data to database
    sql = "INSERT INTO data (student_name, student_id, package_type, package_pack, package_price) VALUES (%s, %s, %s, %s, %s)"
    val = (student_name, student_id, set_type, packs, total_price)
    mycursor.execute(sql, val)
    mydb.commit()

    # To print back the output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python. 
    output_label.config(text=f"Student: {student_name}\nId: {student_id}\nSet: {set_type}, Packs: {packs}, Total Price: RM{total_price}")


# Main Window
root = tk.Tk()
root.title("Movies")
root.geometry('600x700')


# Page Title
label = tk.Label(root, text='Calculate your Set Price', font=("Times New Romans",30, "bold"))
label.pack(ipadx=10, ipady=10)

# Prices List by using textbox
prices_text = tk.Text(root, height=15, width=45)
prices_text.pack(pady=20)

# The defined list by using pricebox
prices_text.insert(tk.END, "Set & Prices:\n\n")
prices_text.insert(tk.END, "SetA: Cloudy with a Chance of Meatballs, Popcorn, Soda \nPrice: RM6\n\n")
prices_text.insert(tk.END, "Set B: Cloudy with a Chance of Meatballs, Popcorn, Soda, Freegift \nPrice: RM9\n\n")
prices_text.insert(tk.END, "Set C: Cloudy with a Chance of Meatballs, Popcorn, Soda, Meatballs, Blanket \nPrice: RM13\n\n")
prices_text.configure(state='disabled')

#Student Name Entry
student_name_label = tk.Label(root, text="Student Name:", font= ("Times New Roman",14))
student_name_label.pack()
student_name_entry = tk.Entry(root)
student_name_entry.pack()

#Student ID Entry
student_id_label = tk.Label(root, text="Student Id:", font= ("Times New Roman",14))
student_id_label.pack()
student_id_entry = tk.Entry(root)
student_id_entry.pack()

# Set Type Dropdown (Label)
packs_label = tk.Label(root, text="Choose Your Package:", font= ('Times New Roman',14))
packs_label.pack()

# Set Type Dropdown
package_var = tk.StringVar(root)
package_var.set("Select your Set")  # Default value before your selection
trip_dropdown = tk.OptionMenu(root, package_var, "Set A", "Set B", "Set C")
trip_dropdown.pack(pady=10)


# Packs Entry.
packs_label = tk.Label(root, text="Packs:")
packs_label.pack()
packs_entry = tk.Entry(root)
packs_entry.pack()

# Save Button
save_button = tk.Button(root, text="Calculate", command=submit)
save_button.pack(pady=10)

# Output Label & result
label = tk.Label(root, text='Price Package', font=("Times New Romans",12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()