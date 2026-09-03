import pandas as pd
import numpy as np

df=pd.read_csv("konkanifinal.csv")

duplicate=df[df.duplicated()]

df = df.drop_duplicates()

# Save cleaned data to new CSV
df.to_csv("cleaned_data.csv", index=False)

print("Duplicates removed successfully!")