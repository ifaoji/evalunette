import os
import shutil
import sys
import tempfile
import time
from pathlib import Path

from src.color import Color
from src.execute import ExecuteCommand
from src.norm import check_norm
from src.project import Project
from src.spinner import Spinner


def make_exec(path: str, target: str) -> bool:
    result = ExecuteCommand(f"make -C {path} {target}")

    return result.exit_code == 0


def print_test(name: str, ok_count: int, ko_count: int, longest_name: int):
    print(Color.cyan(f"\r{name.ljust(longest_name + 5)}"), end="")

    print(Color.green(f"[{ok_count} {'OK' if ok_count == 1 else 'OKs'}]"), end="")

    if ko_count > 0:
        print(Color.red(f" [{ko_count} {'KO' if ko_count == 1 else 'KOs'}]"), end="")

    print("\033[K", end="", flush=True)


def test_isalpha(path: str, longest_name: int):
    if not make_exec(path, "isalpha"):
        print(Color.bold(Color.red("Failed to compile")))
        return

    exec = path + "/bin/isalpha"

    # Currently only testing those values, since apparently libc uses arrays or
    # so to check which can cause a segfault lol
    # Entire uchar range might also be problematic, who knows, therefore I only
    # check for valid ascii values and EOF as of now.
    cases = [
        -1,  # EOF
        *range(0, 128),
        # *range(-128, 128),
        # *range(321, 347),
        # *range(300, 321),
        # *range(347, 400),
        # 2147483647,
        # -2147483648,
    ]

    oks = 0
    kos = 0
    for case in cases:
        result = ExecuteCommand(f"{exec} {case}")

        if result.exit_code == 0:
            oks += 1
        else:
            kos += 1
            print(f"\n\n\n{case} {result.exit_code}\n\n\n")

        print_test("ft_isalpha", oks, kos, longest_name)

    print()


tests = [("ft_isalpha", test_isalpha)]


class Libft(Project):
    name = "Libft"
    identifiers = ["libft", "lft"]

    def __init__(self, ignore_norm=False):
        if not ignore_norm:
            check_norm()

        with Spinner(f"Creating libft.a", done_message=f"Created libft.a"):
            make_result = ExecuteCommand("make", 10)
            if make_result.exit_code != 0:
                print(
                    Color.bold(Color.red("ERROR (╥﹏╥)\n")),
                    Color.yellow("Failed to run make"),
                )
                sys.exit(1)

            make_result = ExecuteCommand("make clean", 10)
            if make_result.exit_code != 0:
                print(
                    Color.bold(Color.red("ERROR (╥﹏╥)\n")),
                    Color.yellow("Failed to run make clean"),
                )
                sys.exit(1)

        self.start_test()

    def start_test(self):
        longest_name = max(len(s[0]) for s in tests)

        with tempfile.TemporaryDirectory() as tmp_dir:
            code_path = Path(f"{__file__}/../../../tests/libft").resolve()
            # Since `copytree` requires the destination directory not to exist
            tmp_dir += "/tmp"
            shutil.copytree(code_path, tmp_dir)
            shutil.copy("./libft.h", tmp_dir)
            shutil.copy("./libft.a", tmp_dir)

            for test in tests:
                test[1](tmp_dir, longest_name)

    @staticmethod
    def is_project(path: Path) -> bool:
        end_part = path.parts[-1]

        if end_part.lower() in Libft.identifiers:
            return True

        return False
