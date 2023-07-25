class Song:
    count = 0
    artists = set()
    genres = set()
    all=[]
    genre_count={}
    artist_count={}
    genreMap = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_all(self)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

        
    @classmethod
    def add_to_all(cls, song):
        cls.all.append(song)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, self):
        cls.genres.add(self.genre)

    @classmethod
    def add_to_artists(cls, self):
        cls.artists.add(self.artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = len([song.name for song in cls.all if song.genre == genre])
        #print(cls.genre_count)
        
    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = len([song.name for song in cls.all if song.artist == artist])

# Song("99 Problems", "Jay Z", "Rap")
# Song("Halo", "Beyonce", "Pop")
# Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# Song("Out of Touch", "Hall and Oates", "Pop")
# Song("Sara Smile", "Hall and Oates", "Pop")
# print(Song.genre_count["Pop"])
