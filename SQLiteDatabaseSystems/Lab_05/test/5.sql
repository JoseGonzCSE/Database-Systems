SELECT s_name,p_size,min(ps_supplycost)
    FROM supplier,partsupp,part,region,nation
    WHERE p_type LIKE "%STEEL%"
        AND r_name= "ASIA"
        AND r_regionkey=n_nationkey
        AND p_partkey=ps_partkey
        AND s_suppkey=ps_suppkey
        and n_nationkey=s_nationkey
    
    GROUP BY p_size
    
 

