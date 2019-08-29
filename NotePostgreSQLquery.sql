DESCRIBE empapi_empinfo;
SHOW CREATE TABLE empapi_empinfo;
SHOW TABLES LIKE '%key_word%';
SHOW INDEX FROM table_name;
SELECT * FROM table_name;

pg_dump -t empapi_empinfo -s;

select column_name, data_type, character_maximum_length
from INFORMATION_SCHEMA.COLUMNS where table_name = 'empapi_empinfo';

SELECT *
FROM info_schema.columns
WHERE table_schema = 'empapi_empinfo';

---
SELECT * FROM article_article ORDER BY 1 DESC;
	SELECT * FROM movie_movie ORDER BY 1 DESC;
	SELECT * FROM movie_song ORDER BY 1 DESC;


---
SELECT * FROM movie_movie AS mm 
INNER JOIN movie_song AS ms ON (mm.)


---
SELECT * FROM movie_song AS ms 
INNER JOIN movie_movie AS mm ON (ms.movie_id = mm.id)
ORDER BY 1 DESC;


--- songSearch
SELECT * FROM movie_song
WHERE name LIKE '%son%';a


--- fc_cust_reg

CREATE TABLE company
()



