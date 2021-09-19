def arithmetic_arranger(problems, show_ans=False):

    import re

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        if re.match('.*[a-zA-z].*', problem):
            return 'Error: Numbers must only contain digits.'
        if re.match('.*(\*|/).*', problem):
            return 'Error: Operator must be \'+\' or \'-\'.'
        if re.match('.*\d{5,}.*', problem):
            return 'Error: Numbers cannot be more than four digits.'

    arranged_problems = ''
    arr = []
    width = []
    for problem in problems:
        problem_splitted = re.findall('\d+|\+|\-', problem)
        width.append(0)
        ans_num = 0
        ans = ''
        if not show_ans:
            width[-1] = max(len(s) for s in problem_splitted) + 2
        else:
            ans_num = int(problem_splitted[0]) + int(problem_splitted[2]) if problem_splitted[1] == '+' else int(problem_splitted[0]) - int(problem_splitted[2])
            ans = str(ans_num)
            width[-1] = max(len(ans),max(len(s) for s in problem_splitted) + 2)
        col = []
        col.append(' ' * (width[-1] - len(problem_splitted[0])) + problem_splitted[0])
        col.append(problem_splitted[1] + ' ' * (width[-1] - len(problem_splitted[2]) - 1) + problem_splitted[2])
        col.append('-' * width[-1])
        if show_ans:
            col.append(ans)
        arr.append(col)

    for i in range(len(problems)):
        if i == 0:
            arranged_problems += arr[0][0]
        else:
            arranged_problems += ' ' * 4 + arr[i][0]

    arranged_problems += '\n'

    for i in range(len(problems)):
        if i == 0:
            arranged_problems += arr[0][1]
        else:
            arranged_problems += ' ' * 4 + arr[i][1]

    arranged_problems += '\n'

    for i in range(len(problems)):
        if i == 0:
            arranged_problems += arr[0][2]
        else:
            arranged_problems += ' ' * 4 + arr[i][2]

    if show_ans:
        arranged_problems += '\n'
        for i in range(len(problems)):
            if i == 0:
                arranged_problems += ' ' * (width[i] - len(arr[0][3])) + arr[0][3]
            else:
                arranged_problems += ' ' * (width[i] - len(arr[i][3]) + 4) + arr[i][3]

    return arranged_problems