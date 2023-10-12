SELECT distinct n_name,count(s_name), min(s_acctbal)

    FROM nation,supplier
    WHERE (s_nationkey=n_nationkey) 
    GROUP BY n_name
    HAVING count(s_nationkey)>5