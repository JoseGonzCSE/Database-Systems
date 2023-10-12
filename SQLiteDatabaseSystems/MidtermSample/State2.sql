
--question 1

SELECT DISTINCT makers
FROM products, laptop
    WHERE pmodel=laptopmodel
        AND lscreen>15
        AND lprice<1000

--question 2
SELECT M,count()
FROM (SELECT pmaker as m 
        FROM product,pc 
        WHERE pmodel=pcmodel
            AND pcspeed>2.0
        UNION
        select pmaker
        FROM product,laptop
        WHERE pmodel=lmodel
            AND lhd>250
        UNION
        select pmaker
        from product,printer
        where pmodel=printermodel
            and ptype="laser"
    



--question 3

SELECT avg(price)
FROM product,Pc 
    WHERE productmodel=pcmodel
        and pcram>4gb


--question 4

SELECT distinct pmakers 
FROM products
    where ptype="pc"
    union SELECT pmaker
        FROM products
        WHERE ptype="laptop"
    EXCLUDE
    SELECT pmaker
    from products
    where ptype="printer"

--question 5

SELECT count(distinct p_maker)
FROM product
WHERE p_maker in (SELECT p_maker
                    FROM product
                    WHERE ptype=pc)
    and where p_maker in (select p_maker
                            from product
                            where ptype=laptop)

--question 6
SELECT sum(m)
FROM (SELECT min(price) as m
        FROM Pc 
        Union
        select min(price)
        from laptop
        UNION
        SELECT min(price)
        from printer)
    



--question 7
SELECT min(m) 
FROM (SELECT min(pric


--question 8

SELECT distinct maker
FROM product,pc    
    WHERE ptype="printer"
        AND pmaker in (SELECT max(price)
                            from pc )



