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
import collections


def String_generate(n, q, x, final_list):
    if n == 0:
        final_list.append(x[:])
    else:
        for j in range(0, q):
            x.append(j)
            String_generate(n-1, q, x, final_list)
            x.pop()
    return x


def Vi_generate(n, s, v, q):
    for i in range(0, n):
        for j in range(1, s+1):
            v[i] += v[i-j] if (i-j >= 0) else 0
        v[i] = v[i]*(q-1) + 1


def find_M(v, s, n, q):
    m = 0
    for i in range(1, s+1):
        m += v[n-i]
    return m*(q-1) + 1


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


def del_sphere(final_list, num):
    temp_list = []
    del_list = {}
    for i in final_list:
        for j in range(len(i)):
            pref = i[:j]
            suff = i[j+1:]
            temp = tuple(pref) + tuple(suff)
            if (num > 0) and (temp not in temp_list):
                temp_list.append(temp)
            else:
                if temp not in del_list:
                    del_list[temp] = []
                if i not in del_list[temp]:
                    del_list[temp].append(i)
    main_list = {}
    if (num == 0):
        return del_list
    else:
        num -= 1
        x = del_sphere(temp_list, num)
        new_dict = {}
        # print(x)
        # print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(del_list)
        for i in x:
            for j in x[i]:
                if (j in del_list):
                    tuple1 = tuple(i for i in del_list[j])
                    for k in del_list[j]:
                        if i not in new_dict:
                            new_dict[i] = []
                        if k not in new_dict[i]:
                            new_dict[i].append(k)
        # print(new_dict)
        return new_dict


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
    v = np.zeros(n)
    ans = {}

    if s < n:
        String_generate(n, q, x, final_list)
        x = final_list
        x = np.array(x)
        Vi_generate(n, s, v, q)
        m = find_M(v, s, n, q)
        for i in x:
            func(i, v, m, n, ans)

    else:
        ans[0] = []
    # Open the output file
    with open('output.txt', 'a') as f:
        # Create a pretty printer object
        codewords = pp.PrettyPrinter(indent=4, stream=f)

        del_list = del_sphere(final_list, s-1)
        # codewords.pprint(del_list)

        sphered = {}
        q_ary_residue = []
        for i in ans:
            flag = True
            list_tuple = [tuple(lst) for lst in ans[i]]
            x = set(list_tuple)
            for j in del_list:
                list_tuple = [tuple(lst) for lst in del_list[j]]
                y = set(list_tuple)
                # print(x, y)
                # print(type(x), type(y), type(ans[i]), type(del_list[j]))
                if len(x.intersection(y)) > 1:
                    print(len(x.intersection(y)))
                    flag = False
                    break
            if (flag and len(ans[i]) > 1):
                print("a = ", i, file=f)
                q_ary_residue.append(i)
                for k in ans[i]:
                    code = []
                    for j in k:
                        if (j == 0):
                            code.append(0)
                            code.append(0)
                        elif (j == 1):
                            code.append(0)
                            code.append(1)
                        elif (j == 2):
                            code.append(1)
                            code.append(1)
                        else:
                            code.append(1)
                            code.append(0)
                    if i not in sphered:
                        sphered[i] = []
                    sphered[i].append(code)
                    print("original=", k, "gray mapped=", code, file=f)

        # codewords.pprint(sphered)
        # # print n , q , s and max_codeword
        print("N = ", n, ", q = ", q, ", s = ", s, ", Codeword total = ", len(final_list),
              ", Max number of codewords = ", max(len(v) for v in ans.values()), file=f)
        print(
            "============================================================================", file=f)

        binary_residue = []
        for j in sphered:
            if (len(sphered[j]) > 1):
                print("a = ", j, file=f)
                print(sphered[j], file=f)
                del_list = del_sphere(sphered[j], s)
                binary_residue.append(j)
                # # Use the pretty printer to print the dictionary
                reverse_del_list = {}
                for i in del_list:
                    for j in del_list[i]:
                        if tuple(j) not in reverse_del_list:
                            reverse_del_list[tuple(j)] = []
                        reverse_del_list[tuple(j)].append(i)
                # print("reverse", reverse_del_list, file=f)
                del_list = reverse_del_list
                print("deletion sphere", file=f)
                codewords.pprint(del_list)
                flag = True
                for i in del_list:
                    list_tuple = [tuple(lst) for lst in del_list[i]]
                    x = set(list_tuple)
                    for j in del_list:
                        list_tuple = [tuple(lst) for lst in del_list[j]]
                        y = set(list_tuple)
                        if len(x.intersection(y)) == 0 or x == y:
                            flag = True
                        else:
                            flag = False
                            break
                if flag:
                    code = []
                    for i in del_list:
                        code.append(i)
                    print("--------------No intersection------------\n", code, file=f)

        print(sorted(q_ary_residue), file=f)
        print(sorted(binary_residue), file=f)
