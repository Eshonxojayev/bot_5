# import psycopg2 as psql
# import os
#
# class Database:
#     @staticmethod
#     def connect(query):
#         db = psql.connect(
#             database="group_34",
#             host="localhost",
#             user="postgres",
#             password=os.getenv('DB_USER_PASSWORD')
#         )
#
#         cursor = db.cursor()
#         cursor.execute(query)
#         db.commit()
#         return "Succesfull"