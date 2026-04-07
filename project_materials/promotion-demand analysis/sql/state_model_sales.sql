SELECT
    c.state,
    p.model,
    SUM(s.sales_amount) AS total_sales
FROM sales s
INNER JOIN customers c
    ON s.customer_id = c.customer_id
INNER JOIN products p
    ON s.product_id = p.product_id
WHERE s.sales_transaction_date BETWEEN DATE '2015-07-04' AND DATE '2015-10-31'
GROUP BY
    c.state,
    p.model
ORDER BY
    c.state ASC,
    total_sales DESC;