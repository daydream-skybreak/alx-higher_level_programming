-- lists all records with score >= 10
-- shows score and name in the described order
-- ordered by score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
