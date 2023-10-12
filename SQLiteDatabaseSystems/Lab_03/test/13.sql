SELECT sum(c_acctbal)
    FROM region, customer,nation
    WHERE r_regionkey=n_regionkey AND r_name="ASIA" and c_nationkey=n_nationkey and c_mktsegment="MACHINERY"