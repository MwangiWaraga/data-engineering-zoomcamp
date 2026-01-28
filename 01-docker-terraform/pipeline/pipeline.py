import sys
print("arguments", sys.argv)

# name = sys.argv[0]
month = int(sys.argv[1])
# print(f"Running {name} pipeline for day =  {day}")

import pandas as pd

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_month_{sys.argv[1]}.parquet")
