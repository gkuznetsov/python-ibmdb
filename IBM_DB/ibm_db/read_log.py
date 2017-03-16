#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import config

def main():
    import ibm_db
    conn = ibm_db.connect('SAMPLE', 'db2inst1', 'kgg1024')
    #conn = ibm_db.connect(config.database, config.user, config.password)

    result = ibm_db.exec_immediate(conn, "ALTER TABLE emp_resume DATA CAPTURE CHANGES;")
    result = ibm_db.exec_immediate(conn, "COMMIT;")
    result = ibm_db.exec_immediate(conn, "INSERT INTO emp_resume VALUES('000120', 'ascii', 'This is a new resume2.');")
    result = ibm_db.exec_immediate(conn, "INSERT INTO emp_resume VALUES('000030', 'ascii', 'This is another new resume2');")
    result = ibm_db.exec_immediate(conn, "COMMIT;")
    result = ibm_db.exec_immediate(conn, "DELETE FROM emp_resume WHERE empno = '000120';")
    result = ibm_db.exec_immediate(conn, "COMMIT;")
    result = ibm_db.exec_immediate(conn, "DELETE FROM emp_resume WHERE empno = '000030';")
    result = ibm_db.exec_immediate(conn, "COMMIT;")
    teststr = "sdfasfasfs"
    ibm_db.close(conn)
    ibm_db.read_log_record(teststr, teststr)

if __name__ == '__main__':
    main()
