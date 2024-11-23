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
