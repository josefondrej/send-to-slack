from send_to_slack.send_file import send_file

if __name__ == '__main__':
    file_path = "C:/Temp/file"
    channel = "@josef.ondrej"
    response = send_file(file_path, channel)
