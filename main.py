import os
import threading
import requests, random
from dhooks import Webhook
from discordwebhook import Discord
import ctypes
import time


def groupfinder():
	id = random.randint(1000000, 17000000)
	r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}")
	if 'owned' not in r.text:
		re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
		if 'isLocked' not in re.text and 'owner' in re.text:
			if re.json()['publicEntryAllowed'] == True and re.json(
			)['owner'] == None:
				hook.send(
				    f'```Hit: https://www.roblox.com/groups/group.aspx?gid={id}```')
				print(f"[+] Hit: {id}")
			else:
				print(f"[-] No Entry Allowed: {id}")
		else:
			print(f"[-] Group Locked: {id}")
	else:
		print(f"[-] Group Already Owned: {id}")


print("""


____ _    ____ _  _ ____    ____ ____ ____ _  _ ___  
|__| |    |___ |_/  [__     | __ |__/ |  | |  | |__] 
|  | |___ |___ | \_ ___]    |__] |  \ |__| |__| |    

____ _ _  _ ___  ____ ____ 
|___ | |\ | |  \ |___ |__/ 
|    | | \| |__/ |___ |  \ 

""")

#your webhook
hook = Webhook("https://discord.com/api/webhooks/1165743537195864144/0XibC_vOPCxAqgEMVOy6GfoNGwPXPZ1solizy8T3dlcAVUnpUNe49qqGhuQ8MKHRjIbM")
threads = int(input("[-] How many threads: "))
hook.send("'```[+] Starting Group Finder'```")

while True:
	time.sleep(0.5)
	if threading.active_count() <= threads:
		threading.Thread(target=groupfinder).start()
