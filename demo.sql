-- Create the table
CREATE TABLE sample_data (
    id int,
    date DATE NOT NULL,
    value NUMERIC(10, 2) NOT NULL
);

-- Create a view
CREATE OR REPLACE VIEW sample_data_view AS
    SELECT date, value FROM sample_data ORDER BY date;

-- Add index
CREATE INDEX sample_data_date_idx ON sample_data (date);

-- Insert sample data
INSERT INTO sample_data (id, date, value) VALUES
(1, '2024-01-01', 100.50),
(2, '2024-01-02', 105.75),
(3, '2024-01-03', 98.25),
(4, '2024-01-04', 110.00),
(5, '2024-01-05', 112.50),
(6, '2024-01-06', 108.75),
(7, '2024-01-07', 115.25),
(8, '2024-01-08', 120.00),
(9, '2024-01-09', 118.50),
(10, '2024-01-10', 122.75);

-- Insert some more sample data
INSERT INTO sample_data (id, date, value) VALUES
(11, '2024-01-11', 125.50);
INSERT INTO sample_data (id, date, value) VALUES
(12, '2024-01-12', 130.75);
INSERT INTO sample_data (id, date, value) VALUES
(13, '2024-01-13', 135.25);
