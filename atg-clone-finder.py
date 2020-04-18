from telethon import TelegramClient
from telethon.errors import FloodWaitError
import time
import datetime


# Use your own values from my.telegram.org
api_id = your id here
api_hash = your api here

client = TelegramClient('anon', api_id, api_hash)

async def main():
    print('Here are your opened chat:')
    
    i = 0;
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(i, ':' , dialog.name, 'has ID', dialog.id)
        i = i + 1

    confirm = False
    max = len(dialogs) - 1
    
    while (confirm == False):
        target_index = -1
        
        #Get target chat
        while (target_index < 0 or target_index > max):
            print('Please insert target between 0 and', max)
            target_index = int(input())
            if (target_index < 0 | target_index > max ):
                print('Target out of range')
        
        target = dialogs[target_index]
        print('Target is', target.name, 'with ID', target.id)
        
        #Wait for confirm
        print('Correct? Y/N')
        reply = input()[0]
        if (reply == 'Y' or reply == 'y'):
            confirm = True
    
    print('Insert string to search:')
    string_search = input()
    
    print('Start searching', string_search, 'from', target.name, 'in 3 sec...')
    #If you made some mistake with target and destination, this is the last time you can Ctrl-c
    time.sleep(3)
    
    target_entity = await client.get_entity(target.id)
    
    find_n = 0
    error_n = 0
    
    async for message in client.iter_messages(target_entity, reverse = True, wait_time = 1, search = string_search):            
        try:
            print(message.id, ':', message.text)
            find_n = find_n + 1
        except Exception as e2:
            print('Error msg', message.id, ':', message.text, '. CAUSE:', e2)
            error_n = error_n + 1
            
    print('Find error:', error_n)
    print('Find correctly from', target.name, ':', find_n)

with client:
    client.loop.run_until_complete(main())
