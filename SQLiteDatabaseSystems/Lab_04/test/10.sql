SELECT DISTINCT P1.p_type, min(l_discount), max(l_discount)
    FROM part P1, lineitem
    INNER JOIN part P2 on P1.p_type = P2.p_type
    WHERE (P1.p_type LIKE '%ECONOMY%' AND P2.p_type LIKE '%COPPER%')
    AND l_partkey = P1.p_partkey
    group by P1.p_type