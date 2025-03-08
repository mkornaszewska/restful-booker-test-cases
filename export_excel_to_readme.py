import pandas as pd
from tabulate import tabulate
import re

# File paths
test_scenarios_path = "data/restful_booker_test_scenarios.xlsx"
test_cases_path = "data/restful_booker_test_cases.xlsx"
readme_path = "README.md"

# Load Excel files
df_test_scenarios = pd.read_excel(test_scenarios_path, dtype=str)
df_test_cases = pd.read_excel(test_cases_path, dtype=str)

# Ensure consistent formatting
df_test_scenarios = df_test_scenarios.applymap(lambda x: str(x).replace("\n", "<br/>") if pd.notna(x) else "")
df_test_cases = df_test_cases.applymap(lambda x: str(x).replace("\n", "<br/>") if pd.notna(x) else "")

# Group scenarios by priority
priority_levels = ["P0", "P1", "P2"]
priority_tables = {}

for priority in priority_levels:
    df_filtered = df_test_scenarios[df_test_scenarios['Priority'] == priority]

    if not df_filtered.empty:
        df_filtered = df_filtered.sort_values(by="Priority")  # Change this column if needed

        # Create markdown table
        priority_tables[priority] = f"## {priority}\n\n" + tabulate(df_filtered.to_numpy().tolist(), headers=df_filtered.columns.tolist(), tablefmt="pipe")
    else:
        priority_tables[priority] = f"## {priority}\n\nNo test scenarios found for this priority."

# Read existing README file
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# Update README with categorized test scenarios
for priority, table in priority_tables.items():
    readme_content = re.sub(
        rf"(<!-- {priority}_TEST_SCENARIOS_START -->)(.*?)(<!-- {priority}_TEST_SCENARIOS_END -->)",
        f"\\1\n\n{table}\n\n\\3",
        readme_content,
        flags=re.DOTALL,
    )

# Update README with test cases
markdown_test_cases = tabulate(df_test_cases.to_numpy().tolist(), headers=df_test_cases.columns.tolist(), tablefmt="pipe")
readme_content = re.sub(
    r"(<!-- TEST_CASES_START -->)(.*?)(<!-- TEST_CASES_END -->)",
    f"\\1\n\n{markdown_test_cases}\n\n\\3",
    readme_content,
    flags=re.DOTALL,
)

# Write back the updated content
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated with categorized test scenarios and test cases!")