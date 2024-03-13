-- count tv shows by genres
SELECT tv_genres.name,
       COUNT(tv_show_genres.genre_id) AS number_of_shows
  FROM tv_genres
  JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
 WHERE tv_show_genres.show_id IS NOT NULL
 GROUP BY tv_genres.id
 ORDER BY number_of_shows DESC;
