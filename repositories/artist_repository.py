from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

#CREATE

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

#SELECT BY ID

def select(id):
    user = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist


#DELETE ALL

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)
