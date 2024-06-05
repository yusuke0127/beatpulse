import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

class Spotify:
    """Spotify utility class for interacting with the Spotify API."""
    
    @classmethod
    def sp_client(cls):
        """Initialize and return a Spotify client with client credentials."""  
        try:
            client_id = os.getenv('SPOTIPY_CLIENT_ID')
            client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
            if not client_id or not client_secret:
                raise ValueError("Spotify client ID and secret must be set in the environment variables.")
            
            auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
            return spotipy.Spotify(auth_manager=auth_manager)
        except Exception as e:
            raise RuntimeError("Failed to initialize Spotify client") from e


    @classmethod
    def search(cls, song_title:str) -> dict:
        """Search for a track by title and return search results."""
        try:
            sp = cls.sp_client()
            results = sp.search(q=song_title, type="track")
            return results["tracks"]["items"]
        except spotipy.exceptions.SpotifyException as e:
            raise RuntimeError("Failed to search for track") from e

    
    @classmethod
    def song_info(cls, song_uri:str):
        """Get song information by URI."""
        try:
            sp = cls.sp_client()
            return sp.audio_features(song_uri)[0]
        except spotipy.exceptions.SpotifyException as e:
            raise RuntimeError("Failed to get song information") from e

    
    @classmethod
    def get_tempo(cls, song_uri:str) -> dict:
        """Get tempo and time signature of a song by URI."""
        try:
            sp = cls.sp_client()
            af = sp.audio_features(song_uri)[0]
            return {
                "tempo": round(af["tempo"]),
                "time_signature": round(af["time_signature"])
            }
        except spotipy.exceptions.SpotifyException as e:
            raise RuntimeError("Failed to get tempo and time signature") from e
