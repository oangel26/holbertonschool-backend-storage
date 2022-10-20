-- Write a SQL script that creates a stored procedure that adds a new correction for a student.
-- Procedure takes 3 inputs (in this order):
-- user_id, a users.id value
-- project_name, a new or already exists projects
-- score, the score value for the correction

delimiter |
CREATE PROCEDURE AddBonus(
	user_id INT,
    project_name VARCHAR(255),
    score FLOAT
)
BEGIN
	INSERT INTO projects (name)
    SELECT * FROM (SELECT project_name) AS tmp
    WHERE NOT EXISTS (
		SELECT name FROM projects WHERE name = project_name
	) limit 1;
    SET @project_id = (SELECT id FROM projects WHERE name = project_name);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, @project_id, score);
END
|
delimiter ;
