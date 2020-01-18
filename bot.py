import os
import slack
from hewwwo import hewwwo
from creds.slackToken import botToken

counter = 0

@slack.RTMClient.run_on(event='message')
def quickTest(**message):
    global counter
    data = message['data']
    web = message['web_client']

    print(counter)
    print(data)
    if counter == 2:
        
        web.chat_postMessage(
            channel='the_finer_things',
            text=(hewwwo(data['text']))
        )
        counter = 0
    counter += 1

    

rtmClient = slack.RTMClient(token=botToken)
rtmClient.start()
