-- select the score and name of all user with a score above 10 order in decrement (higher first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
