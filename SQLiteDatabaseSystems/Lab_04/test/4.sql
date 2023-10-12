SELECT s_name, count(*)
    FROM supplier,part,nation,partsupp
    WHERE p_size<20
        AND n_name="CANADA"
        AND n_nationkey=s_nationkey
        AND ps_partkey=p_partkey
        AND ps_suppkey=s_suppkey
    GROUP BY s_name
   
    