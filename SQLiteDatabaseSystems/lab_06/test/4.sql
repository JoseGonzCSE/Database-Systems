SELECT count(s_suppkey)
    FROM( SELECT s_suppkey
            FROM supplier
            INNER JOIN partsupp on ps_suppkey=s_suppkey
            INNER JOIN part on ps_partkey=p_partkey
            INNER JOIN nation on n_nationkey=s_nationkey
            WHERE n_name= "UNITED STATES"
            GROUP BY s_suppkey
            HAVING count(DISTINCT p_partkey)>=40)
            as results