SELECT s_name,c_name,o_totalprice
    FROM supplier,customer,orders,lineitem
    WHERE o_totalprice=(SELECT min(o_totalprice)
                        FROM orders
                        WHERE o_orderstatus="F")
        and s_suppkey=l_suppkey
        AND c_custkey=o_custkey
        AND o_orderkey=l_orderkey
        GROUP by s_name
        ORDER by o_totalprice DESC
       