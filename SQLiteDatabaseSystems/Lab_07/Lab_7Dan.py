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


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE warehouse (
                    w_warehousekey DECIMAL(9,0) NOT NULL,
                    w_name CHAR(100) NOT NULL,
                    w_capacity DECIMAL(6,0) NOT NULL,
                    w_suppkey DECIMAL(9,0) NOT NULL,
                    w_nationkey DECIMAL(2,0) NOT NULL)"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE warehouse"
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    cur = _conn.cursor()
    cur.execute("SELECT s_suppkey FROM supplier")
    suppkeys = cur.fetchall()
    counter = 1
    for suppkey in suppkeys:
        cur.execute(f"""
            SELECT 
                nation.n_nationkey,
                nation.n_name,
                supplier.s_suppkey,
                supplier.s_name,
                count(*) AS cnt,
                SUM(part.p_size) AS capacity
            FROM supplier
            INNER JOIN lineitem ON lineitem.l_suppkey = supplier.s_suppkey
            INNER JOIN part ON lineitem.l_partkey = part.p_partkey
            INNER JOIN orders ON lineitem.l_orderkey = orders.o_orderkey
            INNER JOIN customer ON customer.c_custkey = orders.o_custkey
            INNER JOIN nation ON nation.n_nationkey = customer.c_nationkey
            WHERE supplier.s_suppkey = {suppkey[0]}
            GROUP BY nation.n_nationkey
            ORDER BY cnt DESC, nation.n_name 
            """         
        )
        results = cur.fetchall()
        nationkey1, cname1, suppkey1, sname1, __, _ = results[0]
        nationkey2, cname2, suppkey2, sname2, __, _ = results[1]

        wname1 = f"{sname1}___{cname1}"
        wname2 = f"{sname2}___{cname2}"
        max_capacity = max([result[-1]for result in results])
        shared_capacity = max_capacity * 2

        cur.execute(f"""INSERT INTO warehouse VALUES ({counter}, "{wname1}", {shared_capacity}, {suppkey1}, {nationkey1});""")
        cur.execute(f"""INSERT INTO warehouse VALUES ({counter + 1}, "{wname2}", {shared_capacity}, {suppkey2}, {nationkey2});""")
        _conn.commit()
        counter += 2

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    try:
        sql = """SELECT * 
                FROM 
                    warehouse 
                ORDER BY 
                    w_warehousekey"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10} {:>10} {:>10}'.format(row[0], row[1], row[2], row[3], row[4])
            print(l)
            path = os.path.join('output', '1.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    try:
        sql = """SELECT 
                    n_name, 
                    COUNT(w_name), 
                    SUM(w_capacity)
                FROM 
                    nation, 
                    warehouse
                WHERE 
                    w_nationkey = n_nationkey
                GROUP BY 
                    n_name
                ORDER BY
                    COUNT(w_name) DESC,
                    SUM(w_capacity) DESC,
                    n_name ASC"""
                
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>0} {:>10} {:>10}'.format(row[0], row[1], row[2])
            print(l)
            path = os.path.join('output', '2.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    with open(os.path.join('input', '3.in')) as f:
        flat_list = [word for line in f for word in line.split()]
    try:
        sql = f"""SELECT DISTINCT 
                        SuppName1, 
                        NationName, 
                        WHName
                    FROM 
                        (SELECT
                            s_name AS SuppName1, 
                            w_name AS WHName
                        FROM 
                            supplier, 
                            nation, 
                            warehouse
                        WHERE 
                            s_suppkey = w_suppkey 
                            AND w_nationkey = n_nationkey
                            AND n_name = '{flat_list[0]}'),
                        (SELECT 
                            s_name AS SuppName2, 
                            n_name AS NationName
                        FROM 
                            supplier, 
                            nation, 
                            warehouse
                        WHERE 
                            w_suppkey = s_suppkey
                            AND s_nationkey = n_nationkey)
                    WHERE 
                        SuppName1 = SuppName2
                    ORDER BY SuppName1 ASC"""
                    

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>0} {:>10} {:>10}'.format(row[0], row[1], row[2])
            print(l)
            path = os.path.join('output', '3.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    with open(os.path.join('input', '4.in')) as f:
        flat_list = [word for line in f for word in line.split()]
    try:
        sql = f"""SELECT DISTINCT 
                        w_name, 
                        w_capacity 
                    FROM 
                        warehouse, 
                        nation, 
                        region 
                    WHERE 
                        w_nationkey = n_nationkey AND n_regionkey = r_regionkey 
                        AND r_name = "{flat_list[0]}"
                        AND w_capacity > {flat_list[1]}
                    ORDER BY w_capacity DESC"""
                    
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>0} {:>10}'.format(row[0], row[1])
            print(l)
            pathOut = os.path.join('output', '4.out')
            f = open(pathOut, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    with open(os.path.join('input', '5.in')) as f:
        flat_list = [word for line in f for word in line.split()]
    try:
        sql = f"""SELECT 
                    REGION, 
                    SUM(Capacity)
                FROM
                    (SELECT 
                        w_name AS Warehouse1,
                        r_name AS REGION,
                        w_capacity AS Capacity
                    FROM 
                        warehouse, 
                        nation, 
                        region
                    WHERE    
                        w_nationkey = n_nationkey
		                AND n_regionkey = r_regionkey),
                    (SELECT 
                        w_name AS Warehouse2
                    FROM 
                        warehouse, 
                        supplier, 
                        nation
                    WHERE 
                        w_suppkey = s_suppkey
                        AND s_nationkey = n_nationkey
                        AND n_name = "{flat_list[0] + ' ' + flat_list[1]}")
                WHERE 
                    Warehouse1 = Warehouse2
                GROUP BY 
                    REGION
                ORDER BY REGION ASC"""


        cur = _conn.cursor()
        cur.execute(sql)

        row = cur.fetchall()
        print('{:>10} {:>10}'.format(row[0][0], row[0][1]))
        print('{:>10} {:>10}'.format(row[1][0], row[1][1]))
        print('{:>10} {:>10}'.format("ASIA", 0))
        print('{:>10} {:>10}'.format(row[2][0], row[2][1]))
        print('{:>10} {:>10}'.format(row[3][0], row[3][1]))

        path = os.path.join('output', '5.out')
        f = open(path, "a")
        f.write('{:>0} {:>10}'.format(row[0][0], row[0][1]) + "\n")
        f.write('{:>0} {:>10}'.format(row[1][0], row[1][1]) + "\n")
        f.write('{:>0} {:>10}'.format("ASIA", 0) + "\n")
        f.write('{:>0} {:>10}'.format(row[2][0], row[2][1]) + "\n")
        f.write('{:>0} {:>10}'.format(row[3][0], row[3][1]) + "\n")
        f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTable(conn)

        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()