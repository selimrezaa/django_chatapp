import json
from time import sleep

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep 


from asgiref.sync import async_to_sync
from .models import *

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("websocket connected...", event)
        groupName = self.scope['url_route']['kwargs']['groupkanam']
        print("groupname.......", groupName)
        async_to_sync(self.channel_layer.group_add)(groupName, self.channel_name)
        self.send({
          'type': 'websocket.accept',
        })
    
    def websocket_receive(self, event):
      # abcd = json.loads(event)
      # print("type json loads.....", type(abcd))


      groupName = self.scope['url_route']['kwargs']['groupkanam']
      async_to_sync(self.channel_layer.group_send)(
        groupName, 
        {
        'type':'chat.message',
        'text':event['text']
        }
      )

    def chat_message(self, event):
      print("data:...", event['text'])
      print("type.......", type(event))
      self.send({
        'type': 'websocket.send',
        'text': event['text']
      })
     
    
    def websocket_disconnect(self, event):
        print("websocket disconnected...",event)
        raise StopConsumer()