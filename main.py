#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402


host = "localhost"
port = 4444
password = "secret"

ws = obsws(host, port, password)
ws.connect()

try:
    scenes = ws.call(requests.GetSceneList())
    for s in scenes.getScenes():
        name = s['name']
        print("\n"+name+"\n")
        ws.call(requests.PauseRecording())
        time.sleep(2)
        ws.call(requests.ResumeRecording())

    print("End of list")

except KeyboardInterrupt:
    pass

ws.disconnect()
