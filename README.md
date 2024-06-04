# BeatPulse
#### Video Demo:  https://www.youtube.com/watch?v=g4YMt9ij3sI
### Description:
BeatPulse is a CLI app where users can search for a music's BPM using the Spotify's API. Users can also create playlists to store BPM's of multiple songs. Search history is also stored for convenience.
## Code Structure
```
data
├── history.csv
└── playlists
lib
├── base.py
├── history.py
├── playlist.py
├── spotify.py
└── track.py
README.md
requirements.txt
project.py 
.env
.envrc
test_project.py
```

- **data** - stores history and created playlists in csv format
- **lib** - Contains the apps logic
    - `base.py` - Base class
    - `history.py` - Contains history class implementation
    - `playlist.py` - Contains playlist class implementation
    - `spotify.py` - Contains the client definition used in interacting with Spotify's API
    - `track.py` - Model class for tracks with its properties
- **requirements.txt** - List of dependecies
- **project.py** - Serves as the CLI interface
- **test_project.py** - Test suite for the app
- **.env** - Where `env vars` are stored
- **.envrc** - Necessary file to use dotenv in pyenv

## Requiremets
- `python-dotenv` - Used to the managed environment variables
- `pytest` - testing framework used
- `inflect` - Used to make generating sentences from a list easier
- `spotipy` - Spotify API wrapper written in Python
- `pydantic<=1.10.10` - Dependency for `inflect`, as the newer version 2 breaks it.

## Installation
1. Clone the repository:
```
git clone git@github.com:yusuke0127/beatpulse.git
cd git@github.com:yusuke0127/beatpulse.git
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Set up Spotiufy API credentials
    - Follow the getting started part in [Spotify's API documentation](https://developer.spotify.com/documentation/web-api) to generate your `CLIENT_ID` and `CLIENT_SECRET`
    - Create a `.env` file in the root directory of your project and add your credentials:
    ```
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    ```

## Usage
1. Run the CLI application:
```
python project.py
```
2. Follow the on-screen prompts to interact with the application:
```
================================================================================
                    Welcome to BeatPulse
================================================================================

                1 - Search for a song
                2 - Create a playlist
                3 - View playlists
                4 - Delete a playlist
                5 - View search history
                6 - Clear search history
                1
```
3. Example interaction
```
Song title: mr brightside
1 Mr. Brightside by The Killers
2 Mr. Brightside by The Killers
3 Mr. Brightside by Savage Sons
...
================================================================================
Which one: 1
Mr. Brightside by The Killers has a tempo of 148 and time signature of 4 / 4
```

## Testing
1. Ensure `pytest` is installed.
2. Run the test suite:
```
pytest test_project.py
```