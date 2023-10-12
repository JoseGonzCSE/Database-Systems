SELECT c_name,count(*)
    FROM orders, customer,nation
    WHERE n_name= "GERMANY"
        AND o_orderdate >="1993-01-01" and o_orderdate<="1993-12-31"
        AND n_nationkey=c_nationkey
        AND c_custkey=o_custkey
    GROUP BY c_name