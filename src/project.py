import pathlib


class Project:
    name: str
    identifiers: list[str]

    def is_project(path: pathlib.Path) -> bool:
        """
        Detect whether the provided path is for this project.
        """

        return False
