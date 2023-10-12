SELECT r_name,count(*)
    FROM supplier,region,nation
    WHERE r_regionkey=n_regionkey
         AND s_nationkey=n_nationkey
    GROUP BY r_name
        