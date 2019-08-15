import re
import sqlite3

conn = sqlite3.connect('naverDS.sqlite')
cur = conn.cursor()
#커서는 프로그램 잘 돌아가게 해주는 것!
# Make some fresh tables using executescript()

cur.executescript('''
DROP TABLE IF EXISTS Age;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Gender;
DROP TABLE IF EXISTS Merital;
DROP TABLE IF EXISTS Parenthood;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS User;

CREATE TABLE Age (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    howOld    INTEGER UNIQUE
);

CREATE TABLE Country (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    countryName   TEXT UNIQUE
);

CREATE TABLE Gender (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    sex   TEXT UNIQUE
);

CREATE TABLE Merital (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    marriedQ   TEXT UNIQUE
);

CREATE TABLE Parenthood (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    parent   TEXT UNIQUE
);

CREATE TABLE Category (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    categoryName   TEXT UNIQUE
);

CREATE TABLE User (
    ages_id  INTEGER,
    country_id INTEGER,
    gender_id INTEGER,
    married_id INTEGER,
    parents_id INTEGER,
    category_id INTEGER
);

''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'naver_DS2.csv'
hand = open(fname)
entry = dict()
realData = dict()
temp={}
ageLi = list()
conLi = list()
sexLi = list()
merLi = list()
parLi = list()
catLi = list()
Final_hi = list()
i=0
for sp in hand:
    entry = sp.split()
    for getData in entry:
        realData = getData.split(',')
        try:
            ageLi.append(realData[1])
        except:
            ageLi.append('NULL')
        try:
            conLi.append(realData[2])
        except:
            conLi.append('NULL')
        try:
            sexLi.append(realData[3])
        except:
            sexLi.append('NULL')
        try:
            merLi.append(realData[4])
        except:
            merLi.append('NULL')
        try:
            parLi.append(realData[5])
        except:
            parLi.append('NULL')
        try:
            catLi.append(realData[12])
        except:
            catLi.append('NULL')

        temp['나이']=realData[1]
        temp['국적']=realData[2]
        temp['성별']=realData[3]
        temp['결혼유무']=realData[4]
        temp['부모님']=realData[5]
        temp['행복의기준']=realData[12]
        Final_hi.append(temp)
        i = i+1
        print(temp)


        cur.execute('''INSERT OR IGNORE INTO Age (howOld)
            VALUES ( ? )''', ( realData[1], ) )
        cur.execute('SELECT id FROM Age WHERE howOld = ? ', (realData[1], ))
        ages_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Country (countryName)
            VALUES ( ? )''', ( realData[2], ) )
        cur.execute('SELECT id FROM Country WHERE countryName = ? ', (realData[2], ))
        country_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Gender (sex)
            VALUES ( ? )''', ( realData[3], ) )
        cur.execute('SELECT id FROM Gender WHERE sex = ? ', (realData[3], ))
        gender_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Merital (marriedQ)
            VALUES ( ? )''', ( realData[4], ) )
        cur.execute('SELECT id FROM Merital WHERE marriedQ = ? ', (realData[4], ))
        married_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Parenthood (parent)
            VALUES ( ? )''', ( realData[5], ) )
        cur.execute('SELECT id FROM Parenthood WHERE parent = ? ', (realData[5], ))
        parents_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Category (categoryName)
            VALUES ( ? )''', ( realData[12], ) )
        cur.execute('SELECT id FROM Category WHERE categoryName = ? ', (realData[12], ))
        category_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO User
            (ages_id,country_id, gender_id, married_id, parents_id, category_id)
            VALUES ( ?, ?, ?, ?, ?, ? )''',
            ( ages_id,country_id, gender_id, married_id, parents_id, category_id ) )
        conn.commit()
