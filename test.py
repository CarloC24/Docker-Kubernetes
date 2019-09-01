import os

variable = os.environ.get("VARS") or "NO VAR SUPPLIED"

print(f"variable {variable} ")
