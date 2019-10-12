# Slack Command Trigger (Evernote)

Automatically clip multiple channels over a range of days and from Slack into Evernote using the Web API. Options to clip yesterday, the last week, or the last month. Requires a legacy API token.

## install
	
install slacker
`pip install slacker`

install npm

## request a legacy API token
1. Generate a legacy token at: https://api.slack.com/custom-integrations/legacy-tokens
2. edit `index.py` and insert the token for `apiKey` at the top of the file.

    npm install
    <or>
    npm i

## running
with no arguments, it will clip yesterday's messages.

    npm start

    <or>
    
    python index.py



## options

* -w, --week =>  - clip the last week of messages (minus today).
* -m, --month =>  - clip the last month of messages (minus today).
* ~~-t, --token => String - Your Slack API-token~~
* ~~-cmd, --command => String - The slash command you want to use~~
* ~~-c, --channel => String - The channel you want to post to~~
* ~~-i, --instruction => String - all the text following your slash-command~~

## example
To clip yesterday's messages:
`python index.py`

To clip the last week of messages (minus today):
`python index.py --week`

To clip the last month of messages (minus today):
`python index.py --month`
