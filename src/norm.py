from typing import Optional

from src.color import Color
from src.execute import ExecuteCommand


# TODO: Currently not printing notices, eg global variables
def check_norm():
    result = ExecuteCommand("norminette")

    if result.exit_code > 1:
        print(result.exit_code)
        print(
            Color.red(
                f"Failed to check Norm{' is norminette installed?' if result.exit_code == 127 else '.'}"
            )
        )
        return

    errors = [line for line in result.stdout.splitlines() if "Error" in line]

    if len(errors) == 0:
        print("Checking Norm:", Color.green("No Norm Errors ʕ·͡ᴥ·ʔ"))
        return

    count = sum(1 for error in errors if error.startswith("Error:"))
    print(
        "Checking Norm:",
        Color.red(f"{count} Norm {'Error' if count == 1 else 'Errors'} •`_´•"),
    )

    for error in errors:
        if error.startswith("Error:"):
            print("\t", end="")
        print(Color.yellow(error))
