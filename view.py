import os
import pandas as pd

df = pd.read_csv("./records/record.csv", encoding="utf-8")

print(df.to_string(index=False))