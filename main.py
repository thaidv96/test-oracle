import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data.csv")

engine = create_engine('oracle+cx_oracle://root:123456d@localhost:2210')
print("connecting...")
connection = engine.connect()
print("connected...")
df.to_sql(name='dancu', con=connection, schema='bhxh', if_exists='append')
print("Done")
