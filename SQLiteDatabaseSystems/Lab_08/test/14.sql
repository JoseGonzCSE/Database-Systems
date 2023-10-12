.eqp on


DROP INDEX orders_idx_o_orderpriority_o_orderdate;
DROP INDEX nation_idx_n_name;
DROP INDEX customer_idx_c_nationkey_c_custkey;

CREATE INDEX orders_idx_o_orderpriority_o_orderdate ON orders(o_orderpriority,o_orderdate,o_orderdate);
CREATE INDEX nation_idx_n_name ON nation(n_name);
CREATE INDEX customer_idx_c_nationkey_c_custkey ON customer(c_nationkey,c_custkey);



select count(o_orderkey)
from orders, customer, nation
where c_custkey=o_custkey
    and c_nationkey=n_nationkey
    and n_name='BRAZIL'
    and o_orderpriority='1-URGENT'
    and o_orderdate >= '1994-01-01' and o_orderdate <= '1997-12-31';
