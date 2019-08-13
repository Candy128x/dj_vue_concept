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
SELECT * FROM table_name ORDER BY 1 DESC;
SELECT * FROM public.article_article;











