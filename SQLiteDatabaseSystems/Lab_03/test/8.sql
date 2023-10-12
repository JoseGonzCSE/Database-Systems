SELECT s_name,s_acctbal
    FROM supplier,region,nation
    WHERE (s_acctbal >7000)AND(r_name="EUROPE") AND r_regionkey=n_regionkey AND n_nationkey=s_nationkey;