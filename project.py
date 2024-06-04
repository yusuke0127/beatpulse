import sys
import inflect
from lib.track import Track
from lib.spotify import Spotify
from lib.history import History
from lib.playlist import Playlist

p = inflect.engine()


def main():
    """Main function to handle user input and execute corresponding actions."""
    welcome()
    match get_user_input():
        case 1:
            results = search_track()
            if results:
                print("Search results:")
                song = process_results(results)
                print(f"{song.title} by {p.join(song.artists)} has a tempo of {song.tempo} and time signature of {song.time_signature} / 4")
        case 2:
            create_playlist()
        case 3:
            view_playlist()
        case 4:
            delete_playlist()
        case 5:
            get_history()
        case 6:
            clear_history()
        case _:
            sys.exit("Command not found")
    

def get_user_input():
    """Prompt the user to select an option and return the corresponding integer."""
    while True:
        try:
            return int(input("""
                1 - Search for a song
                2 - Create a playlist
                3 - View playlists
                4 - Delete a playlist
                5 - View search history
                6 - Clear search history
                =========================
                Select: """))
        except EOFError:
            break
        except ValueError:
            pass


def welcome():
    """Print a welcome message."""
    print("="*60)
    print(" "*20 + "Welcome to BeatPulse")
    print("="*60)


def search_track():
    """Search for a track using the Spotify API."""
    return Spotify.search(Track.get_track())


def select_track(list):
    """Prompt the user to select a track from a list and return the selected track."""
    while True:
        try:
            selected = int(input("Which one: "))
            if selected < 1 or selected > len(list):
                print(f"Invalid selection. Please choose a number between 1 and {len(list)}.")
            else:
                return list[selected - 1]
        except ValueError:
            print("Invalid input. Please enter a number.")
        

def process_results(results):
    track_list = []
    for idx, song in enumerate(results):
        # Pluck artist names from artists list
        artist_names = pluck(song["artists"], "name")
        track = Track(song["name"], song["uri"], artist_names)
        print(f"{idx + 1}. {track.title} by {p.join(artist_names)}")

        track_list.append(track)

    print("="*60)
    selected_track  = select_track(track_list)
    track_info = Spotify.get_tempo(selected_track.uri)
    selected_track.tempo = track_info["tempo"]
    selected_track.time_signature = track_info["time_signature"]

    write_history(selected_track)
    return selected_track


def create_playlist():
    """Create a playlist by adding selected tracks."""
    name = Playlist.get_name()
    playlist = []
    
    if name in Playlist.list():
        print(f"{name} already exists!")
        return
    
    while True:
        try:
            results = search_track()
            song = process_results(results)
            # Save song to a playlist
            playlist.append(song)
            ans = input("Search for more songs? Yes or No: ").lower()
            if ans == "no" or ans == "n":
                Playlist().create(playlist, name)
                print(f"Playlist {name} created")
                break
        except EOFError():
            sys.exit("Playlist creation interrupted.")
            

def view_playlist():
    """View and list all playlists."""
    playlists = Playlist.list()
    if len(playlists) < 1:
        print("No playlist yet!")
        return
    
    for i, playlist_title in enumerate(playlists, start=1):
        print(f"{i} - {playlist_title}")
    
    # Select playlist to view
    try:
        selected = int(input("Select a playlist to view: "))
        if selected < 1 or selected > len(playlists):
            raise ValueError
        playlist_songs = Playlist.view(playlists[selected - 1])
        
        for i, track in enumerate(playlist_songs, start=1):
            artists = p.join(track["artists"].split(","))
            print(f"{i}. title: {track['title']}, artists: {artists}, tempo: {track['tempo']}, time_signature: {track['time_signature']}")

    except ValueError:
        print("Invalid selection or playlist name doesn't exist.")


def delete_playlist():
    """Delete a selected playlist."""
    playlists = Playlist.list()
    
    if len(playlists) < 1:
        print("No playlist to delete!")
        return
    for i, playlist_title in enumerate(playlists, start=1):
        print(f"{i} - {playlist_title}")

    # Select which playlist to delete
    try:
        selected = int(input("Select a playlist to delete: "))
        if selected < 1 or selected > len(playlists):
            raise ValueError
        Playlist.delete(playlists[selected - 1])
    except ValueError():
        print("Invalid selection or playlist doesn't exist.")
    

def get_history():
    """Retrieve and return the search history."""
    history = History.list()
    if len(history) < 1:
        print("Empty search history")
        
    for track in history:
        artists = p.join(track['artists'].split(","))
        print(f"title: {track['title']}, artists: {artists}, tempo: {track['tempo']}, time_signature: {track['time_signature']}")


def clear_history():
    """Clear the search history and exit."""
    History.clear()
    sys.exit("Successfully cleared history")


def write_history(song):
    """Write a track to the search history."""
    History().write(song)
    

def pluck(list, key):
    """Return a list of values corresponding to the specified key from a list of dictionaries."""
    return [x.get(key) for x in list]


if __name__ == "__main__":
    main()