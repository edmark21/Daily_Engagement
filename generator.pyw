import json
from tkinter import *
from tkinter import filedialog

def convert():
    data = text.get("1.0", END).split("\n")
    result = []
    for line in data:
        if line.strip() != "":
            name, number, email = line.split("\t")
            result.append({"name": name, "number": number, "email": email})
    output.delete("1.0", END)
    output.insert(END, json.dumps(result, indent=4))

def save():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".json", initialfile="contacts.json")
    if file:
        file.write(output.get("1.0", END))
        file.close()

root = Tk()
root.title("Convert to JSON")

Label(root, text="Enter data:").pack()
text = Text(root)
text.pack()

Button(root, text="Convert", command=convert).pack()

Label(root, text="Output:").pack()
output = Text(root)
output.pack()

Button(root, text="Save", command=save).pack()

root.mainloop()
