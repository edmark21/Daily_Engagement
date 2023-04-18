import tkinter as tk
import json

with open('contacts.json', 'r') as f:
    data = json.load(f)

class ResultsViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Results")
        self.pack()
        self.create_widgets()
        self.show_results()

    def create_widgets(self):
        dispositions = ["", "AE CONTACTED", "RTVM | SMS SENT", "CALL DROPPED", "WRONG NUMBER", "RESIGNED | NOT INTERESTED", "SMS Blast"]
        self.labels = {}
        
        for disposition in dispositions:
            label = tk.Label(self)
            label.pack()
            self.labels[disposition] = label
        
        # Added label to display total number of contacts with a disposition
        self.total_label = tk.Label(self)
        self.total_label.pack()

    def show_results(self):
        dispositions = ["", "AE CONTACTED", "RTVM | SMS SENT", "CALL DROPPED", "WRONG NUMBER", "RESIGNED | NOT INTERESTED", "SMS Blast"]
        results = {disposition: 0 for disposition in dispositions}
        
        for contact in data:
            if "disposition" in contact:
                results[contact["disposition"]] += 1
            else:
                results[""] += 1
        
        for disposition, count in results.items():
            if disposition == "":
                self.labels[disposition]["text"] = f"No Disposition: {count}"
            else:
                self.labels[disposition]["text"] = f"{disposition}: {count}"
        
        # Update total label text
        total = sum(results.values()) - results[""]
        self.total_label["text"] = f"Total Contacted: {total}"

root = tk.Tk()
app = ResultsViewer(master=root)
app.mainloop()
