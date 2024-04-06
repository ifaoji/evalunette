import argparse
import dataclasses
import pathlib
from typing import Optional

from src.projects.projects import get_project_by_identifier, get_project_names


@dataclasses.dataclass
class Args:
    path: str
    project: Optional[str]
    ignore_norm: bool


def str_to_path_dir(path_str: str):
    path = pathlib.Path(path_str)

    if not path.exists():
        raise argparse.ArgumentTypeError(f"The provided path `{path}` does not exist.")

    if not path.is_dir():
        raise argparse.ArgumentTypeError(
            f"The provided path `{path}` is not a directory."
        )

    return path


def valid_project(project_str: str):
    project = get_project_by_identifier(project_str)

    if not project:
        raise argparse.ArgumentTypeError(
            f"The provided project `{project_str}` does not exist."
        )

    return project


def parse_args() -> Args:
    parser = argparse.ArgumentParser(description="Evalunette")

    parser.add_argument(
        "path",
        nargs="?",
        type=str_to_path_dir,
        default=pathlib.Path.cwd(),
        help="The path to your project.",
    )

    parser.add_argument(
        "-p",
        "--project",
        type=valid_project,
        help=f"The project you want to test. Valid projects are: {', '.join(get_project_names())}.",
    )

    parser.add_argument(
        "--ignore-norm", action="store_true", help="Do not execute norminette."
    )

    args = parser.parse_args()

    return Args(args.path, args.project, args.ignore_norm)
