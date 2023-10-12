SELECT DISTINCT substr(l_receiptdate,1,7), count(*)
    FROM customer,lineitem,orders
    WHERE c_name="Customer#000000020"
        AND o_custkey=c_custkey
        AND o_orderkey=l_orderkey
    GROUP by substr(l_receiptdate,1,7)
