-- Write a SQL script that creates a stored procedure that computes and store the average
-- score for a student. An average score can be a decimal.
-- Procedure takes 1 input:
-- user_id, a users.id value


delimiter |
CREATE PROCEDURE ComputeAverageScoreForUser(
	user_id INT
)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END
|
delimiter ;
