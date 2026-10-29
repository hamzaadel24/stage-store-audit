CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    full_name   TEXT NOT NULL,
    city        TEXT,
    email       TEXT UNIQUE,
    created_at  DATE DEFAULT CURRENT_DATE
);


CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    item        TEXT NOT NULL,
    price       NUMERIC CHECK (price > 0),
    qty         INT NOT NULL,
    total_cost  NUMERIC
);


INSERT INTO customers (customer_id, full_name, city, email) VALUES
(1, 'Ahmed Ali',   'Cairo', 'ahmed@example.com'),
(2, 'Sara',        'Alex',  'sara@example.com'),
(3, 'Mona',        'Giza',  'mona@example.com'),
(4, 'Omar Hassan', 'Tanta', 'omar@example.com');


INSERT INTO orders (order_id, customer_id, item, price, qty, total_cost) VALUES
(101, 1, 'laptop stand', 250.50, 3, 751.50),
(102, 2, 'mouse pad',    400.00, 2, 800.00),
(106, 3, 'webcam hd',    150.75, 4, 603.00);

--*Query 1 (WHERE + ORDER BY):* Select all orders where total_cost > 500
SELECT * FROM orders
WHERE total_cost > 500
ORDER BY total_cost DESC;


--*Query 2 (INNER JOIN + GROUP BY):* Show each customer's full_name, order count (COUNT), and total spent (SUM(total_cost)).
SELECT c.full_name, COUNT(o.order_id) AS order_count, SUM(o.total_cost) AS total_spent
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.full_name;


--*Query 3 (LEFT JOIN):* Find the customer who has *no orders*

SELECT c.full_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;


--Query 4 (HAVING):* Show only customers whose SUM(total_cost) is greater than 700

SELECT c.full_name,
       SUM(o.total_cost) AS total_spent
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.full_name
HAVING SUM(o.total_cost) > 700;


--*Query 5 (CASE WHEN):* Select all orders and add a column order_label that labels total_cost < 500 

SELECT *,
       CASE
           WHEN total_cost < 500 THEN 'cheap'
           WHEN total_cost < 800 THEN 'medium'
           ELSE 'expensive'
       END AS order_label
FROM orders;
