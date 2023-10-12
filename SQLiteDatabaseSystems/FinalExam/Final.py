import sqlite3
from sqlite3 import Error
import os


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn


def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def build_data_cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("BUILD DATA CUBE")


    _conn.execute("BEGIN")
    try:
        sql = """INSERT INTO price_cube
                select dist.name, prod.name, count(prod.name),total
                FROM (select 'ALL' as name
                        from distributor dist1
                            where dist1.name like '%A%'
                    UNION ALL 
                    select 'D' as name
                        from distributor dist2
                            where dist2.name like '%D%'
                    UNION ALL
                    select  'P' as name
                        FROM distributor dist3
                            where dist3.name like '%D%') as dist,
                    (select 'ALL' as name
                    FROM 
                        (select name 
                            from  product prod1, distributor distt1
                                where distt1.name = prod1.maker 
                                    and prod1.type = 'laptop'
                        UNION
                        select name
                            from product prod2, distributor distt2
                            where distt2.name = prod2.maker 
                                and prod2.maker.type = 'pc'
                        UNION
                        select name
                            from product prod3, distributor distt3
                            where distt3.name = prod3.maker 
                                and prod3.type = 'printer')
                    UNION ALL 
                    select   'laptop' as name 
                            from product prod1, distributor distt1
                            where distt1.name = prod1.maker 
                                and prod1.type = 'laptop'
                    UNION ALL
                    select 'pc' as name
                            from product prod2, distributor distt2
                            where distt2.name = prod2.maker 
                                and prod2.type = 'pc'
                    UNION ALL
                    select sum(price) as total
                            from product prod1, distributor distt1
                            where distt1.name = prod1.maker 
                                and prod1.type = 'laptop'
                    UNION ALL
                    select sum(price) as total
                            from product prod2, distributor distt2
                            where distt2.name = prod2.maker 
                                and prod2.type = 'pc'
                group by dist.name, prod.name"""
        _conn.execute(sql)
        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)





    print("++++++++++++++++++++++++++++++++++")


def print_Product(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT PRODUCT")


    try:
        sql = """select * from product"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:<20} {:<20} {:<20}'.format("model", "type", "maker")
        print(l)

        rows = cur.fetchall()

        for row in rows:
            l2 = '{:<20} {:<20} {:<20}'.format(row[0], row[1], row[2])
            print(l2)
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def print_Distributor(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT DISTRIBUTOR")

    try:
        sql = """select * from distributor"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        l = '{:<20} {:<20} {:>20}'.format("model", "name", "price")
        print(l)

        main = [list(x) for x in rows]
        for j in range( len( main ) ):

            for k in range( len( main[j] ) ):
                    if main[j][k] == None:
                        main[j][k] = "null"
                    else:
                        continue

        rows= tuple( tuple(y) for y in main )

        print("--------------------------------------------------------")

        for row in rows:
            l2 = '{:<20} {:<20} {:<20}'.format(row[0], row[1], row[2])
            print(l2)
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def print_Cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT DATA CUBE")



    cur=_conn.cursor()

    _conn.execute("BEGIN")
    try:
        sql = """select * From price_cube"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    rows=cur.fetchall()



    l = '{:<20} {:<20} {:>10} {:>10}'.format("dist", "prod", "cnt", "total")
    print(l)

    print("++++++++++++++++++++++++++++++++++")


def modifications(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("MODIFICATIONS")

   # with open('modifications.txt','r') as file:
    #    contents=file.read()
    #    all=contents.split()
    #    table=all[0] #gives the table
    #    Operations=all[1] # gives the operation Delete or Insert
     #   one= all[2]
     #   two= all[3]
     #   three=all[4]

      #  if table== "Product":
      #      if Operations == "I": 
      #          sql= """insert into product(model,type,maker) 
      #                values(one,two,three) """  
       #         _conn.execute(sql)  
      #      elif Operations == "D":
       #         sql= """ Delete FROM product
       #                 where model= one"""    
       #         _conn.execute(sql)

       # elif table=="Distributor":
       #     if Operations == "I":
        #        sql= """insert into distributor(model,name,price)
        #            values (one,two,three)"""
        #        _conn.execute(sql)
        #    elif Operations == "D":
        #        sql= """ Delete FROM distributor
        #                where model= one"""    
        #        _conn.execute(sql)




    print("++++++++++++++++++++++++++++++++++")



def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        print_Product(conn)
        print_Distributor(conn)

        build_data_cube(conn)
        print_Cube(conn)

        modifications(conn)

        print_Product(conn)
        print_Distributor(conn)
        print_Cube(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
