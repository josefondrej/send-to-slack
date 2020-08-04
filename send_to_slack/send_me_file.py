import os

import send_to_slack.load_credentials_to_env
from send_to_slack.send import send_file


def send_me_file(file_path: str):
    send_file(file_path=file_path, channel=os.environ["NOTIFY_ME_CHANNEL"])