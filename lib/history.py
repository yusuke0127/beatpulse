import csv
import os
from lib.base import Base

class History(Base):
    def __init__(self) -> None:
        pass

    
    @classmethod
    def list(cls) -> list:
        """List all tracks in the history."""
        tracks = []            
        file_path = os.path.join("data", "history.csv")
        if not os.path.exists(file_path):
            os.makedirs("data")
            with open(file_path, "w") as new_file:
                pass
        
        try:
            with open(file_path) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tracks.append({
                        "title": row["title"],
                        "uri": row["uri"], 
                        "artists": row["artists"],
                        "tempo": row["tempo"], 
                        "time_signature": row["time_signature"],
                        })
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            
        tracks.reverse()
        return tracks
    
    
    def write(self, track:object) -> None:
        """Write a track to the history."""
        if not os.path.exists("data"):
            os.makedirs("data")
        
        file_path = os.path.join("data", "history.csv")
        try:
            with open(file_path, "a") as file:
                writer = csv.DictWriter(file, fieldnames=["title", "uri", "artists", "tempo", "time_signature"])
                if super().empty_file(file_path):
                    writer.writeheader()
                writer.writerow({
                    "title": track.title, 
                    "uri": track.uri, 
                    "artists": ','.join(track.artists),
                    "tempo": track.tempo,
                    "time_signature": track.time_signature
                })
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            
        return None

    @classmethod
    def clear(cls) -> None:
        """Clear the history file."""
        file_path = os.path.join("data", "history.csv")
        try:
            with open(file_path, "w") as file:
                file.truncate()
        except Exception as e:
            print(f"An error occurred while clearing the file: {e}")
        
        return None
