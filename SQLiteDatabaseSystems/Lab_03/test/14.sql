SELECT count(o_orderpriority)
    FROM nation,customer,orders
    WHERE n_name= "PERU" AND (o_orderdate like "%1995%" or o_orderdate like "%1996%" or o_orderdate like "%1997%")
        AND o_orderpriority="1-URGENT"
        AND n_nationkey=c_nationkey AND o_custkey=c_custkey