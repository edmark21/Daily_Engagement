import json
import pandas as pd

with open('contacts.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)
