SELECT count(p_partkey)
    FROM (SELECT p_partkey
            FROM supplier
            inner JOIN partsupp on ps_suppkey=s_suppkey
            INNER JOIN part on ps_partkey=p_partkey
            inner JOIN nation on n_nationkey= s_nationkey
            WHERE n_name= "UNITED STATES"
            GROUP BY p_partkey
            HAVING count(DISTINCT s_suppkey)=2)
            as results