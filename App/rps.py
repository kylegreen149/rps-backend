import random
import sqlite3

# Creates connection to leaderboard database
conn = sqlite3.connect('leaderboard.db')

def create_leaderboard():
    sql = """
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY,
            username TEXT,
            games INTEGER,
            wins INTEGER,
            losses INTEGER,
            ties INTEGER,
            longest_win_streak INTEGER,
            longest_losing_streak INTEGER,
            win_pct REAL,
            loss_pct REAL,
            ties_pct REAL,
            rock_picks INTEGER,
            paper_picks INTEGER,
            scissors_picks INTEGER 
        )
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def add_to_leaderboard(username, games, wins, losses, ties, longest_win_streak, longest_losing_streak, win_pct, loss_pct, ties_pct, rock_picks, paper_picks, scissors_picks):
    """Adds player stats to leaderboard database"""
    sql = """
        INSERT INTO leaderboard (username, games, wins, losses, ties, longest_win_streak, longest_losing_streak, win_pct, loss_pct, ties_pct, rock_picks, paper_picks, scissors_picks)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(sql, [username, games, wins, losses, ties, longest_win_streak, longest_losing_streak, win_pct, loss_pct, ties_pct, rock_picks, paper_picks, scissors_picks])
    conn.commit()

def home_screen():
    while True:
        prompt = """Rock Paper Scissors (Advanced Edition)
        Play the classic Rock Paper Scissors game with advanced user stats!!

        How to play:
        When the prompt comes up, correctly type the words "rock", "paper", or "scissors"
        That's it!!

        Select an option:
        1. Sign up as a new player
        2. Continue progress as an existing player
        3. See Leaderboard
        4. Quit


        >>"""
        option = input(prompt)
        if option == "1":
            signUp()
        elif option == "2":
            signIn()
        elif option == "3":
            show_leaderboard()
        elif option == "4": 
            print("Closing game... Come back soon!")
            exit()
        else:
            print("Enter a number from 1-3 only.")

def signUp():
    enter_username = input("Enter a username to play with: ")
    play_rps(enter_username)

def signIn():
    pass

def show_leaderboard():
    pass

def play_rps(username):
    pass