from datetime import datetime

import send_to_slack.load_credentials_to_env
from send_to_slack.send_me import notify_me


class SlackLogger:
    def __init__(self, send_to_slack: bool = True, print_to_console: bool = True):
        self._send_to_slack = send_to_slack
        self._print_to_console = print_to_console

    def message(self, level: str, text: str, send_to_slack: bool = None, print_to_console: bool = None):
        send_to_slack = send_to_slack if send_to_slack is not None else self._send_to_slack
        print_to_console = print_to_console if print_to_console is not None else self._print_to_console

        text = f"[{level}] {str(datetime.now())}:\t {text}"

        if print_to_console:
            print(text)

        if send_to_slack:
            notify_me(text)

    def debug(self, text: str):
        self.message("DEBUG", text)

    def info(self, text: str):
        self.message("INFO", text)

    def warn(self, text: str):
        self.message("WARN", text)

    def error(self, text: str):
        self.message("ERROR", text)


if __name__ == '__main__':
    log = SlackLogger()
    log.info("Hey")
