-- select score and count them ordered by each score so that the count aggregate count every different apparition of score
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY  score
ORDER BY score DESC;
