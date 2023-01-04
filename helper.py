import mysql.connector as connector

rec=[]
class Student:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                    user='root',
                                    password='Suyash1855@',
                                    database='StudentRecord')
        query="""create table if not exists user2( Personid int NOT NULL AUTO_INCREMENT, name varchar(200), 
        enrollmentno varchar(10), birthDate varchar(10), Fathername varchar(200), course varchar(200), 
        feestatus varchar(100), gender varchar(10), semester varchar(10), email varchar(200), PRIMARY KEY (Personid))"""

        cur= self.con.cursor()
        cur.execute(query)
        print("created")

    def insert_student(self,  name, enrollmentno, birthDate,Fathername, course, feestatus, gender, semester, email):
        query= """insert into user2( name, enrollmentno, birthDate, Fathername, course, feestatus, gender, semester, email)values
        ('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format( name, enrollmentno, birthDate, Fathername, course,
         feestatus, gender, semester, email)

        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("inserted")
    def fetch_all(self,enrol):
        query="select * from user2 where enrollmentno='{}'".format(enrol)
        cur= self.con.cursor()
        cur.execute(query)
        for row in  cur:
            for i in range(0,10):
                rec.insert(i, row[i])

    def delete_user(self, userId):
        query= " delete from student where userId= {}".format(userId)
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()

S1= Student()
# S1.insert_student("Suyash Vishwakarma", "8000448003", "27/02/2003", "NandKumar", "BSC_ECM", "Paid", "Male", "3rd_Sem", "sanvishw@gmail.com")
# S1.insert_student("Durgesh Khanna", "8000448000", "27/11/2003", "Ajey Khanna", "Itegrated M_tech", "Paid", "Male", "3rd_Sem", "dugesh@gmail.com")
# S1.insert_student("Aviral Dubey", "8000448001", "5/04/2003", "Sunil Dubey", "BSC_ECM", "Paid", "Male", "3rd_Sem", "aviral@gmail.com")
# S1.insert_student("Ashutosh Singh", "8000448002", "17/12/2002", "Ram Singh", "BSC_ECM", "Paid", "Male", "3rd_Sem", "ashu@gmail.com")
# S1.insert_student("Semon Bhatia", "8000448004", "2/05/2003", "Harjeet Singh Bhatia", "BSC_ECM", "Paid", "Female", "3rd_Sem", "simran@gmail.com")
# S1.insert_student("Surya Ambaselkar", "8000448005", "7/04/2003", "Vinay Ambaselkar", "Itegrated M_tech", "Paid", "Female", "3rd_Sem", "shouryaa@gmail.com")
# S1.insert_student("Jayesh Janardhan", "8000448006", "20/12/2003", "Sam Janardhan", "Itegrated M_tech", "Paid", "Male", "3rd_Sem", "jayesh@gmail.com")
# S1.insert_student("Vatasala Garg ", "8000448007", "29/02/2004", "P Garg", "Itegrated M_tech", "Paid", "Male", "3rd_Sem", "vat@gmail.com")
# S1.insert_student("Avneet Kaur", "8000448008", "10/02/2003", "Harvinder Kaur", "BSC_ECM", "Paid", "Female", "3rd_Sem", "avneet@gmail.com")
# S1.insert_student( "khushi Vishwakarma", "8000448009", "9/06/2002", "Lakhan Vishwakarma", "Itegrated M_tech", "Paid", "Female", "3rd_Sem", "khushVish@gmail.com")

# S1.delete_user(11)
