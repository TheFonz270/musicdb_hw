import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository
import os

os.system('psql -d music_collection -f db/music_collection.sql')

artist1 = Artist('Ozzy')
artist2 = Artist('Imagine Dragons')
artist3 = Artist('David Bowie')

artist_repository.save(artist1)
artist_repository.save(artist2)
artist_repository.save(artist3)

album1 = Album('Blizzard of Ozz', 'metal', artist1)
album2 = Album('Believer', 'Rock-ish', artist2)
album3 = Album('Life on Mars', 'Bowie', artist3)

album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)
