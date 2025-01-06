import tkinter as tk
from tkinter import ttk

top = tk.Tk()  # Creating the parent window
top.title("Restaurant App")  # Title of the application

# Labels and data for the menu items
label = tk.Label(top, text="Welcome to our restaurant!", font=("Arial", 30, "bold"))
label.pack(pady=60)  # Label position

def new_window():
    second_window = tk.Toplevel()
    data1 = ["Grilled Chicken", "Beef Steak", "Spaghetti Bolognese", "Shrimp Fried Rice", "Margherita Pizza", 
         "Chicken Alfredo Pasta", "Smashed Burger", "Chicken Shawarma Plate", "Lasagna", "Fish and Chips", 
         "Salmon", "Chicken Curry", "BBQ Ribs", "Chicken Wings", "Beef Tacos"]
    data2 = ["150EGP", "350EGP", "100EGP", "170EGP", "160EGP", "220EGP", "180EGP", "155EGP", "230EGP", "260EGP", 
         "280EGP", "120EGP", "195EGP", "175EGP", "240EGP"]
    data3 = ["Ice Cream", "Cheesecake", "Brownies", "Apple Pie", "Tiramisu", "Water", "Iced Tea", "Mint Lemonade", 
         "Mojito", "Turkish Coffee", "Latte", "Tea", "Hot Chocolate", "Cappuccino", "Espresso"]
    data4 = ["25EGP", "50EGP", "60EGP", "80EGP", "100EGP", "10EGP", "35EGP", "40EGP", "50EGP", "65EGP", "80EGP", 
         "30EGP", "75EGP", "85EGP", "95EGP"]

    
    table = ttk.Treeview(second_window, columns=("main", "p1", "dd", "p2"), show="headings")
    table.heading("main", text="Main Dishes")
    table.heading("p1", text="Prices")
    table.heading("dd", text="Desserts and Drinks")
    table.heading("p2", text="Prices")
    table.pack()

    for i in range(len(data1)):
        table.insert("", "end", values=(data1[i], data2[i], data3[i], data4[i]))

# View Menu Button
button = tk.Button(top, text="View Menu", width=25, height=2, font=("Arial", 20), command=new_window)
button.pack(side="top")  # Positioning the button

# Items and their prices
items = {
    "Grilled chicken": 150.0,
    "Beef steak": 350.0,
    "Spaghetti Bolognese": 100.0,
    "Shrimp Fried Rice": 170.0,
    "Margherita Pizza": 160.0,
    "Chicken Alfredo Pasta": 220.0,
    "Smashed Burger": 180.0,
    "Chicken Shawarma Plate": 155.0,
    "Lasagna": 230.0,
    "Fish and Chips": 260.0,
    "Salmon": 280.0,
    "Chicken Curry": 120.0,
    "BBQ Ribs": 195.0,
    "Chicken Wings": 175.0,
    "Beef Tacos": 240.0,
    "Ice Cream": 25.0,
    "Cheesecake": 50.0,
    "Brownies": 60.0,
    "Apple Pie": 80.0,
    "Tiramisu": 100.0,
    "Water": 10.0,
    "Iced Tea": 35.0,
    "Mint Lemonade": 40.0,
    "Mojito": 50.0,
    "Turkish Coffee": 65.0,
    "Latte": 80.0,
    "Tea": 30.0,
    "Hot Chocolate": 75.0,
    "Cappuccino": 85.0,
    "Espresso": 95.0,
}

# Create frame for items with checkboxes
frame = tk.Frame(top)
frame.pack(fill="both", expand=True)

# add a canvas to the frame for scrolling
canvas = tk.Canvas(frame)
canvas.pack(side="left", fill="both", expand=True)

# add a vertical scrollbar
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# configure canvas scrolling
canvas.configure(yscrollcommand=scrollbar.set)  #expand
canvas.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# create a frame inside the canvas for adding checkboxes
scrollable_frame = tk.Frame(canvas) 
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw") # make the box dirction

# create variables for item checkboxes
item_vars = [tk.BooleanVar(value=False) for _ in items]

# display items with checkboxes inside the scrollable frame
tk.Label(scrollable_frame, text="Select items to add to order:").pack(anchor='w') # Make square to choose the element and make it on the left
for i, (item, price) in enumerate(items.items()):
    tk.Checkbutton(scrollable_frame, text=f"{item} - ${price:.2f}", variable=item_vars[i]).pack(anchor='w')

# order list to hold the selected items
order_list = []

def add_to_order():  # Function to add selected items to the order
    selected_items = []
    for item, var in zip(items, item_vars):
        if var.get():
            selected_items.append(item)
            var.set(False)  # Uncheck the checkbox after adding to order
    
    order_list.extend(selected_items)  # Add selected items to the order list

    # Update the order display
    update_order_display()

def update_order_display():  # Function to update the order display
    order_text = "\n".join(order_list) if order_list else "No items in the order"
    order_display.config(text=f"Order:\n{order_text}")

# add to Order Button
add_order_button = tk.Button(top, text="Add to Order", command=add_to_order)
add_order_button.pack(pady=10)

# display the order summary
order_display = tk.Label(top, text="Order:\nNo items in the order", justify="left")
order_display.pack()

# calculate total button
# Define tax rate (e.g., 10%)
TAX_RATE = 0.10

def calculate_total():  # function to calculate the total of selected items including tax
    subtotal = sum(items[item] for item in order_list)
    tax = subtotal * TAX_RATE
    total_cost = subtotal + tax

    # display the result
    total_label.config(
        text=f"Subtotal: ${subtotal:.2f}\n"
             f"Tax (10%): ${tax:.2f}\n"
             f"Total: ${total_cost:.2f}"
    )

# calculate Total Button
calculate_button = tk.Button(top, text="Calculate Total", command=calculate_total)
calculate_button.pack(pady=10)

# Total Display
total_label = tk.Label(top, text="Subtotal: $0.00\nTax (10%): $0.00\nTotal: $0.00", justify="left")
total_label.pack()


top.mainloop() 
# run the application