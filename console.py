import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# album_repository.delete_all()
# artist_repository.delete_all()

artist_1 = Artist("Anderson .Paak")
artist_repository.save(artist_1)
artist_2 = Artist("Test Artist")
artist_repository.save(artist_2)
album_1 = Album("Malibu", "R&B", artist_1)
album_repository.save(album_1)
album_2 = Album("Test 1", "Test genre 1", artist_2)
album_repository.save(album_2)
album_3 = Album("Test 2", "Test genre 2", artist_2 )
album_repository.save(album_3)

artist_3 = Artist("Different", 12)
album_4 = Album("Different Title", "Different Genre", artist_3, 20)

artists = artist_repository.select_all()
albums = album_repository.select_all()

for artist in artists:
    print(artist.__dict__)

for album in albums:
    print(album.__dict__)

pdb.set_trace()
