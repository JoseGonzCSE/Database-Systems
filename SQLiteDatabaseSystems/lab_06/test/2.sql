SELECT count(results.c_custkey)
    FROM (SELECT c_custkey 
            FROM customer
            INNER JOIN orders on c_custkey=o_custkey
            WHERE strftime("%Y-%m",o_orderdate)="1995-11"
            GROUP BY c_custkey
            HAVING count(c_custkey)>=3) as results