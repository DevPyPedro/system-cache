from abc import ABC, abstractmethod

class ISqlite:
    
    @abstractmethod
    def get_conn():
        '''Return engine sqlite'''