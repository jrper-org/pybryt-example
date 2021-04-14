import pybryt

__all__ = ['does_not_exist', 'have_function', 'short_match_list']

def does_not_exist(value, success_message=None, failure_message = None, **kwargs):
    v = pybryt.Value(value, **kwargs)
    n = ~v
    n.success_message = success_message
    n.failure_message = failure_message
    return(n)


def have_function(func, **kwargs):
    v = pybryt.Value('_function_'+func.__name__, **kwargs)

class short_match_list(list):
   def __eq__(self, v):
       try:
           return all((self[i]==v[i] for i in range(1001)))
       except (KeyError, ValueError, IndexError):
           return False