SELECT r_name
    FROM region,nation,customer,lineitem,supplier,orders
    WHERE r_regionkey=n_regionkey
        AND n_nationkey=s_nationkey
        AND s_suppkey=l_suppkey
        AND c_custkey=o_custkey
        and c_nationkey=s_nationkey
        AND o_orderkey=l_orderkey
    GROUP by r_name
    ORDER by min(l_extendedprice) DESC
    limit 1