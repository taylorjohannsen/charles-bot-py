import os
import slack
from creds.slackToken import botToken

counter = 0

@slack.RTMClient.run_on(event='message')
def quickTest(**message):
    global counter
    data = message['data']
    web = message['web_client']

    counter += 1
    print(counter)
    if counter is 5:
        web.chat_postMessage(
            channel='testing',
            text='You called 5 times!'
        )
        counter = 0

    

rtmClient = slack.RTMClient(token=botToken)
rtmClient.start()
