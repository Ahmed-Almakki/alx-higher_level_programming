-- script that lists all genres from hbtn_0d_tvshows and displays the
SELECT name AS "genre", COUNT(genre_id) AS "number_of_shows"
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC
