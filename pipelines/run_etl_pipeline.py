import os
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

steps = [
    "python python/schema_validation.py",
    "python python/data_quality_checks.py",
    "python python/load_staging_tables.py",
    'psql -U postgres -d retail_inventory_db -f sql/staging/create_staging_tables.sql',
    'psql -U postgres -d retail_inventory_db -f sql/warehouse/create_warehouse_tables.sql',
    'psql -U postgres -d retail_inventory_db -f sql/warehouse/load_fact_dimension_tables.sql',
    'psql -U postgres -d retail_inventory_db -f sql/warehouse/incremental_load.sql'
    "python python/export_warehouse_data.py"
]

for step in steps:
    logging.info(f"Running: {step}")
    result = os.system(step)

    if result == 0:
        logging.info(f"Success: {step}")
    else:
        logging.error(f"Failed: {step}")



print("ETL pipeline finished")