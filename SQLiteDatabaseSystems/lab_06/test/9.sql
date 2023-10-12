SELECT DISTINCT p_name
    FROM customer,orders,part,lineitem,nation,region
    WHERE r_name= "AMERICA"
        AND r_regionkey=n_regionkey
        AND n_nationkey=c_nationkey
        AND p_partkey=l_partkey
        AND c_custkey= o_custkey
        AND o_orderkey=l_orderkey
        AND p_name IN (SELECT  p_name
                        FROM supplier,nation,region,part,lineitem
                        WHERE r_name= "ASIA"
                            AND n_nationkey=s_nationkey
                            AND r_regionkey=n_regionkey
                            AND l_partkey=p_partkey
                            AND s_suppkey=l_suppkey
                        GROUP BY p_name
                        HAVING count(p_name)=3)
        ORDER by p_name 

