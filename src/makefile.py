import re
from collections import defaultdict


def extract_makefile_rules(path):
    """
    Extracts rules from a Makefile.

    Parameters:
        path (str): Path to the Makefile.

    Returns:
        dict: A dictionary where each key is a target and the value is a tuple containing
              a list of dependencies and a list of commands for that target.
    """
    rule_pattern = re.compile(r"^([^\s#]+)\s*:\s*(.*?)$")
    command_pattern = re.compile(r"^\t+(.+)$")

    with open(path, "r") as file:
        lines = file.readlines()

    rules = defaultdict(lambda: {"dependencies": [], "commands": []})
    current_target = None

    for line in lines:
        line = line.rstrip()
        rule_match = rule_pattern.match(line)
        command_match = command_pattern.match(line)

        if rule_match:
            current_target, dependencies = rule_match.groups()
            if dependencies:
                rules[current_target]["dependencies"].extend(dependencies.split())
        elif command_match and current_target:
            command = command_match.group(1)
            rules[current_target]["commands"].append(command)

    return dict(rules)


# Example usage
