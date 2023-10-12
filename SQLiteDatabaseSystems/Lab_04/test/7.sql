SELECT n_name,o_orderstatus,count(*)
    FROM nation,orders,region,customer
    WHERE r_name="AMERICA"
        AND n_regionkey=r_regionkey
        AND c_nationkey=n_nationkey
        AND o_custkey=c_custkey
    GROUP BY n_name,o_orderstatus