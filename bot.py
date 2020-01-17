import os
import slack
from creds.slackToken import botToken

counter = 0

@slack.RTMClient.run_on(event='message')
def quickTest(**message):
    global counter
    # data = message['data']
    web = message['web_client']

    counter += 1
    print(counter)
    if counter == 2:
        web.chat_postMessage(
            channel='the_finer_things',
            text='UwU?'
        )
        counter = 0

    

rtmClient = slack.RTMClient(token=botToken)
rtmClient.start()
