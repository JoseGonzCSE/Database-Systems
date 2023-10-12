.eqp on

DROP INDEX orders_idx_o_orderstatus;
DROP INDEX customer_idx_c_custkey;
DROP INDEX nation_idx_n_nationkey_n_name;
DROP INDEX region_idx_r_regionkey_r_name;



CREATE INDEX orders_idx_o_orderstatus ON orders(o_orderstatus);
CREATE INDEX customer_idx_c_custkey ON customer(c_custkey);
CREATE INDEX nation_idx_n_nationkey_n_name ON nation(n_nationkey);
CREATE INDEX region_idx_r_regionkey_r_name ON region(r_regionkey);--covering



select r_name, count(*) as cnt_ord
from orders, customer, nation, region
where o_custkey=c_custkey
    and c_nationkey=n_nationkey
    and n_regionkey=r_regionkey
    and o_orderstatus='F'
group by r_name;

