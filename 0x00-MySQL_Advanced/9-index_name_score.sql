-- Create index score with first name
CREATE INDEX idx_name_first_score ON names(name(1), score);