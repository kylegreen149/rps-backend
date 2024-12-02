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


>> """
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
            print("Enter a number from 1-4 only.")

def signUp():
    enter_username = input("Enter a username to play with: ")
    if enter_username != "":
        stats = {
            "games": 0,
            "wins": 0,
            "losses": 0,
            "ties": 0,
            "longest_win_streak": 0,
            "longest_losing_streak": 0,
            "win_pct": 0.0,
            "loss_pct": 0.0,
            "ties_pct": 0.0,
            "rock_picks": 0,
            "paper_picks": 0,
            "scissors_picks": 0
        }
        play_rps(enter_username, stats)
    else:
        print("Please enter a valid username!")
        enter_username = input("Enter a username to play with: ")


def get_user_stats(username):
    # Connect to the database
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()

    # Execute the SQL query to find the user
    cursor.execute("SELECT * FROM leaderboard WHERE username = ?", (username,))
    user_stats = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Check if user was found and return stats
    if user_stats:
        return user_stats
    else:
        print("Username not found.")
        return None

def signIn():
    enter_username = input("Enter an existing username to continue playing: ")
    user_stats = get_user_stats(enter_username)
    if user_stats:
        play_rps(enter_username, user_stats)
    else:
        print("Make sure you are entering a username that already exist!")
        enter_username = input("Enter an existing username to continue playing: ")


def show_leaderboard():
    pass

def play_rps(username, stats):
    print("Welcome back,", username, "!")
    print("Here are your stats:")
    print(stats)

home_screen()