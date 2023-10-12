SELECT Distinct nation.n_name
    FROM orders, customer, nation
    WHERE(o_orderdate='1994-09-09' OR o_orderdate='1994-09-10' Or o_orderdate='1994-09-11')AND n_nationkey=c_nationkey
        AND c_custkey=o_custkey
    ORDER BY nation.n_name ASC;