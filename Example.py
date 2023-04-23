import socket
import threading
import tkinter 

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
def handle_connection(conn, addr, choice, player_name):
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

        #Game decision
        if len(choice) > 1:
            
                                                            # Choose a random option for the computer
                                                            #options = ['rock', 'paper', 'scissors']
                                                            #computer_choice = random.choice(options)
                                                            #print(f'Computer chose {computer_choice}')
            # Determine the winner
            if choice[0] == choice[1]:
                conn.sendall('Tie')
            else:
                winner = rules[(choice[0], choice[1])]
                if winner == choice[0]:
                    conn.sendall('Winner is' + choice[0])
                else:
                    conn.sendall('Winner is' + choice[1])
    conn.close()

# Define the function that starts the game
def start_game():
    # Create the server socket
    host = '127.0.0.1'
    port = 5450
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(2)
    print(f'Server listening on {host}:{port}')
    # Accept the first connection
    conn1, addr1 = server_sock.accept()
    choice1=input('Player 1, please choose rock, paper, or scissors: ')
    t1 = threading.Thread(target=handle_connection, args=(conn1, addr1, choice1, 'Player 1'))
    t1.start()
    # Accept the second connection
    conn2, addr2 = server_sock.accept()
    choice2=input('Player 2, please choose rock, paper, or scissors: ')
    t2 = threading.Thread(target=handle_connection, args=(conn2, addr2, choice2, 'Player 2'))
    t2.start()
    # Wait for the threads to finish
    t1.join()
    t2.join()
    server_sock.close()

# Start the game
if __name__ == '__main__':
    start_game()