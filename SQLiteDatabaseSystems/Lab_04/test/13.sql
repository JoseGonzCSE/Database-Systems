SELECT count(l_linenumber)
    FROM lineitem,orders,
        (SELECT s_suppkey
        FROM supplier,region,nation
        WHERE r_regionkey=n_regionkey
            AND n_nationkey=s_nationkey
            AND r_name="AFRICA") S,
        (SELECT c_custkey
        FROM nation,customer
        WHERE n_nationkey=c_nationkey
            and n_name="UNITED STATES") C
    WHERE o_orderkey=l_orderkey
        AND C.c_custkey=o_custkey
        AND S.s_suppkey=l_suppkey;
  
    