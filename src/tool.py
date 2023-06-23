import json
import re
import regex
import func_timeout
from typing import Union
import random


def jsonlines_load(fname: str):
    with open(fname, 'r') as f:
        return [json.loads(line) for line in f]


def jsonlines_dump(fname: str, data: Union[dict, list]):
    try:
        with open(fname, 'a+') as f:
            if isinstance(data, dict):
                f.write(json.dumps(data)+'\n')
            elif isinstance(data, list):
                for d in data:
                    f.write(json.dumps(d)+'\n')

    except (FileNotFoundError, FileExistsError) as e:
        print(f'Error: {e}')
        print(f'Could not write to {fname}')


def extract_num_codex(solution: str):
    answer = None
    try:
        solution = solution.strip()
        answer = re.findall(
            r'The answer is \$?(-?\d+\,*\.?\d*)\%?', solution)

        if len(answer) == 0:
            answer = re.findall(r'-?\d+\,*\.?\d*', solution)
            answer = answer[-1]
        else:
            answer = answer[0]

        answer = answer.replace(',', '')
        answer = float(answer)

    except Exception as e:
        answer = None

    return answer


def safe_execute_codex(code_string: str, keys=None):
    def execute(x):
        try:
            exec(x)
            locals_ = locals()
            if keys is not None:
                return [locals_.get(k, None) for k in keys]

            solution = locals_.get('solution', None)
            if solution is not None:
                return solution()
            else:
                exec('\n'.join([xx[4:]
                                for xx in x.strip().split('\n')[1:-1]]))
                locals_ = locals()
                return locals_.get('result', None)

        except Exception:
            return None
    try:
        ans = func_timeout.func_timeout(3, execute, args=(code_string,))
        ans = float(ans) if ans is not None else ans
    except func_timeout.FunctionTimedOut:
        ans = None
    return ans


def extract_num_turbo(solution: str):
    ans = solution.strip().split('\n')[-1].replace('So the answer is ', '')
    prd = [x[0] for x in regex.finditer(
        r'[\d\.,]+', ans) if regex.search(r'\d', x[0])]
    if len(prd) > 2:
        prd = prd[-1]
    elif len(prd):
        prd = prd[0]
    else:
        prd = None
    try:
        prd = float(prd.replace(',', '').rstrip('.')) if prd else prd
    except:
        prd = None
    return prd


def safe_execute_turbo(code_string: str, keys=None):
    def execute(x, code_return):
        try:
            exec(x)
            locals_ = locals()
            if keys is not None:
                return [locals_.get(k, None) for k in keys]

            solution = locals_.get('solution', None)
            if solution is not None:
                return solution()
            else:
                executed_code = 'import math\n' + 'import datetime\n' + \
                    '\n'.join([xx[4:]
                                for xx in x.strip().split('\n')[1:-1]])
                exec(executed_code)
                locals_ = locals()
                return locals_.get(code_return, None)

        except Exception as exp:
            print('Executing code error', exp)
            return None

    # === find code snippets between def solution(): and return ===
    try:
        code_list = code_string.strip().split('\n')

        new_code_list = []
        all_codes = []
        code_return = 'ans'

        for i in range(len(code_list)):
            if code_list[i].strip() == 'def solution():':
                new_code_list.append(code_list[i])
                for j in range(i+1, len(code_list)):
                    if code_list[j].startswith('    '):
                        new_code_list.append(code_list[j])
                    if 'return ' in code_list[j]:
                        code_return = code_list[j].split('return ')[1].strip()
                all_codes.append('\n'.join(new_code_list))
                new_code_list = []
        new_code = all_codes[-1]

        ans = func_timeout.func_timeout(
            3, execute, args=(new_code, code_return,))
        ans = ans if ans is not None else ans
    except func_timeout.FunctionTimedOut:
        ans = None

    try:
        ans = float(ans) if ans is not None else ans
    except:
        ans = None

    return ans


def extract_choice_turbo(selection: str):
    if selection.startswith('Both') or selection.startswith('Neither'):
        if random.random() < 0.5:
            choices_a_b = '(A)'
        else:
            choices_a_b = '(B)'
    else:
        try:
            choices = re.findall(r'(\(A\)|\(B\)) can correctly', selection)

            if len(choices) == 0:
                choices = re.findall(
                    r'(\(A\)|\(B\)) is(?:\sthe)? correct', selection)
            choices_a_b = choices[0]

        except:
            if random.random() < 0.5:
                choices_a_b = '(A)'
            else:
                choices_a_b = '(B)'

    return choices_a_b


def extract_choice_codex(selection: str):
    try:
        choice = re.findall(r'\(A\)|\(B\)', selection)

        if choice[0] == '(A)':
            return '(A)'
        elif choice[0] == '(B)':
            return '(B)'
        else:
            if random.random() < 0.5:
                return '(A)'
            else:
                return '(B)'
    except Exception as e:
        if random.random() < 0.5:
            return '(A)'
        else:
            return '(B)'


def extract_date_cot(solution: str):
    cot_answer = None
    cot_answers = re.findall(r'\d{1,2}/\d{1,2}/\d{4}', solution)
    try:
        cot_answer = cot_answers[-1]
        if len(cot_answer.split('/')[0]) == 1:
            cot_answer = '0' + cot_answer

        if len(cot_answer.split('/')[1]) == 1:
            cot_answer = cot_answer.split(
                '/')[0] + '/0' + cot_answer.split('/')[1] + '/' + cot_answer.split('/')[2]
    except Exception as e:
        cot_answer = None

    return cot_answer


def execute_date_pal(code_string: str, keys=None):
    def execute(x, code_return):
        try:
            exec(x)
            locals_ = locals()
            if keys is not None:
                return [locals_.get(k, None) for k in keys]

            solution = locals_.get('solution', None)
            if solution is not None:
                return solution()
            else:
                executed_code = 'import math\n' + 'import datetime\n' + 'from datetime import datetime\n' + 'from dateutil.relativedelta import relativedelta as relativedelta\n' + \
                    'from dateutil.relativedelta import relativedelta as timedelta\n' + \
                    'import pytz\n' + \
                    '\n'.join([xx[4:] for xx in x.strip().split('\n')[1:-1]])
                exec(executed_code)
                locals_ = locals()
                return locals_.get(code_return, None)

        except Exception as exp:
            print('Executing code error', exp)
            return None

    # find code snippets between def solution(): and return
    try:
        code_list = code_string.strip().split('\n')

        new_code_list = []
        all_codes = []
        code_return = 'ans'

        for i in range(len(code_list)):
            if code_list[i].strip() == 'def solution():':
                new_code_list.append(code_list[i])
                for j in range(i+1, len(code_list)):
                    if code_list[j].startswith('    '):
                        new_code_list.append(code_list[j])
                    if 'return ' in code_list[j]:
                        code_return = code_list[j].split('return ')[1].strip()
                all_codes.append('\n'.join(new_code_list))
                new_code_list = []
        new_code = all_codes[-1]
        ans = func_timeout.func_timeout(
            3, execute, args=(new_code, code_return,))
    except func_timeout.FunctionTimedOut:
        ans = None

    return ans
