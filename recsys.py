from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from collections import defaultdict

from surprise import SVDpp
from surprise import Dataset
from surprise import Reader

import pymysql
import pandas as pd

#import mysql.connector
from datetime import date, datetime, timedelta


user_id = []
category_id = []
score = []


def get_top_n(predictions, n=10):

    # First map the predictions to each user.
    top_n = defaultdict(list)

    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n] 

    return top_n



def get_user_id():
    conn = pymysql.connect(host='localhost', user='root', password='4106pysz',
                        db='cupid', charset='utf8')

    curs = conn.cursor()
    sql = "select creater_id from api_adtrade where status = 3"
    curs.execute(sql)

    rows = curs.fetchall()
    
    for i in rows:
        user_id.append(i[0])

    conn.close()

def get_category_id():
    conn = pymysql.connect(host='localhost', user='root', password='4106pysz',
                        db='cupid', charset='utf8')

    curs = conn.cursor()
    sql = "select ad_id from api_adtrade where status = 3"
    curs.execute(sql)

    rows = curs.fetchall()
    
    for i in rows:
        sql = "select category_id from api_ads where id = " + str(i[0])
        curs.execute(sql)
        result = curs.fetchall()
        for j in result:
            category_id.append(j[0])

    conn.close()

def get_score():
    conn = pymysql.connect(host='localhost', user='root', password='4106pysz',
                        db='cupid', charset='utf8')

    curs = conn.cursor()
    sql = "select score from api_adtrade where status = 3"
    curs.execute(sql)

    rows = curs.fetchall()
    
    for i in rows:
        score.append(i[0])


    conn.close()       

def recommended():
    # ratings_dict = {'userID': category_id,
    #                 'itemID': user_id,
    #                 'rating': score }
    ratings_dict = {'userID': [1, 2, 2, 3, 4, 1, 2, 3, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3],
                    'itemID': [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6],
                    'rating': [3, 2, 2, 2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3]}
    df = pd.DataFrame(ratings_dict)

    reader = Reader(rating_scale=(1, 3))
    data = Dataset.load_from_df(df[['userID', 'itemID', 'rating']], reader)

    trainset = data.build_full_trainset()
    algo = SVDpp()
    algo.train(trainset)

    testset = trainset.build_anti_testset() + trainset.build_testset()
    #print(testset)
    predictions = algo.test(testset)

    top_n = get_top_n(predictions, n=10)

    tomorrow = datetime.now().date() + timedelta(days=1)

    # add_employee = ("INSERT INTO employees "
    #             "(first_name, last_name, hire_date, gender, birth_date) "
    #             "VALUES (%s, %s, %s, %s, %s)")
    # add_salary = ("INSERT INTO salaries "
    #             "(emp_no, salary, from_date, to_date) "
    #             "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

    data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

    data_salary = {
        #'emp_no': emp_no,
        'salary': 50000,
        'from_date': tomorrow,
        'to_date': date(9999, 1, 1),
    }


    conn = pymysql.connect(host='localhost', user='root', password='4106pysz',
                        db='cupid', charset='utf8')


    for uid, user_ratings in top_n.items():
        t = [est for (est, _) in user_ratings]
        str1 = ','.join(str(e) for e in t)
        # #print(str1)
        curs = conn.cursor()

        sql = 'insert into api_recommend (id, adbos_id, recommend) values (NULL, '+ str(uid)+', "'+str1+'")'
        curs.execute(sql)
        conn.commit()
        print(sql)

    conn.close()

if __name__ == "__main__":
    #recommended()
    get_user_id()
    get_category_id()
    get_score()
    recommended()
    #print(score, category_id, user_id)