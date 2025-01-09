from typing import List, Union, Tuple, Dict


num : int = 67


name : str = "hello world"



def sum(a:int,b:int) -> int:    
    return a+b
    
numbers : List[int] = [1,2,3,4,5]

my_tuple : Tuple[int,str] = (12,"string")

my_dict = Dict[str, int] = {
    "name": 123,
    "age": 234
}

my_union : Union[str, int] = "this is a string"
