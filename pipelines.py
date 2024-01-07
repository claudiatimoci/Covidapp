# Define your item pipelines here

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# import sqlalchemy as db

# class WebcrawlerPipeline:
#     def process_item(self, item, spider):
#         return item

# class DataBase():
#     def __init__(self, name_database='Covid'):
#         self.name = name_database
#         self.url = f"sqlite:///{name_database}.db"
#         self.engine = db.create_engine(self.url)
#         self.connection = self.engine.connect()
#         self.metadata = db.MetaData()
#         self.table = self.engine.table_names()

#     def create_table(self, name_table, **kwargs):
#         columns = [db.Column(k, v, primary_key=True) if 'id_' in k else db.Column(k, v) for k, v in kwargs.items()]
#         db.Table(name_table, self.metadata, *columns)
#         self.metadata.create_all(self.engine)
#         print(f"Table '{name_table}' has been created successfully")

#     def read_table(self, name_table, return_keys=False):
#         table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
#         if return_keys:
#             return table.columns.keys()
#         else:
#             return table

#     def add_row(self, name_table, **kwargs):
#         table = self.read_table(name_table)
#         stmt = db.insert(table).values(kwargs)
#         self.connection.execute(stmt)
#         print('Row added')

#     def delete_row_by_id(self, name_table, id_):
#         table = self.read_table(name_table)
#         stmt = db.delete(table).where(table.c.id_ == id_)
#         self.connection.execute(stmt)
#         print(f'Row id {id_} deleted')

#     def select_table(self, name_table):
#         table = self.read_table(name_table)
#         stm = db.select([table])
#         result = self.connection.execute(stm).fetchall()
#         return result


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
 
 
# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import sqlalchemy as db
 
 
# class covidPipeline:
#     def process_item(self, item, spider):
#         return item
# class DataBase():
#     def __init__(self, name_database='Covid'):
#         self.name = name_database
#         self.url = f"sqlite:///{name_database}.db"
#         self.engine = db.create_engine(self.url)
#         self.connection = self.engine.connect()
#         self.metadata = db.MetaData()
 
#         # Charger les tables existantes dans la base de données
#         self.metadata.reflect(bind=self.engine)
 
#         # Obtenir la liste des noms de tables
#         self.table_names = list(self.metadata.tables.keys())
 
 
#     def create_table(self, name_table, **kwargs):
#         if name_table not in self.table_names:
#             columns = [db.Column(k, v) for k, v in kwargs.items()]
#             table = db.Table(name_table, self.metadata, *columns)
#             table.create(self.engine, checkfirst=True)
#             print(f"Table '{name_table}' created successfully")
#         else:
#             print(f"Table '{name_table}' already exists")
 
#     # def read_table(self, name_table, return_keys=False):
#     #     table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
#     #     if return_keys:table.columns.keys()
#     #     else : return table
            
#     def get_table_names(self):
#         return self.table_names

            
#     def read_table(self, name_table=None, return_keys=False):
#         if name_table:
#             table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
#             if return_keys:
#                 return table.columns.keys()
#             else:
#                 return table
#         else:
#             return self.get_table_names()
#     # def read_table(self, name_table, return_keys=False):
#     #     table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
#     #     if return_keys:
#     #         return table.columns.keys()
#     #     else:
#     #         return table
#     # def read_table(self, name_table, return_keys=False):
#     #     table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
#     #     if return_keys:
#     #         return table.columns.keys()
#     #     else:
#     #         return table

 
 
#     def add_row(self, name_table, **kwarrgs):
#         name_table = self.read_table(name_table)
 
#         stmt = (
#             db.insert(name_table).
#             values(kwarrgs)
#         )
#         self.connection.execute(stmt)
#         self.connection.commit()
#         print(f'Row id added')
 
 
#     def delete_row_by_id(self, table, id_):
#         name_table = self.read_table(name_table)
 
#         stmt = (
#             db.delete(name_table).
#             where(table.c.id_ == id_)
#             )
#         self.connection.execute(stmt)
#         print(f'Row id {id_} deleted')
 
#     def select_table(self, name_table):
#         name_table = self.read_table(name_table)
#         stm = db.select([name_table])
#         return self.connection.execute(stm).fetchall()
    
#     def get_table_names(self):
#         return self.table_names

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlalchemy as db
import streamlit as st
 
class UfcstatsPipeline:
    def process_item(self, item, spider):
        return item
class DataBase():
    def __init__(self, name_database='Covid'):
        self.name = name_database
        self.url = f"sqlite:///{name_database}.db"
        self.engine = db.create_engine(self.url)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
 
        # Charger les tables existantes dans la base de données
        self.metadata.reflect(bind=self.engine)
 
        # Obtenir la liste des noms de tables
        self.table_names = list(self.metadata.tables.keys())
 
 
    def create_table(self, name_table, **kwargs):
        if name_table not in self.table_names:
            columns = [db.Column(k, v) for k, v in kwargs.items()]
            table = db.Table(name_table, self.metadata, *columns)
            table.create(self.engine, checkfirst=True)
            print(f"Table '{name_table}' created successfully")
        else:
            print(f"Table '{name_table}' already exists")
 
    def read_table(self, name_table, return_keys=False):
        table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
        if return_keys:table.columns.keys()
        else : return table
 
 
    def add_row(self, name_table, **kwarrgs):
        name_table = self.read_table(name_table)
 
        stmt = (
            db.insert(name_table).
            values(kwarrgs)
        )
        self.connection.execute(stmt)
        self.connection.commit()
        print(f'Row id added')
 
 
    def delete_row_by_id(self, table, id_):
        name_table = self.read_table("CovidCases")
 
        stmt = (
            db.delete(name_table).
            where(table.c.id_ == id_)
            )
        self.connection.execute(stmt)
        print(f'Row id {id_} deleted')
 
    # def select_table(self, name_table):
    #     name_table = self.read_table("CovidCases")
    #     stm = db.select([name_table])
    #     return self.connection.execute(stm).fetchall()
    def select_table(self, name_table):
        table = self.read_table(name_table)
        
        stm = db.select(
            table.c.country,
            table.c.deaths,
            table.c.death_rate,
            table.c.total_cases
        ).select_from(table)
        
        result = self.connection.execute(stm).fetchall()
        
        return result