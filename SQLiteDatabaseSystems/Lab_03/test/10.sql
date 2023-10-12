SELECT sum(o_totalprice) 
    FROM orders,customer,nation,region
    WHERE (r_name="ASIA" AND o_orderdate like"%1997%" AND c_custkey=o_custkey AND n_nationkey=c_nationkey AND n_regionkey=r_regionkey)