# Atg-clone

A Python script that forward all messages from a target chat to a destination chat (work with user, group, supergroup and channel)

## When should I use it?
I used it to make a copy on cloud of a group with a lot of large files.  
With this script the forwarded files will be available also if the target close and you are kicked out. If you make a copy with a completly export of the chat with Telegram App you are forced to download the large files too, but with this script all files and the chat are saved via cloud in the destination

## Installation
Tested with Windows 10 and Linux Ubuntu
- Install Python (tested with Python 3.7+)
- Download *telethon*
```shell
pip install telethon
```
- Clone this repository
- Insert your id and hash in the script (you can get one in <https://my.telegram.org> - *Api development tools*)
- Run the code with
```shell
python atg-clone.py
```
- PROFIT

## Simple guide
Create a group where just you are the only component (or not, just create the destination chat and write a message so it become opened) 
1. Login with number and code (remeber to put the +xxx before your number)
2. The script show you the opened chats
3. Choose the target chat
4. Choose the destination chat
5. Confirm 
6. If you want to continue a precendent forwarding insert the last message_id that you have forwarded
(so if you write 10000, the first message_id forwarded will be 10001)
7. Wait 3 sec (if something is wrong, this is the last moment you can stop the script before it starts)
8. PROFIT

## Telegram limitation
Telegram allow to forward 2000 msg per hour, after this limit you will get a *FloodError* and you have to wait. You can close the script and re-run when you want, just remember the last message forwarded

## Oh no, I can't remember the last message_id forwarded!
If you can't remember the message.id of your last message forwarded, you can run the script *atg-clone-finder.py* that search a specific string required via input with
```shell
python atg-clone-finder.py
```

## Oh no, I have too much money!
If this project help you reduce time to develop, you can give me a can of Coke Zero :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](http://paypal.me/andrea8998)
