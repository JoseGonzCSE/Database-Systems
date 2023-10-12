SELECT count(DISTINCT s_name)
    FROM supplier,part,partsupp
    WHERE p_type LIKE "%POLISHED%"
        AND p_partkey=ps_suppkey
        AND s_suppkey=ps_suppkey
        and p_size IN (3,23,36,49)