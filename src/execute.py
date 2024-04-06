import subprocess
from subprocess import CalledProcessError, SubprocessError, TimeoutExpired


class ExecuteCommand:
    successful = False
    exit_code = -1
    stdout = ""
    stderr = ""
    timeout_expired = False

    def __init__(self, command: str, timeout=5):
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                shell=True,
                timeout=timeout,
                text=True,
                check=True,
            )

            self.exit_code = result.returncode
            self.stdout = result.stdout
            self.stderr = result.stderr

            self.successful = True
        except TimeoutExpired:
            self.timeout_expired = True
        except CalledProcessError as e:
            self.exit_code = e.returncode
            self.stdout = e.stdout
            self.stderr = e.stderr
        except SubprocessError as err:
            self.exit_code = 1
            self.stderr = str(err)
        except Exception as err:
            self.exit_code = 1
            self.stderr = f"Unexpected error: {err}"
