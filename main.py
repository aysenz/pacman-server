import logging
from websocket_server import WebsocketServer
from components.game import Game
from uuid import UUID
import json

server = WebsocketServer(13254, host='0.0.0.0', loglevel=logging.INFO)
game = Game()

def new_msg(client, server, message):
  try:
    message = json.loads(message)
  except ValueError as e:
    message = None
  if message != None:
    if message['cmd_type'] == 'connect_new_gamer':
      # {"cmd_type":"connect_new_gamer", "name": "ayzakh"}
      new_gamer = game.connect_new_gamer(client['id'], message['name'])
      server.send_message(client, json.dumps({
        'cmd_type': 'all_positions',
        'positions': {
          'artifacts': game.get_all_artifacts(),
          'heroes': game.get_all_heroes()
        }
      }))
      server.send_message(client, json.dumps({ 'cmd_type': 'your_id', 'your_id': client['id'] }))
      server.send_message_to_all(json.dumps({
        'cmd_type': 'connect_new_gamer', 'name': message['name'], 'hero': new_gamer.__dict__
      }))
    elif message['cmd_type'] == 'move':
      # {"cmd_type":"move", "direction": "up"}
      move = game.move(client['id'], message['direction'])
      if move['eat'] != None:
        if move['eat'].__class__.__name__ == 'Artifact':
          server.send_message_to_all(json.dumps({
            'cmd_type': 'destroy_artifact', 'artifact_id': int(move['eat'].id)
          }))
        # elif move['eat'].__class__.__name__ == 'Hero':
        #   server.send_message_to_all(json.dumps({
        #     'cmd_type': 'destroy_hero', 'hero_id': client['id']
        #   }))
      # if type(move['eat']) == None: del move['eat']
      server.send_message_to_all(json.dumps({
        'cmd_type': 'destroy_hero', 'hero_id': client['id']
      }))
      server.send_message_to_all(json.dumps({
        'cmd_type': 'move', 'hero_id': client['id'], 'position': { 'x': move['x'], 'y': move['y'], 'diameter': move['diameter'] }
      }))
def client_left(client, server):
  game.disconnect_gamer(client['id'])
  server.send_message_to_all(json.dumps({
    'cmd_type': 'destroy_hero', 'hero_id': client['id']
  }))


server.set_fn_client_left(client_left)
server.set_fn_message_received(new_msg)
server.run_forever()