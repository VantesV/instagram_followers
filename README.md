# Script to see who doesn't follow you back on instagram

1. Clone this repository or copy the `instagram.py` file onto your computer.

2. Download a copy of your information on instagram by following this:
https://help.instagram.com/181231772500920#:~:text=Downloading%20a%20copy%20of%20your%20information . Choose JSON format.  You'll receive an email with the subject "Your Meta download request is in progress" and another one ~15 minutes later with the subject "Your Meta information download is ready".

3. Follow the download instructions in your email.

4. Once downloaded, navigate into `instagram-YOUR_NAME/followers_and_following` and copy 2 files (`followers_1.json` and `following.json`) into the same folder/directory that you saved `instagram.py` to.

5. In your terminal of choice, run
`python instagram.py` and it will create a text file showing the instagram names of those you follow that do not follow you back.