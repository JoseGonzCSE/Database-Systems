SELECT n_name,count(distinct o_orderkey)
    FROM nation,orders,supplier,lineitem
    WHERE o_orderdate >= "1995-01-01" AND o_orderdate <= "1995-12-31"
        AND o_orderstatus ="F"
        AND o_orderkey=l_orderkey
        AND n_nationkey=s_nationkey
        AND l_suppkey=s_suppkey
    Group by n_name
    HAVING count(DISTINCT o_orderkey)>50