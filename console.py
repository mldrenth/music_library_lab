import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Anderson .Paak")
artist_repository.save(artist_1)
album_1 = Album("Malibu", "R&B", artist_1)
album_repository.save(album_1)

pdb.set_trace()
