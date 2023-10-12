SELECT n_name,count(o_orderkey)
    FROM orders, customer,nation,region
    WHERE r_name="AMERICA"
        AND r_regionkey=n_regionkey
        AND n_nationkey=c_nationkey
        AND o_custkey=c_custkey
    GROUP BY n_name