from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository
  
def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(['artist_id'])
        album = Album(row['title'], artist, row['genre'], row['id'] )
        albums.append(task)
    return tasks 

def save(album):
    sql = f"INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album