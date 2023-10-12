.eqp on


CREATE INDEX supplier_idx_s_nationkey_s_acctbal ON supplier(s_acctbal);

select min(s_acctbal)
from supplier;
