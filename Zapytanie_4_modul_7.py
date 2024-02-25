from sqlalchemy import func
from sql_alchemy import Grade, Student, Subject, Group, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example4.db', echo = True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# SELECT
#     group_id_id,
#     AVG(grade) AS average_grade_group,
#     (SELECT AVG(grade) FROM Grades) AS average_grade_scale
# FROM
#     Grades
# GROUP BY
#     group_id_id;

query_result = session.query(
    Grade.group_id_id, func.avg(Grade.grade).label('average_grade')
).group_by(Grade.group_id_id).all()



for row in query_result:
    print(row)