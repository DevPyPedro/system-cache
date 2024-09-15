from abc import ABC, abstractmethod

class IRedis:
    
    @abstractmethod
    def get_conn():
        '''Return engine Redis'''