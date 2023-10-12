SELECT c_name, sum(o_totalprice)
    FROM nation, orders, customer
    WHERE o_orderdate >="1995-01-01" AND o_orderdate <="1995-12-31"
    AND n_name ="FRANCE"
    AND c_custkey=o_custkey
    AND c_nationkey=n_nationkey
    GROUP BY c_name