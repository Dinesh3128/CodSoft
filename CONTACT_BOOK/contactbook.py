import json
import tkinter as tk
from tkinter import ttk

class ContactBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.contacts = {}

        # Load existing contacts
        self.load_contacts()

        # Create and set up the GUI
        self.create_widgets()

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=2)

    def create_widgets(self):
        # Labels and Entry Widgets
        tk.Label(self.master, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.master, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.master, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.master, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Buttons
        add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        add_button.grid(row=4, column=0, padx=5, pady=5)

        view_button = tk.Button(self.master, text="View Contacts", command=self.view_contacts)
        view_button.grid(row=4, column=1, padx=5, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact_id = len(self.contacts) + 1
            self.contacts[contact_id] = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
            self.save_contacts()
            print(f"Contact '{name}' added successfully!")
        else:
            print("Name and phone are required.")

    def view_contacts(self):
        # Create a new window to display contacts
        view_window = tk.Toplevel(self.master)
        view_window.title("View Contacts")

        # Treeview to display contacts
        contact_tree = ttk.Treeview(view_window, columns=("ID", "Name", "Phone", "Email", "Address"), show="headings")
        contact_tree.heading("ID", text="ID")
        contact_tree.heading("Name", text="Name")
        contact_tree.heading("Phone", text="Phone")
        contact_tree.heading("Email", text="Email")
        contact_tree.heading("Address", text="Address")

        for contact_id, contact_info in self.contacts.items():
            contact_tree.insert("", "end", values=(contact_id, contact_info['Name'], contact_info['Phone'], contact_info['Email'], contact_info['Address']))

        contact_tree.pack()

        # Buttons for Update and Delete
        update_button = tk.Button(view_window, text="Update", command=lambda: self.update_contact(contact_tree))
        update_button.pack(pady=5)

        delete_button = tk.Button(view_window, text="Delete", command=lambda: self.delete_contact(contact_tree))
        delete_button.pack(pady=5)

    def update_contact(self, contact_tree):
        selected_item = contact_tree.selection()
        if not selected_item:
            print("Please select a contact to update.")
            return

        contact_id = contact_tree.item(selected_item, "values")[0]
        contact_info = self.contacts.get(contact_id, {})

        update_window = tk.Toplevel(self.master)
        update_window.title("Update Contact")

        tk.Label(update_window, text=f"Updating Contact ID: {contact_id}").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        tk.Label(update_window, text="Update Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        updated_name_entry = tk.Entry(update_window)
        updated_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        updated_name_entry.insert(0, contact_info.get('Name', ''))

        tk.Label(update_window, text="Update Phone:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        updated_phone_entry = tk.Entry(update_window)
        updated_phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        updated_phone_entry.insert(0, contact_info.get('Phone', ''))

        tk.Label(update_window, text="Update Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        updated_email_entry = tk.Entry(update_window)
        updated_email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        updated_email_entry.insert(0, contact_info.get('Email', ''))

        tk.Label(update_window, text="Update Address:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        updated_address_entry = tk.Entry(update_window)
        updated_address_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        updated_address_entry.insert(0, contact_info.get('Address', ''))

        def perform_update():
            if updated_name_entry.get():
                self.contacts[contact_id]['Name'] = updated_name_entry.get()
            if updated_phone_entry.get():
                self.contacts[contact_id]['Phone'] = updated_phone_entry.get()
            if updated_email_entry.get():
                self.contacts[contact_id]['Email'] = updated_email_entry.get()
            if updated_address_entry.get():
                self.contacts[contact_id]['Address'] = updated_address_entry.get()

            self.save_contacts()
            print(f"Contact with ID {contact_id} updated successfully!")
            update_window.destroy()

            # Refresh the view
            self.view_contacts()
            
        update_button = tk.Button(update_window, text="Update", command=perform_update)
        update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def delete_contact(self, contact_tree):
        selected_item = contact_tree.selection()
        if not selected_item:
            print("Please select a contact to delete.")
            return

        contact_id = contact_tree.item(selected_item, "values")[0]
        contact_info = self.contacts.get(contact_id, {})

        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Contact")

        tk.Label(delete_window, text=f"Deleting Contact ID: {contact_id}").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        tk.Label(delete_window, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Label(delete_window, text=contact_info.get('Name', '')).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(delete_window, text="Phone:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        tk.Label(delete_window, text=contact_info.get('Phone', '')).grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(delete_window, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        tk.Label(delete_window, text=contact_info.get('Email', '')).grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(delete_window, text="Address:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        tk.Label(delete_window, text=contact_info.get('Address', '')).grid(row=4, column=1, padx=5, pady=5, sticky="w")

        def perform_delete():
            del self.contacts[contact_id]
            self.save_contacts()
            print(f"Contact with ID {contact_id} deleted successfully!")
            delete_window.destroy()

            # Refresh the view
            self.view_contacts()

        delete_button = tk.Button(delete_window, text="Delete", command=perform_delete)
        delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

def main():
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
