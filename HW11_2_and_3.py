# question #2: what are the differences between a list and a tuple/ and when should each of them be used?

# the differences are: mutability(lists are mutable, tuples are not mutable),
# hashing(tuples can be used as key, lists can't), operations(lists offer multiple methods for manipulation,
# while tuples have only index() and count()).
# Their usage is when the collection needs to be modified, or be flexible (sort, reverse, etc.) lists should be used
# they are more general purpose.
# When the sequence should be constant the integrity of data should be a bit more protected, or (for some reason)
# it is supposed to be used as a key tuples are the way to go.

# question #3: why the following code does not cause error?
# data_tuple = (
# {"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
# )
# data_tuple[0] ["age"] = 31
# data_tuple[0] .clear()

# the immutability of the tuple does not extend to the objects it contains. In this example the dictionary is mutable
# while trying to change the integer or string would cause an error.
