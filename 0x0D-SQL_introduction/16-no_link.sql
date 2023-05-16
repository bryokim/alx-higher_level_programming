-- Lists all records of the table second_table.
-- Don't list rows without a name value
-- Results should display the score and name.
-- Records listed by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
