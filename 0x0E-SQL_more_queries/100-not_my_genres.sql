-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT DISTINCT name
FROM tv_shows sh
INNER JOIN
	tv_show_genres tvg ON sh.id = tvg.show_id
INNER JOIN
	tv_genres gn ON gn.id = tvg.genre_id
WHERE name NOT IN
	(SELECT name
	FROM tv_shows 
	INNER JOIN 
        	tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN
		tv_genres ON tv_show_genres.genre_id = tv_genres.id
	WHERE title = "Dexter")
ORDER BY name
