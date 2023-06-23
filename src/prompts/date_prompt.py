# ===== Codex =====
CODEX_COT_PROMPT = '''
Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY? 

A: If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/05/2015. So the answer is 01/05/2015.



Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

A: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019. So the answer is 01/07/2019.



Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

A: One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943. 10 days before today is 05/23/1943. So the answer is 05/23/1943.



Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

A: Today is 04/19/1969. 24 hours later is one day after today, which would be 04/20/1969. So the answer is 04/20/1969.



Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

A: Today is 03/12/2002. So the date 24 hours later will be 03/13/2002. So the answer is 03/13/2002.



Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

A: The last day of February is the 28th, so Jane was born on 02/28/2001. Today is her 16-year old birthday, so today is 02/28/2017. So yesterday was 02/27/2017. So the answer is 02/27/2017.
'''.strip()+'\n\n\n\n'


CODEX_PAL_PROMPT = '''
Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

# solution in Python
def solution():
    # If 2015 is coming in 36 hours, then today is 36 hours before.
    today = datetime(2015, 1, 1) - relativedelta(hours=36)
    # One week from today,
    one_week_from_today = today + relativedelta(weeks=1)
    # The answer formatted with %m/%d/%Y is
    result = one_week_from_today.strftime('%m/%d/%Y')
    return result




Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

# solution in Python:
def solution():
    # If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.
    today = datetime(2019, 1, 1) + relativedelta(days=6)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result




Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

# solution in Python:
def solution():
    # If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
    today = datetime(1943, 6, 1) + relativedelta(days=1)
    # 10 days ago,
    ten_days_ago = today - relativedelta(days=10)
    # The answer formatted with %m/%d/%Y is
    result = ten_days_ago.strftime('%m/%d/%Y')
    return result




Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

# solution in Python:
def solution():
    # It is 4/19/1969 today.
    today = datetime(1969, 4, 19)
    # 24 hours later,
    later = today + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result




Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

# solution in Python:
def solution():
    # If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/1/2002.
    today = datetime(2002, 3, 12)
    # 24 hours later,
    later = today + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = later.strftime('%m/%d/%Y')
    return result




Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

# solution in Python:
def solution():
    # If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
    today = datetime(2001, 2, 28) + relativedelta(years=16)
    # Yesterday,
    yesterday = today - relativedelta(days=1)
    # The answer formatted with %m/%d/%Y is
    result = yesterday.strftime('%m/%d/%Y')
    return result    
'''.strip()+'\n\n\n\n\n'


CODEX_SELECT_PROMPT = '''
Date Understanding Problem: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY? 

Question: Which of the following two choices can correctly answer the date understanding problem?

(A)
def solution():
    # If 2015 is coming in 36 hours, then today is 36 hours before.
    today = datetime(2015, 1, 1) - relativedelta(hours=36)
    # One week from today,
    one_week_from_today = today + relativedelta(weeks=1)
    # The answer formatted with %m/%d/%Y is
    result = one_week_from_today.strftime('%m/%d/%Y')
    return result

(B)
A: If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/06/2015. So the answer is 01/06/2015.

Answer: (A)




Date Understanding Problem: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

Question: Which of the following two choices can correctly answer the date understanding problem?

(A)
def solution():
    # If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 5 days later.
    today = datetime(2019, 1, 1) + relativedelta(days=5)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result

(B)
A: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019. So the answer is 01/07/2019.

Answer: (B)




Date Understanding Problem: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

Question: Which of the following two choices can correctly answer the date understanding problem?

(A)
def solution():
    # If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
    today = datetime(1943, 6, 1) + relativedelta(days=1)
    # 10 days ago,
    ten_days_ago = today - relativedelta(days=10)
    # The answer formatted with %m/%d/%Y is
    result = ten_days_ago.strftime('%m/%d/%Y')
    return result

(B)
A: One day before 06/01/1943 is 05/31/1943, so today is 05/31/1943. 10 days before today is 05/21/1943. So the answer is 05/21/1943.

Answer: (A)




Date Understanding Problem: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

Question: Which of the following two choices can correctly answer the date understanding problem?

(A)
def solution():
    # It is 4/19/1969 today.
    today = datetime(1969, 4, 19)
    # 24 hours later,
    later = today - relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result

(B)
A: Today is 04/19/1969. 24 hours later is one day after today, which would be 04/20/1969. So the answer is 04/20/1969.

Answer: (B)




Date Understanding Problem: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

Question: Which of the following two choices can correctly answer the date understanding problem?

(A)
def solution():
    # If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/1/2002.
    today = datetime(2002, 3, 12)
    # 24 hours later,
    later = today + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = later.strftime('%m/%d/%Y')
    return result


(B)
A: Today is 03/12/2002. 1 day later is 03/13/2002. So the date 24 hours later will be 03/14/2002. So the answer is 03/14/2002.

Answer: (A)




Date Understanding Problem: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

Question: Which of the following two choices can correctly answer the date understanding problem?

(A)
def solution():
    # If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
    today = datetime(2001, 2, 29) + relativedelta(years=16)
    # Yesterday,
    yesterday = today - relativedelta(days=1)
    # The answer formatted with %m/%d/%Y is
    result = yesterday.strftime('%m/%d/%Y')
    return result

(B)
A: The last day of February is the 28th, so Jane was born on 02/28/2001. Today is her 16-year old birthday, so today is 02/28/2017. So yesterday was 02/27/2017. So the answer is 02/27/2017.

Answer: (B)
'''


# ===== ChatGPT, GPT-4 =====
TURBO_COT_SYSTEM = 'You are a helpful assistant that can solve date understanding problems step by step.'

TURBO_COT_USER = '''
Let's solve the following date understanding problems. You need to solve these date understanding problems step by step. Here is one example how to do it,

Question: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY? 

Answer:
If 2015 is coming in 36 hours, then it is coming in 2 days.
And 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014.
So one week from today will be 01/05/2015.
So the answer is 01/05/2015.


Now it's your turn. Here is another date understanding problem:
Question: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?



Question: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?



Question: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?



Question: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?



Question: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?
'''.strip()


TURBO_COT_ASSISTANT = '''
Answer:
If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday.
And today is the first monday, would be six days later.
So today is 01/07/2019.
So the answer is 01/07/2019.



Answer:
One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943.
And 10 days before today is 05/23/1943.
So the answer is 05/23/1943.



Answer:
Today is 04/19/1969.
And 24 hours later is one day after today, which would be 04/20/1969.
So the answer is 04/20/1969.



Answer:
Today is 03/12/2002.
So the date 24 hours later will be 03/13/2002.
So the answer is 03/13/2002.



Answer:
The last day of February is the 28th, so Jane was born on 02/28/2001.
And today is her 16-year old birthday, so today is 02/28/2017.
So yesterday was 02/27/2017.
So the answer is 02/27/2017.
'''.strip()

TURBO_PAL_SYSTEM = 'You are a helpful assistant that can solve date understanding problems by using Python code.'


TURBO_PAL_USER = '''
Let's use python to solve date understanding problems. You need to write python code to answer these date understanding problems. Here is one example how to do it,

Question: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

# solution in Python
def solution():
    # If 2015 is coming in 36 hours, then today is 36 hours before.
    today = datetime(2015, 1, 1) - relativedelta(hours=36)
    # One week from today,
    one_week_from_today = today + relativedelta(weeks=1)
    # The answer formatted with %m/%d/%Y is
    result = one_week_from_today.strftime('%m/%d/%Y')
    return result


Now it's your turn. Here is another date understanding problem,
Question: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

# solution in Python:



Question: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

# solution in Python:



Question: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

# solution in Python:



Question: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

# solution in Python:



Question: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

# solution in Python:
'''.strip()


TURBO_PAL_ASSISTANT = '''
def solution():
    # If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.
    today = datetime(2019, 1, 1) + relativedelta(days=6)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result



def solution():
    # If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
    today = datetime(1943, 6, 1) + relativedelta(days=1)
    # 10 days ago,
    ten_days_ago = today - relativedelta(days=10)
    # The answer formatted with %m/%d/%Y is
    result = ten_days_ago.strftime('%m/%d/%Y')
    return result



def solution():
    # It is 4/19/1969 today.
    today = datetime(1969, 4, 19)
    # 24 hours later,
    later = today + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result



def solution():
    # If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/1/2002.
    today = datetime(2002, 3, 12)
    # 24 hours later,
    later = today + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = later.strftime('%m/%d/%Y')
    return result



def solution():
    # If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
    today = datetime(2001, 2, 28) + relativedelta(years=16)
    # Yesterday,
    yesterday = today - relativedelta(days=1)
    # The answer formatted with %m/%d/%Y is
    result = yesterday.strftime('%m/%d/%Y')
    return result
'''.strip()


TURBO_SELECT_SYSTEM = 'You are a helpful assistant that can identify the correct answer to the date understanding problem.'


TURBO_SELECT_USER = '''
There are two choices to the same date understanding problem. One uses natural language to answer the question, while the other uses Python program to answer it. Either of them can correctly answer the date understanding problem. You need to identify which choice can correctly answer the problem. Here is one example how to do it,

Date Understanding Problem: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY? 

(A)
Answer:
If 2015 is coming in 36 hours, then it is coming in 2 days.
And 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014.
So one week from today will be 01/05/2015.
So the answer is 01/05/2015.

(B)
def solution():
    # If 2015 is coming in 36 hours, then today is 36 hours before.
    today = datetime(2015, 1, 1) + relativedelta(hours=36)
    # One week from today,
    one_week_from_today = today + relativedelta(weeks=1)
    # The answer formatted with %m/%d/%Y is
    result = one_week_from_today.strftime('%m/%d/%Y')
    return result

Which of the above two choices can correctly answer the date understanding problem?
(A) can correctly answer the date understanding problem. Because (B) incorrectly calculates the date 36 hours later instead of 36 hours before.

Now it's your turn. Here is another date understanding problem and two choices.
Date Understanding Problem: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

(A)
Answer:
If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday.
And today is the first monday, would be 5 days later.
So today is 01/06/2019.
So the answer is 01/06/2019.

(B)
def solution():
    # If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.
    today = datetime(2019, 1, 1) + relativedelta(days=6)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result

Which of the above two choices can correctly answer the date understanding problem?



Date Understanding Problem: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

(A)
Answer:
One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943.
And 10 days before today is 05/23/1943.
So the answer is 05/23/1943.

(B)
def solution():
    # If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day before.
    today = datetime(1943, 6, 1) - relativedelta(days=1)
    # 10 days ago,
    ten_days_ago = today - relativedelta(days=10)
    # The answer formatted with %m/%d/%Y is
    result = ten_days_ago.strftime('%m/%d/%Y')
    return result

Which of the above two choices can correctly answer the date understanding problem?



Date Understanding Problem: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

(A)
Answer:
Today is 04/19/1969.
And 24 hours later is one day after today, which would be 04/18/1969.
So the answer is 04/18/1969.

(B)
def solution():
    # It is 4/19/1969 today.
    today = datetime(1969, 4, 19)
    # 24 hours later,
    later = today + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = today.strftime('%m/%d/%Y')
    return result

Which of the above two choices can correctly answer the date understanding problem?



Date Understanding Problem: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

(A)
Answer:
Today is 03/12/2002.
So the date 24 hours later will be 03/13/2002.
So the answer is 03/13/2002.

(B)
def solution():
    # If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/1/2002.
    today = datetime(2002, 3, 12)
    # 1 day later,
    later = today + relativedelta(hours=24)
    # so 24 hours later,
    later = later + relativedelta(hours=24)
    # The answer formatted with %m/%d/%Y is
    result = later.strftime('%m/%d/%Y')
    return result

Which of the above two choices can correctly answer the date understanding problem?



Date Understanding Problem: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

(A)
Answer:
The last day of February is the 29th, so Jane was born on 02/29/2001.
And today is her 16-year old birthday, so today is 02/29/2017.
So yesterday was 02/28/2017.
So the answer is 02/28/2017.

(B)
def solution():
    # If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
    today = datetime(2001, 2, 28) + relativedelta(years=16)
    # Yesterday,
    yesterday = today - relativedelta(days=1)
    # The answer formatted with %m/%d/%Y is
    result = yesterday.strftime('%m/%d/%Y')
    return result

Which of the above two choices can correctly answer the date understanding problem?
'''.strip()

TURBO_SELECT_ASSISTANT = '''
(B) can correctly answer the problem. Because (A) missed the fact that there are 6 days between the first day of 2019 and the first Monday of 2019.



(A) can correctly answer the problem. Because (B) missed the fact that delay by one day means one day later instead of one day before.



(B) can correctly answer the problem. Because (A) missed the fact that 24 hours later means one day later instead of one day before.



(A) can correctly answer the problem. Because (B) incorrectly calculates the date 24 hours later twice instead of once.



(B) can correctly answer the problem. Because (A) missed the fact that the last day of Feburary in 2001 is the 28th instead of the 29th.
'''.strip()
