.eqp on

DROP INDEX nation_idx_n_name;
DROP INDEX supplier_idx_s_nationkey_s_acctbal;

CREATE INDEX nation_idx_n_name ON nation(n_name);
CREATE INDEX supplier_idx_s_nationkey_s_acctbal ON supplier(s_nationkey);-- covering


select n_name, count(*) as cnt, max(s_acctbal)
from supplier, nation 
where s_nationkey = n_nationkey
group by n_name
having cnt > 5;
