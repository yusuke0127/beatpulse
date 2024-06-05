# from track import Track
import os
import csv
from lib.base import Base

class Playlist(Base):
    def __init__(self) -> None:
        self.playlists_dir = os.path.join("data", "playlists")
        os.makedirs(self.playlists_dir, exist_ok=True)
    
    def create(self, songs:list, name:str) -> None:
        """Create a new playlist with the given songs."""
        
        playlists = Playlist.list()
        if name in playlists:
            print("name checker")
            return f"{name} already exists!"
        
        filename = f"{name}.csv"
        file_path = os.path.join(self.playlists_dir, filename)
        
        try:
            with open(file_path, "w") as file:
                writer = csv.DictWriter(file, fieldnames=["title", "uri", "artists", "tempo", "time_signature"])
                if super().empty_file(file_path):
                    writer.writeheader()
                for song in songs:
                    writer.writerow({
                        "title": song.title, 
                        "uri": song.uri, 
                        "artists": ','.join(song.artists),
                        "tempo": song.tempo,
                        "time_signature": song.time_signature
                    })
        except Exception as e:
            print(f"An error occurred while creating the playlist: {e}")
            
        return None
    
    @classmethod
    def get_name(cls):
        """Prompt the user for a playlist name."""
        return input("Playlist name: ")
    
    @classmethod
    def list(cls) -> list:
        """List all playlists."""
        
        playlist_dir = os.path.join("data", "playlists")
        os.makedirs(playlist_dir, exist_ok=True)

        # Only return filenames
        return [file.name.replace(".csv", "") for file in os.scandir(playlist_dir) if file.is_file()]

    
    @classmethod
    def view(cls, filename: str) -> list:
        """View the tracks in a playlist."""        
        tracks = []       
        file_path = os.path.join("data", "playlists", f"{filename}.csv")
        
        if not os.path.exists(file_path):
            print(f"Playlist '{filename}' does not exist.")
            return tracks
        
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
        except Exception as e:
            print(f"An error occurred while reading the playlist: {e}")
        
        tracks.reverse()
        return tracks
    
    @classmethod
    def delete(cls, filename: str) -> None:
        """Delete a playlist."""
        file_path = os.path.join("data", "playlists", f"{filename}.csv")
        try:
            os.remove(file_path)
            print(f"Playlist '{filename}' deleted successfully.")
        except FileNotFoundError:
            print(f"Playlist '{filename}' does not exist.")
        except OSError as e:
            # If it fails, inform the user.
            print("Error: %s - %s." % (e.filename, e.strerror))
            
        return None