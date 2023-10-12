 
-- Question 1

SELECT P_makers
    FROM Product,Laptops
        WHERE P_model= L_model
            AND L_screen <"15''"
            AND L_price<1000


  


--Question 2

SELECT count(DISTINCT P_makers)
    FROM Product,PC,Laptop,Printer
        WHERE P_model=Pc_model
            AND p_model=Laptop_model
            and p_model=printer_model
            AND Pc_speed>2.0
            AND Laptop_hd>250
            AND Printer_type="laser"

SELECT M,count()
    FROM (
        SELECT p_maker as M
        FROM Product, Pc 
            WHERE p_model=pc_model
                AND pc_speed>2.0
        UNION
        SELECT p_maker
        FROM product, laptop
            where p_model=pc_model
                AND lap_hd>250
                UNION
        SELECT p_maker
        from product, printer
            where p_model=printer_model
                AND printer.type="laser"
                    

--Question 3

SELECT Product_maker,avg(PC_Price)
    FROM Product,PC
    WHERE P_model=Pc_model
        AND Pc_ram > 4
    GROUP BY P_maker
    HAVING Pc_ram >4


--Question 4

SELECT P_maker
FROM Product
    WHERE p_type="PC" 
    UNION ALL
    SELECT p_maker
    FROM product
    WHERE p_typer="laptop"
    EXCEPT ( SELECT p_maker
                FROM Product
                WHERE p_type ="Printers")

-- Question 5 

SELECT count(distinct p_maker)
    FROM product
    WHERE p_maker in( SELECT p_maker
                        FROM product
                            where P_type="PC")
    AND p_maker in (SELECT p_maker
                        FROM product
                            where P_type="Laptop")
    AND p_maker in (SELECT p_maker
                        FROM product
                            where P_type="Printer")

-- Question 6

SELECT sum(C)
    FROM ( SELECT min(price) as C
            from PC 
            UNION ALL
            select min(price) 
            from laptop
            union ALL 
            select min(price)
            from printer
    

-- Question 7

SELECT Min(p)
    FROM (SELECT distinct product.maker as M, laptop.price as p 
            from laptop,product
            WHERE product_model=l_modle)
            SELECT distinct product.maker as N 
                from product
                where product type="pc"
    where M=N 

--Question 8

SELECT distinct maker
    FROM Product,PC
    WHERE P_model=pc_mdoel
        AND p_type ="printer"
        AND p_maker in ( SELECT max(PC_price)
                        from PC)