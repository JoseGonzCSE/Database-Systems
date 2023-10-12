.eqp on
DROP INDEX region_idx_r_name_r_regionkey;
DROP INDEX nation_idx_n_regionkey_n_nationkey;
DROP INDEX customer_idx_c_nationkey_c_custkey;
DROP INDEX orders_idx_o_custkey_o_orderdate;

CREATE INDEX region_idx_r_name_r_regionkey ON region(r_name);--covering
CREATE INDEX nation_idx_n_regionkey_n_nationkey ON nation(n_regionkey);--covering
CREATE INDEX customer_idx_c_nationkey_c_custkey ON customer(c_nationkey);--covering
CREATE INDEX orders_idx_o_custkey_o_orderdate ON orders(o_custkey,o_orderdate,o_orderdate);

select sum(o_totalprice)
from orders, customer, nation, region
where o_custkey=c_custkey and
    c_nationkey=n_nationkey and
    r_regionkey=n_regionkey and
    r_name='AMERICA' and
    o_orderdate>='1996-01-01' and o_orderdate<='1996-12-31';
