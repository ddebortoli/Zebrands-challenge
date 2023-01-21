from resources.controllers.prod.database.database import Database
import bcrypt


class AdminController():
    def __init__(self, ids=None):
        pass
    
    def getAdmins(self,ids):
        db = Database()
        # Format the query
        if ids:
            query = "SELECT idusers,name,mail FROM users WHERE idusers IN (%s)" % ','.join([
                '%s']*len(ids))
        else:
            query = "SELECT idusers,name,mail FROM users"

        try:
            users = db.executeQueryFetch(query, ids)
            return {"result": users},200
        except Exception as error:
            db.close()
            return {"message:": "Unexpected Error", "description": str(error)},500

    def createAdmin(self,user,password,mail):
        """create una admin per request"""
        ### I think its more safe create admins one by one than creating by bulk
        db = Database()
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        
        query = "INSERT INTO users (name,password,mail) values (%s,%s,%s)"
        
        try:
            db.executeQueryPreCommit(query, (user,hashed_password,mail))
        except Exception as error:
            return {"message": "Unexpected Error.", "description":str(error)}, 500
        else:
            try:
                db.executeCommit()
                db.close()
            except Exception as error:
                db.executeRollback()
                db.close()
                return {"message:": "Unexpected Error", "description": str(error)}, 500
            else:
                return {"message": "Created."}, 201

    def updateAdmins(self, admins):

        db = Database()
        errorOnUpdate = False
        for data in admins:
            ### Users can only update name or mail, i don't think update their password is a good idea
            query = "UPDATE users SET name = %s, mail = %s WHERE idusers = %s \n"
            values = (data["user"], data['mail'],data['iduser'])
            try:
                db.executeQueryPreCommit(query, values)
            except Exception as error:
                errorOnUpdate = True
                db.close()
                return {"message:": "Unexpected Error", "description": str(error)}, 500

        if not errorOnUpdate:
            try:
                db.executeCommit()
                db.close()
            except Exception as error:
                db.executeRollback()
                db.close()
                return {"message:": "Unexpected Error", "description": str(error)}, 500
            else:
                return {"message": "Sucessfull updated."}, 200

    def deleteAdmins(self,admins):

        db = Database()
        errorOnUpdate = False
        query = "DELETE FROM users WHERE idusers = %s"
        
        for admin in admins:
            try:
                db.executeQueryPreCommit(query, (admin['iduser'],))
            except Exception as error:
                errorOnUpdate = True
                print(error,flush=True)

        if not errorOnUpdate:
            try:
                db.executeCommit()
                db.close()
            except Exception as error:
                db.executeRollback()
                db.close()
                return {"message:": "Unexpected Error", "description": error}, 500
            else:
                return {"message": "Sucessfull deleted."}, 200