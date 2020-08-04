import json
import os

file_path = os.path.abspath(__file__)
package_path = "\\".join(file_path.split("\\")[:-2])
package_path = package_path.replace("\\", "/")

with open(f"{package_path}/credentials/credentials.json", "r") as credentials_file:
    credentials = json.load(credentials_file)

os.environ["SLACK_BOT_TOKEN"] = credentials["slack-bot-token"]
os.environ["NOTIFY_ME_CHANNEL"] = credentials["channel"]
