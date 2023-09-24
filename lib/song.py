class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    all_genres = []
    artist_count = {}
    all_artists = []

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)


    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count +=increment  
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist) 

    @classmethod
    def add_to_genre_count(cls,genre):
        cls.all_genres.append(genre) 
        cls.genre_count= {x: cls.all_genres.count(x) for x in cls.all_genres}
    @classmethod
    def add_to_artist_count(cls,artist):
        cls.all_artists.append(artist) 
        cls.artist_count= {x: cls.all_artists.count(x) for x in cls.all_artists}

#ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
#print(Song.genre_count)