SELECT p_mfgr
    FROM part,supplier,partsupp
    WHERE s_name= "Supplier#000000010"
        AND ps_partkey= p_partkey
        AND s_suppkey=ps_suppkey
        AND ps_availqty= (SELECT max(ps_availqty) 
                            FROM partsupp, supplier
                            WHERE s_name="Supplier#000000010"
                            AND ps_partkey= p_partkey
                            AND s_suppkey=ps_suppkey)
    limit 1