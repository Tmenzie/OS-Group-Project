import socket
import threading
import sys
import tkinter as tk
from tkinter import messagebox

class ServerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Rock Paper Scissors Server')
        self.geometry('400x400')
        self.status = tk.Label(self, text='Server has not been started', font=('Arial', 12))
        self.status.pack(pady=10)
        self.start_btn = tk.Button(self, text='Start Server', font=('Arial', 12), command=self.start_server)
        self.start_btn.pack(pady=10)
        self.quit_btn = tk.Button(self, text='Quit', font=('Arial', 12), command=self.quit)
        self.quit_btn.pack(pady=10)
        
    def start_server(self):
        try:
            self.server = RockPaperScissorsServer(self)
            self.status.config(text='Server has been started', fg='green')
            self.start_btn.config(text='Server is running', state='disabled')
        except Exception as e:
            messagebox.showerror('Error', f'Error starting server: {e}')

class RockPaperScissorsServer:
    def __init__(self, gui):
        self.gui = gui
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('127.0.0.1', 54450))
        self.socket.listen(2)
        self.active = True
        self.start_game()

    def start_game(self):
        while self.active:
            try:
                player1, addr1 = self.socket.accept()
                player2, addr2 = self.socket.accept()
                threading.Thread(target=self.play_game, args=(player1, player2)).start()
            except:
                self.active = False
                self.gui.status.config(text='Server has been stopped', fg='red')
                self.gui.start_btn.config(text='Start Server', state='normal')

    def play_game(self, player1, player2):
        self.send_message(player1, 'NEW_1')
        self.send_message(player2, 'NEW_2')
        player1_choice = ''
        player2_choice = ''
        while not self.has_winner(player1_choice, player2_choice):
            self.send_message(player1, 'START')
            player1_choice = self.get_choice(player1)
            self.send_message(player2, 'START')
            player2_choice = self.get_choice(player2)
        winner = self.get_winner(player1_choice, player2_choice)
        if winner == 0:
            self.send_message(player1, 'TIE')
            self.send_message(player2, 'TIE')
        elif winner == 1:
            self.send_message(player1, 'WIN')
            self.send_message(player2, 'LOSE')
        else:
            self.send_message(player1, 'LOSE')
            self.send_message(player2, 'WIN')
        player1.close()
        player2.close()

    def has_winner(self, choice1, choice2):
        return choice1.startswith('CHOICE_') and choice2.startswith('CHOICE_')

    def get_choice(self, player):
        while True:
            choice = player.recv(1024).decode()
            if choice.startswith('CHOICE_'):
                return choice

    def get_winner(self, choice1, choice2):
        if (choice1 == 'CHOICE_ROCK' and choice2 == 'CHOICE_SCISSORS') or \
           (choice1 == 'CHOICE_PAPER' and choice2 == 'CHOICE_ROCK') or \
           (choice1 == 'CHOICE_SCISSORS' and choice2 == 'CHOICE_PAPER'):
            return
