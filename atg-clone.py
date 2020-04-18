from telethon import TelegramClient
from telethon.errors import FloodWaitError
import time
import datetime


# Use your own values from my.telegram.org
api_id = your id here
api_hash = your hash here

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
        destination_index = -1
        
        #Get target chat
        while (target_index < 0 or target_index > max):
            print('Please insert target between 0 and', max)
            target_index = int(input())
            if (target_index < 0 | target_index > max ):
                print('Target out of range')
        
        target = dialogs[target_index]
        print('Target is', target.name, 'with ID', target.id)
        
        #Get destination chat
        while (destination_index < 0 or destination_index > max):
            print('Please insert destination between 0 and', max)
            destination_index = int(input())
            if (destination_index < 0 | destination_index > max ):
                print('Destination out of range')
        
        destination = dialogs[destination_index]
        print('Destination is', destination.name, 'with ID', destination.id)
        
        #Wait for confirm
        print('Correct? Y/N')
        reply = input()[0]
        if (reply == 'Y' or reply == 'y'):
            confirm = True
        
        
    print('Do you want to continue a precedent forwarding? Please insert last message.id forwarded (BASE: 0)')
    start_from = 0
    start_from = int(input())
     
    print('Start forwarding from', target.name, 'to', destination.name, 'in 3 sec...')
    #If you made some mistake with target and destination, this is the last time you can Ctrl-Z
    time.sleep(3)
    
    target_entity = await client.get_entity(target.id)
    destination_entity = await client.get_entity(destination.id)
    forwarded_n = 0
    error_n = 0
    
    async for message in client.iter_messages(target_entity, reverse = True, min_id = start_from, wait_time = 1 ):            
        try:
            await client.forward_messages(destination_entity, message)
            forwarded_n = forwarded_n + 1
            print('Message', message.id, 'forwarded! Total forwarded:', forwarded_n, 'Total errors:', error_n)  
        except FloodWaitError as e:
            print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), 'FLOAD ERROR DETECT! WE MUST WAIT', e.seconds, 'seconds until next forward')
            print('You can exit with Ctrl-c, just remember that if you want to continue forwarding your last message tried to forward is', message.id - 1)

            time.sleep(e.seconds + 10)
            
            #After e.seconds time (and more) of waiting we retry to forward the message (sorry I can't find a better solution)
            #In case of another fail (for example because we can't forward this kind of message) we don't care and continue
            #Another flood exception should not happen, and we can't do anything with exception that are not a flood exception
            try:
                await client.forward_messages(destination_entity, message)
                forwarded_n = forwarded_n + 1
                print('Message', message.id, 'forwarded! Total forwarded:', forwarded_n, 'Total errors:', error_n)
            except Exception as e1:
                print('Error forwarding msg', message.id, ':', message.text, '. CAUSE:', e1)
                error_n = error_n + 1
        #This is to catch other exception that are not a flood exception
        except Exception as e2:
            print('Error forwarding msg', message.id, ':', message.text, '. CAUSE:', e2)
            error_n = error_n + 1
            
    print('Forwarded error:', error_n)
    print('Forwarded correctly from', target.name, 'to', destination.name, ':', forwarded_n)

with client:
    client.loop.run_until_complete(main())
