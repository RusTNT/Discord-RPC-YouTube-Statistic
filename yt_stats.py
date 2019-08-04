import os, sys, logging, json, time, re, asyncio, discord, requests, locale
from pypresence import Presence
from datetime import datetime, date


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
'en_US.UTF-8'
CLIENT_ID = '605856430007910494'
RPC = Presence(CLIENT_ID)
RPC.connect()


clear = lambda: os.system('cls')
clear()


def discord_stats_from_yt(url=None):
    if not url:
        url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC_2_qvYrULTjpBVLDGce8aQ&key=AIzaSyBU_oWEIULi3-n96vWKETYCMsldYDAlz2M"
    else:
        url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + url + "&key=AIzaSyBU_oWEIULi3-n96vWKETYCMsldYDAlz2M"
    prev_title = ""
    start_time = int(time.time())
    while True:
        time.sleep(5)
        try:

            r = requests.get(url).json()
            count = r.get("items", [{}])[0].get('statistics', {}).get("subscriberCount", 0)
            count = locale.format('%d', int(count), grouping=True)

            countview = r.get("items", [{}])[0].get('statistics', {}).get("viewCount", 0)
            countview = locale.format('%d', int(countview), grouping=True)
            title = "Sub's " + count
            details = "View's " + countview
            if title != prev_title:
                prev_title = title
                start_time = int(time.time())
            RPC.update(
                details=title,
                state=details,
                start=start_time,
                large_image="ava"
            )
        except:
            pass


if __name__ == "__main__":
    url = input("Input ChannelID: ")
    discord_stats_from_yt(url)
