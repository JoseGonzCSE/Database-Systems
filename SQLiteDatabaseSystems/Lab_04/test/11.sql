SELECT r_name,s_name,max(s_acctbal)
    FROM region,supplier,nation
    WHERE n_nationkey=s_nationkey
        AND r_regionkey=n_regionkey
    group BY r_name