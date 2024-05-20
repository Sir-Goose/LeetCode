# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE (author_id, viewer_id) IN (SELECT viewer_id, author_id FROM Views)
ORDER BY id ASC;
