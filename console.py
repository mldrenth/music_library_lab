import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

artist_1 = Artist("Anderson .Paak")
artist_repository.save(artist_1)