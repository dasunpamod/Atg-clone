# Atg-clone

A Python script that forward all messages from a target chat to a destination chat (work with user, group, supergroup and channel)

## Installation

- Install Python (tested with Python 3.7+)
- Download telethon
```shell
pip install telethon
```
- Clone this repository
- Insert your id and hash in the script (you can get one in my.telegram.org)
- Run the code with
```shell
python atg-clone.py
```
- PROFIT

## Simple guide
1. The script show you the opened chats
2. Choose the target chat
3. Choose the destination chat
4. Confirm 
5. If you want to continue a precendent forwarding insert the last message_id that you have forwarded
(so if you write 10000, the first message_id forwarded will be 10001)
6. Wait 3 sec (if something is wrong, this is the last moment before the script starts)
7. PROFIT

## Telegram limitation
- Telegram allow to forward 2000 msg per hour, after this limit you will get a FloodError and you have to wait. You can close the script and re-run when you want, just remember the last message forwarded

## Oh no, I can't remember the last message_id forwarded!
- If you can't remember the message_id of your last message forwarded, you can run the script 'finder.py' that search a specific string required via input

## Oh no, I have too much money!
If this project help you reduce time to develop, you can give me a can of Coke Zero :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](http://paypal.me/andrea8998)
