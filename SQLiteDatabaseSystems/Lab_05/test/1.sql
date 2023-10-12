SELECT count(distinct c_name) 
    FROM region,customer,nation
    WHERE r_name != "EUROPE"
        and r_name !="AFRICA"
        AND r_name != "ASIA"
        AND c_nationkey=n_nationkey
        AND n_regionkey=r_regionkey

        