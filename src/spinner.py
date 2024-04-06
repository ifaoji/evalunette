import functools
import itertools
import threading
from typing import Optional

from src.color import Color

_spinners = {
    "dots": {
        "interval": 80,
        "frames": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
    }
}


class Spinner:
    _interval: int
    _cycle: list[str]

    _thread: Optional[threading.Thread] = None
    _stop_event: Optional[threading.Event] = None

    _status_message_count = 0
    _status_message: Optional[str] = None

    _done_message: Optional[str] = None

    def __init__(
        self,
        text: str,
        spinner: str = "dots",
        status_message: Optional[str] = None,
        done_message: Optional[str] = None,
    ):
        self._text = text
        self._interval = _spinners[spinner]["interval"]
        self._cycle = itertools.cycle(_spinners[spinner]["frames"])
        self._status_message = status_message
        self._done_message = done_message

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            with self:
                return fn(*args, **kwargs)

        return wrapped

    def start(self):
        if self._thread is not None:
            return

        self._status_message_count = 0
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._spin)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        if self._thread is None:
            return

        self._stop_event.set()
        self._thread.join()

        self._thread = None
        self._stop_event = None

        self._clear_line()

        self._print_done_message()

    def status_message(self, message: str):
        if self._status_message == message:
            self._status_message_count += 1
            return

        self._status_message_count = 1
        self._status_message = message

    def _print_done_message(self):
        if not self._done_message:
            return

        print(f"{Color.green('✔')} {self._done_message}")

    def _spin(self):
        try:
            self._hide_cursor()

            while not self._stop_event.is_set():
                frame = next(self._cycle)

                print(f"\r{Color.cyan(frame)} {self._text}", end="")

                if self._status_message:
                    print(f" {self._status_message}", end="")

                if self._status_message_count > 1:
                    print(f" ({self._status_message_count}x)", end="")

                self._stop_event.wait(self._interval / 1000)

        finally:
            self._show_cursor()

    def _hide_cursor(self):
        if self._hide_cursor:
            print("\033[?25l", end="")

    def _show_cursor(self):
        print("\033[?25h", end="")

    def _clear_line(self):
        print("\r\033[K", end="")
