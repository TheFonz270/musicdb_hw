from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import repositories.album_repository
  
def select_all():  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'] )
        artists.append(artist)
    return users 

def save(artist):
    sql = f"INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select(id):
    # Create an empty variable 
    artist = None
    # Create an SQL string
    sql = "SELECT * FROM artists WHERE id = %s"
    # Create our values list
    values = [id]
    # Run SQL and capture result
    result = run_sql(sql, values)[0]
    # Create a new task object
    if result is not None:
        artist = Artist(result['name'], result['id'])
    # Return the task object
    return artist