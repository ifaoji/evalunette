import os
import sys

from src.args import parse_args
from src.color import Color
from src.projects.projects import get_project


def print_title():
    title = """__________             ______                  __________      
___  ____/__   _______ ___  /___  _______________  /__  /_____ 
__  __/  __ | / /  __ `/_  /_  / / /_  __ \  _ \  __/  __/  _ \\
_  /___  __ |/ // /_/ /_  / / /_/ /_  / / /  __/ /_ / /_ /  __/
/_____/  _____/ \__,_/ /_/  \__,_/ /_/ /_/\___/\__/ \__/ \___/"""

    text = [
        Color.bold(Color.cyan(title)),
        Color.green("  - By sdabland"),
        "",
        Color.lightmagenta(
            "Even though this tester exist, please create your own tests."
        ),
        Color.lightmagenta(
            "You are not learning anything if you are just using a random tester you found online and getting it to print only green!"
        ),
        Color.lightmagenta("(╯°□°)╯︵ ┻━┻"),
        "",
    ]

    print("\n".join(text))


def main():
    args = parse_args()

    print_title()

    if not args.project:
        project = get_project(args.path)

        if not project:
            print(Color.bold(Color.red("ERROR (╥﹏╥)")))

            if str(args.path) == os.getcwd():
                path = "the current working directory"
            else:
                path = f"path `{args.path}`"

            text = [
                f"      Failed to detect project type in {path}.",
                f"      Maybe try specifying the project directly with `--project`.",
            ]

            print(Color.yellow("\n".join(text)))

            sys.exit(1)
    else:
        project = args.project

    print("Testing Project:", Color.bold(Color.cyan(project.name)))

    os.chdir(args.path)

    project(ignore_norm=args.ignore_norm)
