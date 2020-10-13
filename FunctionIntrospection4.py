import inspect

# TODO: Are you really just returning True?
def my_func(a: list[str], b: int = 1, *args: str, kw1: int = 100, **kwargs: float):
    """A simple function"""
    i = 10
    j = 20
    return True


print(inspect.signature(my_func))  # -> <class 'inspect.Signature'>
# (a: list, b: int = 1, *args: str, kw1: int = 100, **kwargs: float)

for attr in dir(inspect.signature(my_func)):
    print(attr)
# __class__
# __delattr__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __le__
# __lt__
# __module__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __setstate__
# __sizeof__
# __slots__
# __str__
# __subclasshook__
# _bind
# _bound_arguments_cls
# _hash_basis
# _parameter_cls
# _parameters
# _return_annotation
# bind
# bind_partial
# empty
# from_builtin
# from_callable
# from_function
# parameters
# replace
# return_annotation

signature = inspect.signature(my_func)

for k in signature.parameters:
    print(k)
