# Helberg code
# 1. string genegration
# 2. vi array generate
# 3. find m
# 4. find a and classyfy the strings by a


# 1. string genegration
# input: n, k
# output: list of strings

import numpy as np
import pprint as pp
import sys


def String_generate(n, k, x, final_list):
    if n == 0:
        final_list.append(x[:])
    else:
        for j in range(0, k):
            x.append(j)
            String_generate(n-1, k, x, final_list)
            x.pop()
    return x


def Vi_generate(n, s, v):
    for i in range(0, n):
        for j in range(1, s+1):
            v[i] += v[i-j] if (i-j >= 0) else 0


def find_M(v, s, n):
    m = 1
    for i in range(1, s+1):
        m += v[n-i]
    return m


def func(num, v, m, n, ans):
    sum = 0
    for i in range(0, n):
        # print(v[i]*num[i])
        sum += v[i]*num[i]
    sum = sum % m
    # print(sum)
    if sum not in ans:
        ans[sum] = []
    ans[sum].append(num)


if __name__ == "__main__":
    x = []
    final_list = []
    if len(sys.argv) != 4:
        print("Usage: python3 helberg.py n q s")
        sys.exit()

    # Read the command line arguments
    n = int(sys.argv[1])
    q = int(sys.argv[2])
    s = int(sys.argv[3])
    v = np.ones(n)
    ans = {}

    if s < n:
        # Use the function
        String_generate(n, q, x, final_list)
        x = final_list
        x = np.array(x)
        # for i in x:
        #     print(i)

        Vi_generate(n, s, v)
        # print("V = ", v)

        m = find_M(v, s, n)
        # print("m = ", m)

        for i in x:
            func(i, v, m, n, ans)

    else:
        ans[0] = []
    # Open the output file
    with open('output.txt', 'a') as f:
        # Create a pretty printer object
        codewords = pp.PrettyPrinter(indent=4, stream=f)

        # Use the pretty printer to print the dictionary
        codewords.pprint(ans)

        # print n , q , s and max_codeword
        print("N = ", n, ", q = ", q, ", s = ", s,
              ", Max number of codewords = ", max(len(v) for v in ans.values()), file=f)
        print(
            "============================================================================", file=f)
        print(
            "============================================================================", file=f)
