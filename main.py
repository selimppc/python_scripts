# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(ops_data):
    # Use a breakpoint in the code line below to debug your script.
    scores = ['3', 4]
    print(scores.pop())
    # for op in ops_data:
    #     if op == 'C':
    #         scores.pop()
    #     elif op == 'D':
    #         scores.append(2 * scores[-1])
    #     elif op == '+':
    #         scores.append(scores[-1] + scores[-2])
    #     else:
    #         scores.append(int(op))
    # return sum(scores)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ops = ['5', '2', 'C', 'D', "+"]
    result = print_hi(ops_data=ops)
    #print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
