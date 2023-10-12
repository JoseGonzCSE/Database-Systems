SELECT DISTINCT SuppRegion,CustRegion,max(o_totalprice)
    FROM(SELECT *,r_name as SuppRegion
            FROM nation,region,lineitem,supplier
            WHERE s_suppkey=l_suppkey
                AND n_nationkey=s_nationkey
                AND r_regionkey=n_regionkey),
        (SELECT *,r_name as CustRegion
            From nation,region,customer,orders
            WHERE c_custkey=o_custkey
                AND n_nationkey=c_nationkey
                AND r_regionkey=n_regionkey)
    WHERE o_orderkey=l_orderkey
    group BY SuppRegion,CustRegion