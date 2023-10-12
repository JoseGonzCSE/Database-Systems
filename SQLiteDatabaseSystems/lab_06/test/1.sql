SELECT strftime("%m",l_shipdate)as month,sum(l_quantity)
FROM lineitem
WHERE strftime("%Y",l_shipdate)= "1995"
group by month 