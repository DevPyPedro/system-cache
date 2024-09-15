import redis #type: ignore

from src.infra.db.interface.cache_interface import IRedis

class Redis(IRedis):
    
    def __create_conn(self)->redis.client:
        return redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
    
    def get_conn(self):
       redis_client = self.__create_conn()
       return redis_client   
