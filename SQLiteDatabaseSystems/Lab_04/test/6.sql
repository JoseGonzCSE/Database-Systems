SELECT s_name,o_orderpriority,count(DISTINCT p_name)
    FROM supplier,partsupp,part,orders,nation,lineitem
    WHERE n_name="CANADA"
        AND n_nationkey=s_nationkey
        AND p_partkey=ps_partkey
        AND s_suppkey=ps_suppkey
        AND l_orderkey=o_orderkey
        AND p_partkey=l_partkey
        AND ps_suppkey=l_suppkey
    group BY s_name,o_orderpriority
    