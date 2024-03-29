-- list shows without the genre Comedy
SELECT DISTINCT tv_shows.title
  FROM tv_shows
  LEFT JOIN tv_show_genres
    ON tv_show_genres.show_id = tv_shows.id
 WHERE tv_show_genres.genre_id <>
       (SELECT tv_genres.id
          FROM tv_genres
         WHERE tv_genres.name = "Comedy")
       OR tv_show_genres.genre_id IS NULL
 ORDER BY tv_shows.title;
