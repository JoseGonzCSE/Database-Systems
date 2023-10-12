SELECT count(DISTINCT o_custkey)
    FROM orders, customer  
    WHERE c_custkey=o_custkey
        AND o_orderkey not IN ( SELECT DISTINCT o_orderkey
                            FROM orders, lineitem, supplier,nation,region
                            WHERE o_orderkey=l_orderkey
                                AND n_nationkey=s_nationkey
                                AND n_regionkey=r_regionkey
                                AND s_suppkey=l_suppkey
                                AND r_name NOT IN ("AMERICA") )