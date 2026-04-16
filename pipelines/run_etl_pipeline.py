import os
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

steps = [
    "python python/data_quality_checks.py",
    "python python/load_staging_tables.py"
]

for step in steps:
    logging.info(f"Running: {step}")
    result = os.system(step)

    if result == 0:
        logging.info(f"Success: {step}")
    else:
        logging.error(f"Failed: {step}")

print("ETL pipeline finished")