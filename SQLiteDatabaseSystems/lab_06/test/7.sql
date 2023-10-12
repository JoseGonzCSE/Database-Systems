SELECT count(*)
    FROM supplier
    WHERE s_name IN (SELECT s_name
                    FROM supplier,customer,orders,nation,lineitem
                    WHERE n_name IN("GERMANY","FRANCE")
                        and s_suppkey=l_suppkey
                        AND c_custkey=o_custkey
                        AND o_orderkey=l_orderkey
                        and n_nationkey=c_nationkey
                        group BY s_name HAVING count(distinct o_orderkey)<=50)