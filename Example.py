import socket
import threading
import random

# Define the game rules
rules = {
    ('rock', 'paper'): 'paper',
    ('rock', 'scissors'): 'rock',
    ('paper', 'rock'): 'paper',
    ('paper', 'scissors'): 'scissors',
    ('scissors', 'rock'): 'rock',
    ('scissors', 'paper'): 'scissors'
}

# Define the function that handles incoming connections
def handle_connection(conn, addr, player_name):
    print(f'{player_name} connected from {addr}')
    conn.sendall(b'Welcome to rock-paper-scissors!')
    while True:
        # Receive the player's choice
        data = conn.recv(1024)
        if not data:
            print(f'{player_name} disconnected')
            break
        choice = data.decode()
        print(f'{player_name} chose {choice}')
        # Choose a random option for the computer
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)
        print(f'Computer chose {computer_choice}')
        # Determine the winner
        if choice == computer_choice:
            result = 'tie'
        else:
            winner = rules[(choice, computer_choice)]
            if winner == choice:
                result = 'win'
            else:
                result = 'lose'
        # Send the result to the player
        conn.sendall(result.encode())
    conn.close()

# Define the function that starts the game
def start_game():
    # Create the server socket
    host = '127.0.0.1'
    port = 8000
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(2)
    print(f'Server listening on {host}:{port}')
    # Accept the first connection
    conn1, addr1 = server_sock.accept()
    t1 = threading.Thread(target=handle_connection, args=(conn1, addr1, 'Player 1'))
    t1.start()
    # Accept the second connection
    conn2, addr2 = server_sock.accept()
    t2 = threading.Thread(target=handle_connection, args=(conn2, addr2, 'Player 2'))
    t2.start()
    # Wait for the threads to finish
    t1.join()
    t2.join()
    server_sock.close()

# Start the game
if __name__ == '__main__':
    start_game()