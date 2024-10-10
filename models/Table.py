"""
Authors:
- Iván Maldonado (Kikemaldonado11@gmail.com)
- Maria José Vera (nandadevi97816@gmail.com)
- Sergio Fernández (sergiofnzg@gmail.com)

Developed at: October 2024
"""

class Table:
    def __init__(self, _id):
        self.id = _id
        self.game_board = [' ' for _ in range(9)]
        self.available = True
        self.players = []
        self.player_sockets = {}
        self.winner = None
        self.turn = 'X'  
    
    
    def add_player(self, player_id, websocket):
        """Add a player and store their WebSocket."""
        if len(self.players) < 2:
            self.players.append(player_id)
            self.player_sockets[player_id] = websocket
            
        # Table becomes unavailable when full
            
        if len(self.players) == 2:
            self.available = False  
            

    def make_move(self, index, player_turn):
        """Make a move at the given index if the cell is empty."""
        if self.game_board[index] == ' ':
            self.game_board[index] = player_turn
            # Switch the turn to the other player
            self.turn = 'O' if player_turn == 'X' else 'X'
        

    def check_winner(self):
        pass