SELECT r_name,count(o_orderstatus)
    FROM region, orders,customer,nation
    WHERE o_orderstatus = "P" and n_nationkey=c_nationkey and n_regionkey=r_regionkey and o_custkey=c_custkey
    GROUP BY r_name