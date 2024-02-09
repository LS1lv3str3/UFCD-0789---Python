from datetime import datetime

class Log:
    
    def add_error(erro:str, msg: str):
        file = open("ErrorLog", "a")
        msgError = f"{datetime.now()}\t{erro}\t{msg} "
        file.write(msgError + "\n")
        file.close()


class DataError(Exception):
    
    def __init__(self, msg):   
        Log.add_error(self.__class__.__name__, msg)
                 
        super().__init__(msg)