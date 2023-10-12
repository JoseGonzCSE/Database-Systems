SELECT nation1, -(dif1- dif2)
FROM (SELECT n_name AS nation1, count(l_quantity) AS dif1
      FROM customer, orders, lineitem, supplier, nation
      WHERE c_custkey = o_custkey
            AND l_orderkey = o_orderkey
            AND l_suppkey = s_suppkey
            AND s_nationkey != n_nationkey
            AND c_nationkey = n_nationkey
            AND l_shipdate LIKE '%1994%'
      GROUP BY n_name), 
      (SELECT n_name AS nation2, count(l_quantity) AS dif2
       FROM customer, orders, lineitem, supplier, nation
       WHERE c_custkey = o_custkey
             AND l_orderkey = o_orderkey
             AND l_suppkey = s_suppkey
             AND c_nationkey != n_nationkey
             AND s_nationkey = n_nationkey
             AND l_shipdate LIKE '%1994%'
             GROUP BY n_name)
WHERE nation1 = nation2;