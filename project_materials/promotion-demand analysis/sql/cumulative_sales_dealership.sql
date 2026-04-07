WITH daily_sales AS (
    SELECT
        p.model,
        p.year AS model_year,
        p.product_type,
        s.sales_transaction_date,
        SUM(s.sales_amount) AS total_daily_sales
    FROM sales s
    JOIN products p
        ON s.product_id = p.product_id
    WHERE s.channel = 'dealership'
      AND p.production_end_date IS NOT NULL
    GROUP BY
        p.model,
        p.year,
        p.product_type,
        s.sales_transaction_date
)
SELECT
    model,
    model_year,
    product_type,
    sales_transaction_date,
    total_daily_sales,
    SUM(total_daily_sales) OVER (
        PARTITION BY model, model_year
        ORDER BY sales_transaction_date
    ) AS cumulative_sales,
    model || ' ' || model_year AS model_and_year
FROM daily_sales
ORDER BY model, model_year, sales_transaction_date;