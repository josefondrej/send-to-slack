import json
import os

file_path = os.path.abspath(__file__)
package_path = "\\".join(file_path.split("\\")[:-2])
package_path = package_path.replace("\\", "/")

with open(f"{package_path}/credentials/credentials.json", "r") as credentials_file:
    credentials = json.load(credentials_file)

os.environ["SLACK_BOT_TOKEN"] = credentials["slack-bot-token"]
os.environ["NOTIFY_ME_CHANNEL"] = credentials["channel"]

from send_to_slack.send_me import notify_me


class SlackLogger:
    def __init__(self, send_to_slack: bool = True, print_to_console: bool = True):
        self._send_to_slack = send_to_slack
        self._print_to_console = print_to_console

    def message(self, text: str, send_to_slack: bool = None, print_to_console: bool = None):
        send_to_slack = send_to_slack if send_to_slack is not None else self._print_to_console
        print_to_console = print_to_console if print_to_console is not None else self._print_to_console

        if print_to_console:
            print(text)

        if send_to_slack:
            notify_me(text)

    def debug(self, text: str):
        message = f"[DEBUG] {text}"
        self.message(message)

    def info(self, text: str):
        message = f"[INFO] {text}"
        self.message(message)

    def warn(self, text: str):
        message = f"[WARN] {text}"
        self.message(message)

    def error(self, text: str):
        message = f"[ERROR] {text}"
        self.message(message)


if __name__ == '__main__':
    log = SlackLogger()
    log.info("Hey")
