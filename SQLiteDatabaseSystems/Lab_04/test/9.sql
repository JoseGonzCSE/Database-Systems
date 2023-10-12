SELECT count(DISTINCT o_clerk)
    FROM nation,orders,supplier,lineitem
    WHERE n_name= "UNITED STATES"
        AND n_nationkey=s_nationkey
        AND o_orderkey=l_orderkey
        AND l_suppkey=s_suppkey
    