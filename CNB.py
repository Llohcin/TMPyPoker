#! /usr/bin/env python
# -*- coding:utf-8 -*-


import time
import json
from websocket import create_connection
import pprint

# pip install websocket-client
ws = ""

def takeAction(action, data):
    if action == "__bet":
        #time.sleep(2)
        ws.send(json.dumps({
            "eventName": "__action",
            "data": {
                "action": "bet",
                "playerName": "40930",
                "amount": 100
            }
        }))
    elif action == "__action":
        #time.sleep(2)
        ws.send(json.dumps({
            "eventName": "__action",
            "data": {
                "action": "call",
                "playerName": "40930"
            }
        }))


def doListen():
    try:
        global ws
        ws = create_connection("ws://10.104.65.33:3001/")
        ws.send(json.dumps({
            "eventName": "__join",
            "data": {
                "playerName": "40930"
            }
        }))
        while 1:
            result = ws.recv()
            msg = json.loads(result)
            event_name = msg["eventName"]
            data = msg["data"]
            print(event_name)
            pprint.pprint(data)
            print(data)
            takeAction(event_name, data)
    except Exception as e:
        print(e)
        ws.close()
        doListen()


if __name__ == '__main__':
    doListen()
