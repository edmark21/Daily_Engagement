import tkinter as tk
import json

with open('contacts.json', 'r') as f:
    data = json.load(f)

class ContactViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Daily Engagement")
        self.pack()
        self.create_widgets()
        self.current_contact = 0
        self.show_contact()

    def create_widgets(self):
        image_file = "us.pgm"
        self.image = tk.PhotoImage(file=image_file)
        self.image_label = tk.Label(self, image=self.image)
        self.image_label.pack()

        self.name_label = tk.Label(self)
        self.name_label.pack()
        self.name_label.bind("<Button-1>", self.copy_name)

        self.number_label = tk.Label(self)
        self.number_label.pack()
        self.number_label.bind("<Button-1>", self.copy_number)

        self.email_label = tk.Label(self)
        self.email_label.pack()
        self.email_label.bind("<Button-1>", self.copy_email)

        dispositions = ["", "AE CONTACTED", "RTVM | SMS SENT", "CALL DROPPED", "WRONG NUMBER", "RESIGNED | NOT INTERESTED", "SMS Blast"]
        self.disposition_var = tk.StringVar(self)
        self.disposition_var.set(dispositions[0])
        self.disposition_var.trace("w", self.save_disposition)
        self.disposition_dropdown = tk.OptionMenu(self, self.disposition_var, *dispositions)
        self.disposition_dropdown.pack()

        # Added label to display current contact index and total number of contacts
        self.index_label = tk.Label(self)
        self.index_label.pack()

        # Added button to navigate to first contact without a disposition
        self.continue_button = tk.Button(self, text="Continue", command=self.continue_contact)
        self.continue_button.pack()

        self.prev_button = tk.Button(self, text="Previous", command=self.prev_contact)
        self.prev_button.pack(side="left")

        self.next_button = tk.Button(self, text="Next", command=self.next_contact)
        self.next_button.pack(side="right")

    def show_contact(self):
        contact = data[self.current_contact]
        # Update index label text
        self.index_label["text"] = f"{self.current_contact + 1}/{len(data)}"
        
        # Display contact information
        self.name_label["text"] = contact["name"]
        self.number_label["text"] = contact["number"]
        self.email_label["text"] = contact["email"]
        
        if "disposition" in contact:
            self.disposition_var.set(contact["disposition"])
        else:
            self.disposition_var.set("")

    def save_disposition(self, *args):
        contact = data[self.current_contact]
        contact["disposition"] = self.disposition_var.get()
        
        with open('contacts.json', 'w') as f:
            json.dump(data, f)

    def prev_contact(self):
        if self.current_contact > 0:
            self.current_contact -= 1
            self.show_contact()

    def next_contact(self):
        if self.current_contact < len(data) - 1:
            self.current_contact += 1
            self.show_contact()

    def copy_name(self, event):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.name_label["text"])

    def copy_number(self, event):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.number_label["text"])

    def copy_email(self, event):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.email_label["text"])

    # Added method to navigate to first contact without a disposition
    def continue_contact(self):
        for i, contact in enumerate(data):
            if "disposition" not in contact:
                self.current_contact = i
                self.show_contact()
                break

root = tk.Tk()
app = ContactViewer(master=root)
app.mainloop()

        
