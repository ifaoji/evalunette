class Color:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    LIGHTBLACK = "\033[90m"
    LIGHTRED = "\033[91m"
    LIGHTGREEN = "\033[92m"
    LIGHTYELLOW = "\033[93m"
    LIGHTBLUE = "\033[94m"
    LIGHTMAGENTA = "\033[95m"
    LIGHTCYAN = "\033[96m"
    LIGHTWHITE = "\033[97m"
    RESET = "\033[0m"

    # Style codes
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    INVERTED = "\033[7m"

    @classmethod
    def black(cls, text):
        return f"{cls.BLACK}{text}{cls.RESET}"

    @classmethod
    def red(cls, text):
        return f"{cls.RED}{text}{cls.RESET}"

    @classmethod
    def green(cls, text):
        return f"{cls.GREEN}{text}{cls.RESET}"

    @classmethod
    def yellow(cls, text):
        return f"{cls.YELLOW}{text}{cls.RESET}"

    @classmethod
    def blue(cls, text):
        return f"{cls.BLUE}{text}{cls.RESET}"

    @classmethod
    def magenta(cls, text):
        return f"{cls.MAGENTA}{text}{cls.RESET}"

    @classmethod
    def cyan(cls, text):
        return f"{cls.CYAN}{text}{cls.RESET}"

    @classmethod
    def white(cls, text):
        return f"{cls.WHITE}{text}{cls.RESET}"

    @classmethod
    def lightblack(cls, text):
        return f"{cls.LIGHTBLACK}{text}{cls.RESET}"

    @classmethod
    def lightred(cls, text):
        return f"{cls.LIGHTRED}{text}{cls.RESET}"

    @classmethod
    def lightgreen(cls, text):
        return f"{cls.LIGHTGREEN}{text}{cls.RESET}"

    @classmethod
    def lightyellow(cls, text):
        return f"{cls.LIGHTYELLOW}{text}{cls.RESET}"

    @classmethod
    def lightblue(cls, text):
        return f"{cls.LIGHTBLUE}{text}{cls.RESET}"

    @classmethod
    def lightmagenta(cls, text):
        return f"{cls.LIGHTMAGENTA}{text}{cls.RESET}"

    @classmethod
    def lightcyan(cls, text):
        return f"{cls.LIGHTCYAN}{text}{cls.RESET}"

    @classmethod
    def lightwhite(cls, text):
        return f"{cls.LIGHTWHITE}{text}{cls.RESET}"

    # Style methods
    @classmethod
    def bold(cls, text):
        return f"{cls.BOLD}{text}{cls.RESET}"

    @classmethod
    def italic(cls, text):
        return f"{cls.ITALIC}{text}{cls.RESET}"

    @classmethod
    def underline(cls, text):
        return f"{cls.UNDERLINE}{text}{cls.RESET}"

    @classmethod
    def blink(cls, text):
        return f"{cls.BLINK}{text}{cls.RESET}"

    @classmethod
    def inverted(cls, text):
        return f"{cls.INVERTED}{text}{cls.RESET}"
