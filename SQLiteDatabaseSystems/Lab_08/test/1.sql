.eqp on

CREATE INDEX customer_idx_c_name ON customer(c_name);


select c_address, c_phone, c_acctbal
from customer
where c_name='Customer#000000010';
