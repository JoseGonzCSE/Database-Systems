SELECT  n_name, max(s_acctbal)
    FROM nation,supplier
    WHERE s_acctbal>9000
        AND n_nationkey=s_nationkey
    GROUP by n_name