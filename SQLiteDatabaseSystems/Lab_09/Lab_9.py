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

def dropView(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop Views")

    _conn.execute("BEGIN")
    try:
        sql = "DROP VIEW IF EXISTS V1;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS V2;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS V5;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS V10;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS V151;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS V152;"
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def create_View1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V1")

    _conn.execute("BEGIN")
    try:
        sql = """CREATE VIEW V1(c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, c_nation, c_region) AS
                    SELECT c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, n_name, r_name
                    FROM customer, nation, region
                    WHERE r_regionkey = n_regionkey AND n_nationkey = c_nationkey"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V2")

    _conn.execute("BEGIN")
    try:
        sql = """CREATE VIEW V2(s_suppkey, s_name, s_address, s_phone, s_acctbal, s_comment, s_nation, s_region) AS
                    SELECT s_suppkey, s_name, s_address, s_phone, s_acctbal, s_comment, n_name, r_name
                    FROM supplier, nation, region
                    WHERE r_regionkey = n_regionkey AND n_nationkey = s_nationkey"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V5")

    _conn.execute("BEGIN")
    try:
        sql = """CREATE VIEW V5(o_orderkey, o_custkey, o_orderstatus, o_totalprice, o_orderyear, o_orderpriority, o_clerk, o_shippriority, o_comment) AS
                    SELECT o_orderkey, o_custkey, o_orderstatus, o_totalprice, SUBSTR(o_orderdate, 0, 5), o_orderpriority, o_clerk, o_shippriority, o_comment
                    FROM orders"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V10")

    _conn.execute("BEGIN")
    try:
        sql = """CREATE VIEW V10(p_type, min_discount, max_discount) AS
                    SELECT P1.p_type, MIN(l_discount), MAX(l_discount)
                    FROM part P1, lineitem
                    INNER JOIN part P2 ON P1.p_type = P2.p_type
                    WHERE P1.p_partkey = l_partkey
                    GROUP BY P1.p_type"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View151(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V151")

    _conn.execute("BEGIN")
    try:
        sql = """CREATE VIEW V151(c_custkey, c_name, c_nationkey, c_acctbal) AS
                    SELECT c_custkey, c_name, c_nationkey, c_acctbal
                    FROM customer
                    WHERE c_acctbal > 0"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View152(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V152")

    _conn.execute("BEGIN")
    try:
        sql = """CREATE VIEW V152(s_suppkey, s_name, s_nationkey, s_acctbal) AS
                    SELECT s_suppkey, s_name, s_nationkey, s_acctbal
                    FROM supplier
                    WHERE s_acctbal < 0"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    try:
        sql = """SELECT c_name, ROUND(SUM(o_totalprice), 2)
                FROM V1, orders
                WHERE (c_nation = 'FRANCE')
                    AND (c_custkey = o_custkey 
                        AND o_orderdate >= '1995-01-01' 
                        AND o_orderdate <= '1995-12-31')
                GROUP BY c_name"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}'.format(row[0], "|", row[1])
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
        sql = """SELECT s_region, COUNT(*)
                FROM V2
                GROUP BY s_region"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}'.format(row[0], "|", row[1])
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

    try:
        sql = """SELECT c_nation, COUNT(o_orderkey)
                FROM orders, V1
                WHERE (o_custkey = c_custkey
                        AND c_region = 'AMERICA')
                GROUP BY c_nation"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}'.format(row[0], "|", row[1])
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

    try:
        sql = """SELECT s_name, COUNT(*)
                FROM  partsupp, part, V2
                WHERE (s_nation = 'CANADA')
                    AND (s_suppkey = ps_suppkey
                        AND ps_partkey = p_partkey
                        AND p_size < 20)
                GROUP BY s_name"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}'.format(row[0], "|", row[1])
            print(l)
            path = os.path.join('output', '4.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    try:
        sql = """SELECT c_name, COUNT(*)
                FROM V1, V5
                WHERE (o_custkey = c_custkey
                        AND c_nation = 'GERMANY')
                    AND o_orderyear = '1993'
                GROUP BY c_name"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}'.format(row[0], "|", row[1])
            print(l)
            path = os.path.join('output', '5.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")

    try:
        sql = """SELECT s_name, o_orderpriority, COUNT(DISTINCT p_name)
                FROM supplier, nation, lineitem, part, partsupp, V5
                WHERE (s_nationkey = n_nationkey AND n_name = 'CANADA')
                    AND (n_nationkey = s_nationkey
                        AND s_suppkey = ps_suppkey
                        AND ps_partkey = p_partkey
                        AND l_partkey = p_partkey
                        AND l_orderkey = o_orderkey
                        AND ps_suppkey = l_suppkey)
                GROUP BY s_name, o_orderpriority"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}{}{}'.format(row[0], "|", row[1], "|", row[2])
            print(l)
            path = os.path.join('output', '6.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")

    try:
        sql = """SELECT c_nation, o_orderstatus, COUNT(*)
                FROM V1, V5
                WHERE (o_custkey = c_custkey
                        AND c_region = 'AMERICA')
                GROUP BY c_nation, o_orderstatus"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}{}{}'.format(row[0], "|", row[1], "|", row[2])
            print(l)
            path = os.path.join('output', '7.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")

    try:
        sql = """SELECT s_nation, COUNT(DISTINCT o_orderkey)
                FROM V2, V5, lineitem
                WHERE o_orderstatus = 'F'
                    AND o_orderyear = '1995'
                    AND (o_orderkey = l_orderkey
                        AND l_suppkey = s_suppkey)
                GROUP BY s_nation
                HAVING COUNT(DISTINCT o_orderkey) > 50"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}'.format(row[0], "|", row[1])
            print(l)
            path = os.path.join('output', '8.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")

    try:
        sql = """SELECT COUNT(DISTINCT o_clerk)
                FROM V2, V5, lineitem
                WHERE o_orderkey = l_orderkey
                    AND l_suppkey = s_suppkey
                    AND s_nation = 'UNITED STATES'"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}'.format(row[0])
            print(l)
            path = os.path.join('output', '9.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")

    try:
        sql = """SELECT p_type, min_discount, max_discount
                FROM V10
                WHERE p_type LIKE '%ECONOMY%' AND p_type LIKE '%COPPER%'
                GROUP BY p_type"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}{}{}'.format(row[0], "|", row[1], "|", row[2])
            print(l)
            path = os.path.join('output', '10.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")

    try:
        sql = """SELECT s_region, s_name, MAX(s_acctbal)
                FROM V2
                GROUP BY s_region"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}{}{}'.format(row[0], "|", row[1], "|", row[2])
            print(l)
            path = os.path.join('output', '11.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")

    try:
        sql = """SELECT s_nation, MAX(s_acctbal)
                FROM V2
                WHERE s_acctbal > 9000
                GROUP BY s_nation"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}'.format(row[0], "|", row[1])
            print(l)
            path = os.path.join('output', '12.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")

    try:
        sql = """SELECT COUNT(l_linenumber)
                FROM
                    orders,
                    lineitem,
                    (SELECT s_suppkey
                    FROM V2
                    WHERE s_region = 'AFRICA') S,
                    (SELECT c_custkey
                    FROM V1
                    WHERE c_nation = 'UNITED STATES') C
                WHERE o_orderkey = l_orderkey
                    AND S.s_suppkey = l_suppkey
                    AND C.c_custkey = o_custkey"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}'.format(row[0])
            print(l)
            path = os.path.join('output', '13.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")

    try:
        sql = """SELECT DISTINCT SuppRegion, CustRegion, MAX(o_totalprice)
                FROM 
                    (SELECT *, s_region AS SuppRegion
                        FROM V2, lineitem
                        WHERE l_suppkey = s_suppkey),
                    (SELECT *, c_region AS CustRegion
                        FROM V1, orders
                        WHERE o_custkey = c_custkey)
                WHERE l_orderkey = o_orderkey
                GROUP BY SuppRegion, CustRegion"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}{}{}{}{}'.format(row[0], "|", row[1], "|", row[2])
            print(l)
            path = os.path.join('output', '14.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")

    try:
        sql = """SELECT COUNT(DISTINCT o_orderkey)
                FROM orders, lineitem, V151, V152
                WHERE o_orderkey = l_orderkey
                    AND s_suppkey = l_suppkey
                    AND l_orderkey = o_orderkey
                    AND c_custkey = o_custkey"""

        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = '{}'.format(row[0])
            print(l)
            path = os.path.join('output', '15.out')
            f = open(path, "a")
            f.write(l + "\n")
            f.close()

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropView(conn)
        create_View1(conn)
        Q1(conn)

        create_View2(conn)
        Q2(conn)

        Q3(conn)
        Q4(conn)

        create_View5(conn)
        Q5(conn)

        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)

        create_View10(conn)
        Q10(conn)

        Q11(conn)
        Q12(conn)
        Q13(conn)
        Q14(conn)

        create_View151(conn)
        create_View152(conn)
        Q15(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
