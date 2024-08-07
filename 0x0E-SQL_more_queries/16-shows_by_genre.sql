-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT title, name
FROM tv_shows  tv
LEFT JOIN
	tv_show_genres  tv_g ON tv.id = tv_g.show_id
LEFT JOIN
	tv_genres  gn ON gn.id = tv_g.genre_id
ORDER BY title, name
