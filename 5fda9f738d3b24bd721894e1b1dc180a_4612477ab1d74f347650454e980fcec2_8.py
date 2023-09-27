import pymysql
import string

class OpenMySQL:
    def __init__(self):
        self.db =  pymysql.connect(host='127.0.0.1', port=3308, user='root', passwd='root', db='library', charset='utf8')
        self.youbiao = self.db.cursor()  # 建立游标

    # 插入数据
    # 单条数据

    # 多条数据
    def insert_books(self,values):
        sql3 = "insert into books(book_id,title, author,isbn,status) values(%s, %s, %s, %s, %s)"
        self.youbiao.executemany(sql3, values)
        self.db.commit()

    def find_booksById(self,bookId):
        sql6 = "SELECT u.name,b.title,b.`status` " \
               "FROM `reservations` r left join books b on b.book_id=r.book_id " \
               "left join users u on u.user_id=r.user_id " \
               "where b.book_id=(%s)"
        self.youbiao.execute(sql6,bookId)
        all2 = self.youbiao.fetchall()
        print(all2)

    def find_books(self,parma):
        sql="SELECT u.name,b.title,b.`status` FROM `reservations` r left join books b on b.book_id=r.book_id left join users u on u.user_id=r.user_id"
        st= str(parma)[0:2]
        value= str(parma)[2:len(parma)]

        if st=="LB":
            sql=sql+" where b.book_id="+value
        elif  st=="LU" :
            sql=sql+" where u.user_id="+value
        elif st=='LR':
            sql = sql + " where r.reservation_id = " + value
        else:
            sql=sql+" where b.title like  '%"+parma+"%'"

        self.youbiao.execute(sql)
        all2 = self.youbiao.fetchall()
        if  len(all2)==0:
            print("not data")
        else :
            print(all2)

    def find_booksByAll(self):
        sql = "SELECT u.name,b.title,b.`status` " \
               "FROM `reservations` r left join books b on b.book_id=r.book_id " \
               "left join users u on u.user_id=r.user_id " \

        self.youbiao.execute(sql)
        all2 = self.youbiao.fetchall()
        print(all2)

    def amend_reservation(self,status,book_id):

        sql4 = "UPDATE books SET status =%s WHERE book_id = %s"
        self.youbiao.execute(sql4,(status,book_id))
        self.db.commit()

    def del_bookById(self,book_id):
        delBook = "delete from books b  where b.book_id= %s"

        delReser="delete from reservations r  where r.book_id= %s"
        self.youbiao.execute(delBook,book_id)
        self.youbiao.execute(delReser,book_id)
        self.db.commit()


    def close_vernier(self):
        self.youbiao.close()

    def close_db(self):
        self.db.close()

if __name__ == '__main__':
    o = OpenMySQL()
    # establish_mysql()
    # amend_mysql()

# 添加书数据
#     values = [(2,"C", "王教授","2222","LU"), (3,"java", "张教授","3333","LR"), (4,"java", "李教授","111","LR")]
#     o.insert_books(values)

# 根据书id查找
#     o.find_booksById(2)

# 根据条件查询
#     o.find_books("LB2")

# 三个表中查询书记录
#     o.find_booksByAll()

# 根据Book修改book status
#     o.amend_reservation("11",2)

# 根据book_id删除books表reservation表数据
    o.del_bookById(2)
    o.close_vernier()
    o.close_db()
    def del_bookById(self,book_id):
        delBook = "delete from books b  where b.book_id= %s"

        delReser="delete from reservations r  where r.book_id= %s"
        self.youbiao.execute(delBook,book_id)
        self.youbiao.execute(delReser,book_id)
        self.db.commit()


    def close_vernier(self):
        self.youbiao.close()

    def close_db(self):
        self.db.close()

if __name__ == '__main__':
    o = OpenMySQL()
    # establish_mysql()
    # amend_mysql()

# 添加书数据
#     values = [(2,"C", "王教授","2222","LU"), (3,"java", "张教授","3333","LR"), (4,"java", "李教授","111","LR")]
#     o.insert_books(values)

# 根据书id查找
#     o.find_booksById(2)

# 根据条件查询
#     o.find_books("LB2")

# 三个表中查询书记录
#     o.find_booksByAll()

# 根据Book修改book status
#     o.amend_reservati