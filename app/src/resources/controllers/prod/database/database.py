import mysql
from utils.generalControllers import fixDataFromDataBase
from types import NoneType

class Database():
    def __init__(self):
        self.connection = mysql.connector.connect(host="sqlserver.cednxsqskh9k.us-east-1.rds.amazonaws.com",user="ddebortoli",passwd="OZN0kahYCzlxPet",db="Zebrands")
        self.cursor = self.connection.cursor()
    
    def executeQueryFetch(self,query,values=None):
        if values:   
            self.cursor.execute(query,values)
        else:
            self.cursor.execute(query)
        
        data = self.cursor.fetchall()
        data = self._formatWithColumns(data)
        self.close()
        
        return fixDataFromDataBase(data)
    
    def executeQueryPreCommit(self,query,values):
        self.cursor.execute(query,values)
    
    def executeCommit(self):
        self.connection.commit()
    
    def executeRollback(self):
        self.connection.rollback()
    def close(self):
        self.cursor.close()
        self.connection.close()
    
    def _formatWithColumns(self,result):
        "return dict with column and value"
        if type(result) == NoneType: result = []
        item = []
        if len(result) > 0:       
            colums = [column[0] for column in self.cursor.description]
            for row in result:
                item.append(dict(zip(colums,row)))  
        return item