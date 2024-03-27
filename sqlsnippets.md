# Data cleaning

```
# Filtering Out Rows with Missing Values
SELECT order_id, order_status, order_delivered_carrier_date
FROM orders
WHERE order_delivered_carrier_date IS NULL;

# Replacing Missing Values
SELECT order_id, order_status, COALESCE(order_delivered_carrier_date, 'Unknown') AS filled_column
FROM orders;

# Finding duplicate records
SELECT order_id, customer_id, COUNT(*)
FROM orders
GROUP BY order_id, customer_id
HAVING COUNT(*) > 1;
```

# Data analysis

```
# Window function
SELECT order_date, sales_amount, SUM(sales_amount) OVER (ORDER BY order_date) AS running_total
FROM sales;

# Pivot data
SELECT *
FROM (
    SELECT TO_CHAR(order_date, 'YYYY-MM') AS month, product_category, sales_amount
    FROM sales
) AS pivoted
PIVOT (
    SUM(sales_amount)
    FOR product_category IN ('Electronics', 'Clothing', 'Books')
) AS pivoted_sales;

# Categorize data
SELECT 
    SaleAmount,
    CASE 
        WHEN SaleAmount > 1000 THEN 'High'
        WHEN SaleAmount BETWEEN 500 AND 1000 THEN 'Medium'
        ELSE 'Low'
    END AS SaleLevel
FROM Sales;

# Categorizing with CASE WHEN
SELECT 
    CustomerID,
    PurchaseAmount,
    CASE 
        WHEN CustomerStatus = 'VIP' AND PurchaseAmount > 1000 THEN PurchaseAmount * 0.8
        WHEN CustomerStatus = 'Regular' AND PurchaseAmount > 1000 THEN PurchaseAmount * 0.9
        ELSE PurchaseAmount
    END AS FinalAmount
FROM Customers;

# Advanced use of CASE WHEN
SELECT 
    CustomerID,
    PurchaseAmount,
    CASE 
        WHEN CustomerStatus = 'VIP' AND PurchaseAmount > 1000 THEN PurchaseAmount * 0.8
        WHEN CustomerStatus = 'Regular' AND PurchaseAmount > 1000 THEN PurchaseAmount * 0.9
        ELSE PurchaseAmount
    END AS FinalAmount
FROM Customers;

# Recursive query example
WITH RECURSIVE employee_hierarchy AS (
  SELECT employee_id, first_name, last_name, manager_id, 1 AS level
  FROM employees
  WHERE manager_id IS NULL

  UNION ALL

  SELECT e.employee_id, e.first_name, e.last_name, e.manager_id, eh.level + 1
  FROM employees e
  JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT first_name, last_name, level
FROM employee_hierarchy;

# Subquery factoring
WITH cte_product_sales AS (
  SELECT product_id, SUM(quantity * unit_price) AS total_sales
  FROM order_items oi
  JOIN orders o ON oi.order_id = o.order_id
  WHERE o.order_date >= '2022-01-01' AND o.order_date < '2023-01-01'
  GROUP BY product_id
)
SELECT p.product_name, coalesce(ps.total_sales, 0) AS total_sales
FROM products p
LEFT JOIN cte_product_sales ps ON p.product_id = ps.product_id;
```
