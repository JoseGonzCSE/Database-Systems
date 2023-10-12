.eqp on


DROP INDEX customer_idx_c_mktsegment;
DROP INDEX region_idx_r_name_r_regionkey;
DROP INDEX nation_idx_n_regionkey_n_nationkey;



CREATE INDEX customer_idx_c_mktsegment ON customer(c_mktsegment);
CREATE INDEX region_idx_r_name_r_regionkey ON region(r_name);--covering
CREATE INDEX nation_idx_n_regionkey_n_nationkey ON nation(n_regionkey,n_nationkey);--covering


select sum(c_acctbal)
from customer, region, nation
where c_nationkey = n_nationkey
    and n_regionkey = r_regionkey
    and r_name = 'EUROPE'
    and c_mktsegment = 'MACHINERY';
