-- list all genres not linked to the show Dexter
USE hbtn_0d_tvshows;
SELECT tv_genres.name
FROM genres AS tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.tv_show_id != (SELECT id FROM tv_shows WHERE title = 'Dexter')
OR tv_show_genres.tv_show_id IS NULL
GROUP BY tv_genres.id
ORDER BY tv_genres.name ASC;
