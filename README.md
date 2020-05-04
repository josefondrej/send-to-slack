Send to Slack
=============
Set of utility functions for sending files and plots from python directly to slack.

### Prerequisities
1. You need to install requirements. From the `send-to-slack` directory run: 
    ```
    python -m pip install -r requirements.txt
    ```
1. You need to create a slack app at https://api.slack.com/apps, add it to your workspace, set the app's permissions 
so it can send files and add it to the channels you want to use it in.    
1. You need to set the environemental variable `SLACK_BOT_TOKEN` to the token you obtain from https://api.slack.com/apps > Your App > OAuth & Permissions. 
The token should look like something like 
    ```
    xoxb-1234567891011-1213141516171-AbCDEFGhijklmnOPQRSTuVWx
    ```   
1. Then you can import the library in your project and use it like 
    ```python
    from send_to_slack.send_file import send_file
    
    file_path = "C:/Temp/test_file.txt"
    channel = "#general"
    send_file(file_path=file_path, channel=channel)
    
    ```   