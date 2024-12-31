emoji_Convertor = {
    ':-)' : '😊',
    ';-)' : '😉',
    ':-(' : '😞',
    ':-D' : '😃',
    ':-P' : '😛',
    ':-*' : '😘',
    ':-O' : '😮',
}




message = str(input())
words = message.split(' ')
emoji = emoji_Convertor.get(words[-1])
if emoji :
   print(message[:-3] + emoji)
else:
   print(message)