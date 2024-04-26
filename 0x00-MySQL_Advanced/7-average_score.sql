-- creates a procedure that that computes and store score average
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
DECLARE avg_score float;
SET avg_score = (
    SELECT AVG(score)
    FROM corrections AS C 
    WHERE C.user_id = user_id
    );
UPDATE users SET average_score = avg_score WHERE id = user_id;
END
