/*SELECT n_name
    from nation, customer
    WHERE n_nationkey=c_custkey
    GROUP by n_name
    HAVING count(c_custkey)= (SELECT count(c_custkey)
                                FROM nation,customer
                                WHERE n_nationkey=c_custkey
                                GROUP BY n_name
                                ORDER BY count(c_custkey)DESC limit 1)*/
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