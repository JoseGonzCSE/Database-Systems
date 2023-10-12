SELECT count(distinct o_orderkey)
    FROM orders,lineitem,
        (SELECT s_suppkey
            FROM supplier
            WHERE s_acctbal<0) S,
        (SELECT c_custkey
            FROM customer
            WHERE c_acctbal>0) C
    Where o_orderkey=l_orderkey
        AND C.c_custkey=o_custkey
        AND S.s_suppkey=l_suppkey