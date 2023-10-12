SELECT n_name
    FROM nation,lineitem,supplier,orders
    WHERE l_shipdate BETWEEN "1994-00-00" and "1994-12-32"
        AND o_orderkey=l_orderkey
        AND n_nationkey=s_nationkey
        AND l_suppkey=s_suppkey
        GROUP by n_name
        ORDER by sum(l_extendedprice) DESC limit 1