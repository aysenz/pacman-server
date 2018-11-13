from websocket_server import WebsocketServer
from components.game import Game
import json

class Main():
  server = WebsocketServer(13254, host='0.0.0.0')
  game = Game()
  def __init__(self):
    Main.server.set_fn_client_left(Main.client_left)
    Main.server.set_fn_message_received(Main.new_msg)
    Main.server.run_forever()
  @staticmethod
  def new_msg(client, server, message):
    try:
      message = json.loads(message)
    except ValueError as e:
      message = None
    if message != None:
      if message['cmd_type'] == 'connect_new_gamer':
        # {"cmd_type":"connect_new_gamer", "name": "ayzakh"}
        new_gamer = Main.game.connect_new_gamer(client['id'], message['name'])
        server.send_message(client, json.dumps({
          'cmd_type': 'all_positions',
          'positions': {
            'artifacts': Main.game.get_all_artifacts(),
            'heroes': Main.game.get_all_heroes()
          }
        }))
        server.send_message(client, json.dumps({ 'cmd_type': 'your_id', 'your_id': client['id'] }))
        server.send_message_to_all(json.dumps({
          'cmd_type': 'connect_new_gamer', 'name': message['name'], 'hero': new_gamer.__dict__
        }))
      elif message['cmd_type'] == 'move':
        # {"cmd_type":"move", "direction": "up"}
        move = Main.game.move(client['id'], message['direction'])
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
        new_artifacts = Main.game.artifact_manager.balance()
        for a in new_artifacts:
          Main.server.send_message_to_all(json.dumps({
            'cmd_type': 'create_artifact',
            'artifact': a
          }))
  @staticmethod
  def client_left(client, server):
    Main.game.disconnect_gamer(client['id'])
    server.send_message_to_all(json.dumps({
      'cmd_type': 'destroy_hero', 'hero_id': client['id']
    }))

Main()
