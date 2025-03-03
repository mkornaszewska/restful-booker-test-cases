import pandas as pd
from tabulate import tabulate
import re

test_scenarios_path = "data/restful_booker_test_scenarios.xlsx"
test_cases_path = "data/restful_booker_test_cases.xlsx"
readme_path = "README.md"

df_test_scenarios = pd.read_excel(test_scenarios_path, dtype=str)
df_test_cases = pd.read_excel(test_cases_path, dtype=str)

df_test_scenarios = test_scenarios_path.applymap(lambda x: str(x).replace("\n", "<br/>") if pd.notna(x) else "")
df_test_cases = df_test_cases.applymap(lambda x: str(x).replace("\n", "<br/>") if pd.notna(x) else "")

markdown_test_scenarios = tabulate(df_test_scenarios.to_numpy().tolist(), headers=df_test_scenarios.columns.tolist(), tablefmt="pipe")
markdown_test_cases = tabulate(df_test_cases.to_numpy().tolist(), headers=df_test_cases.columns.tolist(), tablefmt="pipe")

with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

updated_content = re.sub(
    r"(<!-- TEST_SCENARIOS_START -->)(.*?)(<!-- TEST_SCENARIOS_END -->)",
    f"\\1\n\n{markdown_test_scenarios}\n\n\\3",
    readme_content,
    flags=re.DOTALL,
)

updated_content = re.sub(
    r"(<!-- TEST_CASES_START -->)(.*?)(<!-- TEST_CASES_END -->)",
    f"\\1\n\n{markdown_test_cases}\n\n\\3",
    updated_content,
    flags=re.DOTALL,
)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(updated_content)

print("✅ README.md updated with test scenarios and test cases!")
