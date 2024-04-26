-- creates a stored procedure that adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE addBonus(
    user_id INT,
    project_name varchar(255),
    score INT
)
BEGIN
DECLARE project_id INT;
IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
THEN
INSERT INTO projects (name) VALUES (project_name);
END IF;
SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
INSERT INTO corrections (user_id, project_id, score) values(user_id, project_id, score);
END
$$
DELIMITER ;
