SELECT o_orderpriority,count(p_name)
    FROM orders,part,lineitem
    WHERE o_orderkey= l_orderkey 
        AND p_partkey=l_partkey
        and o_orderdate BETWEEN "1997-00-00" AND "1997-12-33"
        AND (julianday(l_receiptdate) - julianday(l_commitdate)) > 0
    GROUP BY o_orderpriority
