SELECT min(l_discount)
    FROM lineitem
    WHERE l_discount>(SELECT avg(l_discount)
                        FROM lineitem,orders
                        WHERE o_orderkey=l_orderkey
                            AND o_orderdate BETWEEN "1996-10-00" AND "1996-10-33")