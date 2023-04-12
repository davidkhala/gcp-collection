-- count Shakespeare's use of the string "raisin"
SELECT
  word,
  SUM(word_count) AS count
FROM
  `bigquery-public-data`.samples.shakespeare
WHERE
  word LIKE '%raisin%'
GROUP BY
  word