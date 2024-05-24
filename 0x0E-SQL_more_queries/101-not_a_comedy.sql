-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT title
FROM tv_shows sh
LEFT JOIN
	tv_show_genres tvg ON tvg.show_id = sh.id
LEFT JOIN
	tv_genres gn ON gn.id = tvg.genre_id
WHERE title NOT IN
	(SELECT title
		FROM tv_shows sh
		INNER JOIN
			tv_show_genres tvg ON tvg.show_id = sh.id
		INNER JOIN
			tv_genres gn ON gn.id = tvg.genre_id
		WHERE name = "Comedy")
ORDER BY title
