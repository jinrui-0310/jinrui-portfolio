WITH customers_with_dealerships AS (
    SELECT DISTINCT c.customer_id, c.city
    FROM customers c
    INNER JOIN dealerships d
        ON c.city = d.city
)
SELECT
    s.product_id,
    s.channel,
    s.sales_amount,
    CASE
        WHEN s.sales_amount > 50000 THEN 'Premium'
        WHEN s.sales_amount >= 10000 THEN 'Standard'
        ELSE 'Basic'
    END AS price_category,
    EXTRACT(YEAR FROM s.sales_transaction_date) AS transaction_year,
    s.sales_transaction_date
FROM sales s
JOIN customers_with_dealerships cwd
    ON s.customer_id = cwd.customer_id
WHERE s.sales_transaction_date >= DATE '2017-01-01'
  AND s.sales_transaction_date < DATE '2020-01-01'
  AND s.sales_amount > 5000;