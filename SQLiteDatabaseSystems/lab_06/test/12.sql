SELECT n_name
    FROM nation,orders,customer
     WHERE n_nationkey=c_nationkey
        AND c_custkey=o_custkey
        GROUP BY n_name 
        HAVING count(o_totalprice)=(SELECT count(o_totalprice)
                                    FROM nation,orders,customer
                                    WHERE c_custkey=o_custkey
                                    AND n_nationkey=c_nationkey
                                    GROUP BY n_name
                                    order BY count(o_totalprice))