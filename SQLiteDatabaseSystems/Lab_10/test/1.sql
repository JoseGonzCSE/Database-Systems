DROP TRIGGER t1;

CREATE TRIGGER t1 AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE orders SET o_orderdate = DATETIME('2021-12-01');
END;

INSERT INTO orders
SELECT *
FROM orders
WHERE
o_orderdate LIKE '%1996-12%';

SELECT count(o_orderdate)
FROM orders
WHERE
o_orderdate LIKE '%2021%';