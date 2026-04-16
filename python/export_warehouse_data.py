import pandas as pd
from sqlalchemy import create_engine
from config import *

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

query = """
SELECT *
FROM fact_sales
LIMIT 1000
"""

df = pd.read_sql(query, engine)

df.to_csv("data/warehouse/fact_sales_sample.csv", index=False)

print("Warehouse sample exported")