import io
import os
from typing import Optional

import requests

_slack_bot_token_env = "SLACK_BOT_TOKEN"
_file_api_endpoint = "https://slack.com/api/files.upload"
_message_api_endpoint = "https://slack.com/api/chat.postMessage"

try:
    _bot_token = os.environ[_slack_bot_token_env]
except:
    raise ValueError(
        f"You must set the environmental variable {_slack_bot_token_env} to your slack bot token which you can find at https://api.slack.com/.")


def send_text(text: str, channel: str) -> requests.Response:
    headers = {
        "Authorization": f"Bearer {_bot_token}",
    }

    message = {
        "channel": channel,
        "text": text
    }

    response = requests.post(_message_api_endpoint, data=message, headers=headers)
    return response


def send_bytes(file: io.BufferedReader, channel: str, file_name: Optional[str] = None, comment: Optional[str] = None,
               file_type: Optional[str] = None) -> requests.Response:
    if file_name is None:
        file_name = "Unnamed file."

    headers = {
        "Authorization": f"Bearer {_bot_token}",
    }

    files = {
        "file": (file_name, file),
        "initial_comment": (None, comment),
        "channels": (None, channel),
    }

    if file_type is not None:
        files["file_type"] = file_type

    response = requests.post(_file_api_endpoint, headers=headers, files=files)
    return response


def send_file(file_path: str, channel: str, comment: Optional[str] = None) -> requests.Response:
    file_name = file_path.split("/")[-1]
    if comment is None:
        comment = f"Sending file `{file_name}`."
    with open(file_path, "rb") as file:
        response = send_bytes(file=file, channel=channel, file_name=file_name, comment=comment)
        return response


def plot_to_slack(channel: str, plot_name: Optional[str] = None, comment: Optional[str] = None,
                  format: str = "pdf") -> requests.Response:
    if plot_name is None:
        plot_name = "Unnamed figure."

    buffer = io.BytesIO()
    plt.savefig(buffer, format=format)
    buffer.seek(0)

    response = send_bytes(file=buffer, channel=channel, file_name=plot_name, comment=comment)
    return response


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    channel = "#general"  # alternatively use "@user.name"

    # Test plot to slack
    n_obs = 200
    plt.scatter(np.random.randn(n_obs), np.random.randn(n_obs), alpha=0.5, color="deepskyblue")
    plt.title("Scatterplot")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.grid()
    response = plot_to_slack(channel)

    # Test sending file from disk
    file_path = "files/test.txt"
    response = send_file(file_path, channel)
