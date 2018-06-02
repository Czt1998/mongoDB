#codeing utf -8
import os
from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017/')
db = conn.mydb # 连接数据库名
def main():
    work_dir = '/home/czt/PycharmProjects/untitled/campany_2010'
    for parent, dirnames, filenames in os.walk(work_dir):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            print('文件名：%s' % filename)
            print('文件完整路径：%s\n' % file_path)
            movie_name = filename.split('.')[0]
            name = {}
            with open(file_path) as w:
                line = w.read()
                # print(line)
                # print(type(line))
            name[movie_name] = line
            db.col.insert(name)
    # db.col.remove()
    for item in db.col.find():
        print(item)
        print('\n')


if __name__ == '__main__':
    main()

