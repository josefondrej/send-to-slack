import os

from send_to_slack.send import send_text

_notify_me_channel_env = "NOTIFY_ME_CHANNEL"
notify_me_channel = os.environ[_notify_me_channel_env]


def notify_me(text: str):
    send_text(text, notify_me_channel)


if __name__ == '__main__':
    notify_me("Hey!")
