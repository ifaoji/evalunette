import pathlib

from src.projects.libft import Libft

projects = [Libft]


def get_project(path: pathlib.Path):
    for project in projects:
        if not project.is_project(path):
            continue

        return project

    return None


def get_project_by_identifier(identifier: str):
    identifier = identifier.lower()

    for project in projects:
        if not identifier in project.identifiers:
            continue

        return project

    return None


def get_project_names():
    return [project.name for project in projects]
