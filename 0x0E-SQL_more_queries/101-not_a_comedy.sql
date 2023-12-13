--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN genres ON tv_show_genres.genre_id = genres.id AND genres.name = 'Comedy'
WHERE genres.id IS NULL
ORDER BY tv_shows.title ASC;
