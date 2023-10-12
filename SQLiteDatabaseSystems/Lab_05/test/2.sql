SELECT r_name,count(s_suppkey)
    FROM supplier
    INNER join nation on s_nationkey=n_nationkey
    INNER JOIN region on n_regionkey=r_regionkey
    INNER JOIN( SELECT r_name as inner_r_name, avg(s_acctbal) as r_avg_acctbacl
                    FROM region,nation,supplier
                        WHERE r_regionkey=n_regionkey
                        AND s_nationkey=n_nationkey
                    GROUP by r_name)
                    AS avg_table on avg_table.inner_r_name=r_name
                    WHERE s_acctbal<avg_table.r_avg_acctbacl
                    GROUP by region.r_name;
   