from functional import seq

result = seq(1, 2, 3, 4)\
    .map(lambda x: x * 2)\
    .filter(lambda x: x > 4)\
    .reduce(lambda x, y: x + y)
print("Results: {}".format(result))

# or if you don't like backslash continuation
result2 = (seq(1, 2, 3, 4)
    .map(lambda x: x * 2)
    .filter(lambda x: x > 4)
    .reduce(lambda x, y: x + y)
)
print("Results: {}".format(result2))
# 14