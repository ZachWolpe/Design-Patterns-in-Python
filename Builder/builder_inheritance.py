
class Art:
    def __init__(self) -> None:
        # Piece
        self.artwork        = None
        self.museum         = None
        self.era            = None
        self.year           = None

        # Artist
        self.artist         = None
        self.dob            = None
        self.nationality    = None

    def __str__(self) -> str:
        return f'\n{self.artwork} ({self.year}) is housed in the {self.museum}. \
            \nPainted by {self.nationality} artist {self.artist} (born {self.dob}) as a part of the {self.era} art movement. \n'

    @staticmethod
    def new():
        return ArtBuilder()


class ArtBuilder:
    def __init__(self) -> None:
        self.art = Art()

    def build(self):
            return self.art


class ArtArtistBuilder(ArtBuilder):
    def artist(self, artist):
        self.art.artist = artist
        return self
    
    def date_of_birth(self, dob):
        self.art.dob = dob
        return self

    def nationality(self, nationality):
        self.art.nationality = nationality
        return self


class ArtPieceBuilder(ArtArtistBuilder):
    def artwork_name(self, artwork):
        self.art.artwork = artwork
        return self

    def location(self, museum):
        self.art.museum = museum
        return self
    
    def artistic_movement(self, era):
        self.art.era = era
        return self
    
    def year(self, year):
        self.art.year = year
        return self
    
    

if __name__ == '__main__':
    ab = ArtPieceBuilder()
    a  = ab\
        .artist('Alexandre Cabanel')\
        .date_of_birth('28 September 1823')\
        .nationality('French')\
        .artwork_name('L\'Ange déchu')\
        .location('Musée Fabre in Montpellier, France')\
        .artistic_movement('Academic art')\
        .year('1847')\
        .build()
    print(a)