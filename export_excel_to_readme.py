import pandas as pd
from tabulate import tabulate

excel_file_path = "data/restful_booker_test_cases.xlsx"

df = pd.read_excel(excel_file_path)

markdown_table = tabulate(df.values.tolist(), headers=df.columns.tolist(), tablefmt="pipe")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Test Cases\n\n")
    f.write(markdown_table)

print("✅ README.md updated with Excel data!")
