--MySQL Solution
--First, use SUM() OVER() window function to get the cumulative sum for each turn
--Put that in a cte
--Then select only that person name when ordering the cumulative weight in descending order
