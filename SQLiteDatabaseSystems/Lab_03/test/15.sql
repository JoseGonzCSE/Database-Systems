SELECT Distinct substr(o_orderdate,1,4),count(l_orderkey)
    FROM lineitem,orders,supplier,nation
    WHERE o_orderpriority="3-MEDIUM"
        AND (n_name="GERMANY" or n_name="FRANCE")
        AND l_suppkey=s_suppkey
        AND s_nationkey=n_nationkey
        AND o_orderkey=l_orderkey
    GROUP by substr(o_orderdate,1,4)