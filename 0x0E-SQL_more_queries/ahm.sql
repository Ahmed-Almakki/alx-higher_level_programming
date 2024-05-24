-- aa 
SELECT genre_id, title, name
FROM tv_shows sh
LEFT JOIN
        tv_show_genres tvg ON tvg.genre_id = sh.id
LEFT JOIN
	tv_genres gn ON gn.id = tvg.genre_id
where name <> "Comedy" OR name IS NULL
