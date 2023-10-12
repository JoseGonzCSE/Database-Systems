SELECT count(DISTINCT s_suppkey)
    FROM supplier
    INNER JOIN partsupp on ps_suppkey=s_suppkey
    INNER join part on ps_partkey=p_partkey
    INNER JOIN nation on n_nationkey=s_nationkey
    WHERE p_retailprice=(SELECT max(p_retailprice) 
                            FROM part)