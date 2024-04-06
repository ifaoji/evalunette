from pathlib import Path

from src.norm import check_norm
from src.project import Project


class Libft(Project):
    name = "Libft"
    identifiers = ["libft", "lft"]

    def __init__(self, ignore_norm=False):
        if not ignore_norm:
            check_norm()

    @staticmethod
    def is_project(path: Path) -> bool:
        end_part = path.parts[-1]

        if end_part.lower() in Libft.identifiers:
            return True

        return False
