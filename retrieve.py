import sqlite as sqliteconnection = sql.connect("movie.sql")
pointer = connection.cursor()
pointer.execute(
    "create table if not exists movie(movie_name varchar2(30),actor varchar2(15),actress varchar2(15),year number,director_name varchar2(15))"

)
pointer.execute("insert into movie values('happy death day','israel','jessica',2017,'christopher')")
pointer.execute("insert into movie values('KGF','yash','shrinidhi shetty',2018,'prashanth neel')")
pointer.execute("insert into movie values('KGF chapter2','yash','shrinidhi shetty',2022,'prashanth neel')")
pointer.execute("insert into movie values('Charlie','rakshith shetty','sangeetha',2022,'kiranraj')")
pointer.execute("insert into movie values('james','puneeth Rajkumar','Priya Anand',2022,'Chethan Kumar')")
print("List in DataBase")
print("-----------------------------------------------------------------------------------------------")
allMovies = pointer.execute("select * from movie").fetchall()
for i in allMovies:
    name,actor,actress,year,director_name = i
    print("{n}\t{a}\t{ac}\t{y}\t{d}".format(n=name,a=actor,ac=actress,y=year,d=director_name))
print("-----------------------------------------------------------------------------------------------")
print("query foe particular")
actorQuery = pointer.execute("select * from movies where ator = 'yash'").fetchall()
for i in actorQuery:  
    name,actor,actress,year,director_name = i
    print("{n}\t{a}\t{ac}\t{y}\t{d}".format(n=name,a=actor,ac=actress,y=year,d=director_name))
print("-------------------------------------END-------------------------------------------------------")