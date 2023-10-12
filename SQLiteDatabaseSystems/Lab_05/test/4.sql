SELECT t_cust_counts.cust_n_name, t_cust _counts.cust_counts,t_supp_counts.supp_counts
FROM ( SELECT n_name as cust_n_name, count(c_custkey) as cust_counts
        FROM customer
        inner join nation ON c_nationkey=n_nationkey
        INNER join region on n_regionkey=r_regionkey
        WHERE r_name = "AFRICA"
        GROUP BY n_name) as t_cust_counts
    inner JOIN ( SELECT n_name as supp_n_name, count(s_suppkey)as supp_counts
                FROM supplier
                INNER JOIN nation ON s_nationkey=n_nationkey
                INNER JOIN region on n_regionkey=r_regionkey
                WHERE r_name= "AFRICA"
                GROUP BY n_name)AS t_supp_counts ON t_cust_counts.cust_n_name=t_supp_counts.supp_n_name;
    
  