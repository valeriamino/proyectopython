import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def timeit(func):
    def wrapper(*args,**kwargs):
        start_time= time.time()
        result= func(*args, **kwargs)
        end_time= time.time()
        elapsed_time= end_time - start_time
        logging.info(f"{func.__name__} ejecutada en {elapsed_time:.4f} seconds")
        return result
    return wrapper

def logit(func):
    def wrapper(*args,**kwargs):
        logging.info(f"Corrigiendo {func.__name__}")
        result= func(*args,**kwargs)
        logging.info(f"Completado {func.__name__}")
        return result
    return wrapper        
