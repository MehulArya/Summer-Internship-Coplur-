-- Q-1: What is the total amount each customer spent at the restaurant?
SELECT
  s.customer_id,
  SUM(m.price) AS total_spent
FROM
  sales s
JOIN
  menu m
ON
  s.product_id = m.product_id
GROUP BY
  s.customer_id;

-- Q-2: How many days has each customer visited the restaurant?
SELECT customer_id, COUNT(DISTINCT order_date) as total_days
FROM sales
GROUP BY customer_id;

-- Q-3 What was the first item from the menu purchased by each customer?
SELECT customer_id, MIN(DISTINCT order_date) as total_days
FROM sales
GROUP BY customer_id;

-- Q-4 What is the most purchased item on the menu and how many times was it purchased by all customers?
SELECT s.customer_id, COUNT(s.product_id) AS most_frequent_item
FROM sales s
WHERE s.product_id = (
  SELECT product_id
  FROM (
    SELECT product_id, COUNT(product_id) AS freq
    FROM sales
    GROUP BY product_id
  ) AS X
  WHERE freq = (
    SELECT MAX(freq)
    FROM (
      SELECT product_id, COUNT(product_id) AS freq
      FROM sales
      GROUP BY product_id
    ) AS Y
  )
)
GROUP BY s.customer_id;

-- Q-5 Which item was the most popular for each customer?
SELECT customer_id, product_id, order_count
FROM (
    SELECT customer_id, product_id, COUNT(product_id) AS order_count
    FROM sales
    GROUP BY customer_id, product_id
) AS customer_product_counts
WHERE (customer_id, order_count) IN (
    SELECT customer_id, MAX(order_count)
    FROM (
        SELECT customer_id, product_id, COUNT(product_id) AS order_count
        FROM sales
        GROUP BY customer_id, product_id
    ) AS counts
    GROUP BY customer_id
);

-- Q-6 Which item was purchased first by the customer after they became a member?
SELECT s.customer_id, s.order_date, m.product_name
FROM sales s
JOIN members mem ON s.customer_id = mem.customer_id
JOIN menu m ON s.product_id = m.product_id
WHERE s.order_date = (
    SELECT MIN(order_date)
    FROM sales
    WHERE customer_id = s.customer_id
      AND order_date >= mem.join_date
)
AND s.order_date >= mem.join_date;

-- Q-7 Which item was purchased just before the customer became a member?
SELECT s.customer_id, s.order_date, m.product_name
FROM sales s
JOIN members mem ON s.customer_id = mem.customer_id
JOIN menu m ON s.product_id = m.product_id
WHERE s.order_date = (
    SELECT MAX(order_date)
    FROM sales
    WHERE customer_id = s.customer_id
      AND order_date < mem.join_date
)
AND s.order_date < mem.join_date;

-- Q-8 What is the total items and amount spent for each member before they became a member?
SELECT
  s.customer_id,
  COUNT(*) AS total_items,
  SUM(m.price) AS total_amount
FROM sales s
JOIN members mem ON s.customer_id = mem.customer_id
JOIN menu m ON s.product_id = m.product_id
WHERE s.order_date < mem.join_date
GROUP BY s.customer_id;

-- Q-9 If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
SELECT
  s.customer_id,
  SUM(
    CASE
      WHEN m.product_name = 'sushi' THEN m.price * 20
      ELSE m.price * 10
    END
  ) AS total_points
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY s.customer_id;

-- Q-10 In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just
--      sushi - how many points do customer A and B have at the end of January?
SELECT
  s.customer_id,
  SUM(
    CASE
      WHEN s.order_date BETWEEN mem.join_date AND mem.join_date + INTERVAL 6 day
        THEN m.price * 20
      WHEN m.product_name = 'sushi'
        THEN m.price * 20
      ELSE m.price * 10
    END
  ) AS total_points
FROM sales s
JOIN menu m ON s.product_id = m.product_id
JOIN members mem ON s.customer_id = mem.customer_id
WHERE s.customer_id IN ('A', 'B')
  AND s.order_date <= '2021-01-31'
GROUP BY s.customer_id;