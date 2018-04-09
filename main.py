from fbchat import Client
from fbchat.models import *
client = Client('*******', '**********')

# client.send(Message(text='testing'), thread_id='1623960580995572', thread_type=ThreadType.GROUP)

client.sendLocalImage('friday.gif', thread_id='1623960580995572', thread_type=ThreadType.GROUP)

client.logout()