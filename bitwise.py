import timeit

print("Bitwise method time:",
      timeit.timeit("for x in range(100): x & 1 == 0", number=100000))

print("Modulus method time:",
      timeit.timeit("for x in range(100): x % 2 == 0", number=100000))
