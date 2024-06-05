class Track:
    def __init__(self, title:str, uri: str, artists: list[str] = None, tempo: int = 0, time_signature: int = 0) -> None:
        """
        Initialize a new Track instance.

        :param title: Title of the track
        :param uri: URI of the track
        :param artists: List of artists for the track
        :param tempo: Tempo of the track
        :param time_signature: Time signature of the track
        """
        self.title = title
        self.uri = uri
        self.artists = artists if artists is not None else []
        self.time_signature = time_signature
        self.tempo = tempo

    @property
    def title(self):
        """Get the title of the track."""
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        """Set the title of the track."""
        if not title:
            raise ValueError("Invalid title")
        self._title = title

    @property
    def uri(self):
        """Get the URI of the track."""
        return self._uri


    @uri.setter
    def uri(self, uri: str) -> None:
        """Set the URI of the track."""
        if not uri:
            raise ValueError("Invalid URI")
        self._uri = uri

    @property
    def artists(self) -> list[str]:
        """Get the list of artists for the track."""
        return self._artists
    
    @artists.setter
    def artists(self, artists: list[str]) -> None:
        # self._artists = artists
        
        """Set the list of artists for the track."""
        if not isinstance(artists, list):
            raise ValueError("Artists should be a list of strings")
        self._artists = artists

    
    @property
    def tempo(self) -> int:
        """Get the tempo of the track."""
        return self._tempo 

    @tempo.setter
    def tempo(self, tempo: int) -> None:
        """Set the tempo of the track."""
        if not isinstance(tempo, int):
            raise ValueError("Tempo should be an integer")
        self._tempo = tempo

    @property
    def time_signature(self) -> int:
        """Get the time signature of the track."""
        return self._time_signature

    @time_signature.setter
    def time_signature(self, time_signature: int) -> None:
        """Set the time signature of the track."""
   
        if not isinstance(time_signature, int):
            raise ValueError("Time signature should be an integer")
        self._time_signature = time_signature
    
    @classmethod
    def get_track(cls):
        """Prompt the user to input a song title."""
        return input("Song title: ")