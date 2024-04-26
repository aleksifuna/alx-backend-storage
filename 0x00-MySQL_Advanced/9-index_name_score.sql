-- creates an index idx_name_first on the table names
-- first letter of name column
-- score column
CREATE INDEX idx_name_first_score
ON names (name(1), score);
