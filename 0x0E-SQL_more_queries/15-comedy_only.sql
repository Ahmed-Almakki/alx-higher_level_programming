-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title
FROM tv_show_genres
LEFT JOIN
	tv_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN
	tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE name = "Comedy"
ORDER BY tv_shows.title
