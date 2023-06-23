# ===== Codex =====
CODEX_COT_PROMPT = '''
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

Answer: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6. The answer is 6.



Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

Answer: There are originally 3 cars. 2 more cars arrive. So there are 3 + 2 = 5 cars. The answer is 5.



Q: Leah had 32 chocolates and her sister had 10 more chocolates than her. If they ate 35, how many pieces do they have left in total?

Answer: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39.



Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

Answer: Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8. The answer is 8.



Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

Answer: Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. So he has 5 + 4 = 9 toys now. The answer is 9.



Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

Answer: There were originally 9 computers. For each of 4 days from monday to thursday, 5 more computers were added. So 5 * 4 = 20 computers were added. So there are 9 + 20 = 29 computers now. The answer is 29.



Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

Answer: Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 -23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. The answer is 33.



Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

Answer: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 * 3 = 15 dollars. So she has 23 - 15 = 8 dollars left. The answer is 8.
'''.strip() + '\n\n\n'


CODEX_PAL_PROMPT = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

# solution in Python:


def solution():
    """Olivia has $23. She bought five bagels for $3 each. How much money does she have left?"""
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result





Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

# solution in Python:


def solution():
    """Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?"""
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - \
        golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result





Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

# solution in Python:


def solution():
    """There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"""
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between monday and thursday
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result





Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

# solution in Python:


def solution():
    """Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"""
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result





Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

# solution in Python:


def solution():
    """Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"""
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result





Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

# solution in Python:


def solution():
    """Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"""
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = total_chocolates - chocolates_eaten
    result = chocolates_left
    return result





Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

# solution in Python:


def solution():
    """If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"""
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result





Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

# solution in Python:


def solution():
    """There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"""
    trees_initial = 15
    trees_after = 21
    trees_added = trees_after - trees_initial
    result = trees_added
    return result
'''.strip() + '\n\n\n\n'


CODEX_SELECT_PROMPT = '''
Math Problem: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

Question: Which of the following two choices can correctly answer the math problem?

(A)
def solution():
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result

(B)
Answer: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 * 3 = 15 dollars. So she has 23 - 5 = 18 dollars left. The answer is 18.

Answer: (A)




Math Problem: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

Question: Which of the following two choices can correctly answer the math problem?

(A)
def solution():
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday
    result = golf_balls_left
    return result

(B)
Answer: Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 -23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. The answer is 33.

Answer: (B)




Math Problem: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

Question: Which of the following two choices can correctly answer the math problem?

(A)
def solution():
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between monday and thursday
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result

(B)
Answer: There were originally 9 computers. 5 more computers were added. So there are 9 + 5 = 14 computers now. The answer is 14.

Answer: (A)




Math Problem: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

Question: Which of the following two choices can correctly answer the math problem?

(A)
def solution():
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial - total_received
    result = total_toys
    return result

(B)
Answer: Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. So he has 5 + 4 = 9 toys now. The answer is 9.

Answer: (B)




Math Problem: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

Question: Which of the following two choices can correctly answer the math problem?

(A)
def solution():
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result

(B)
Answer: Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 + 12 = 32. The answer is 32.

Answer: (A)




Math Problem: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

Question: Which of the following two choices can correctly answer the math problem?

(A)
def solution():
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = leah_chocolates - chocolates_eaten
    result = chocolates_left
    return result

(B)
Answer: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39.

Answer: (B)




Math Problem: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

Question: Which of the following two choices can correctly answer the math problem?

(A)
def solution():
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result

(B)
Answer: There are originally 3 cars. 2 more cars arrive. There are 3 + 2 = 5 cars. So there are 5 + 2 = 7 cars now. The answer is 7.

Answer: (A)




Math Problem: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

Question: Which of the following two choices can correctly answer the math problem?

(A)
def solution():
    trees_initial = 15
    trees_after = 21
    trees_added = trees_initial - trees_after
    result = trees_added
    return result

(B)
Answer: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6. The answer is 6.

Answer: (B)
'''.strip() + '\n\n\n\n\n'

# ===== ChatGPT =====
TURBO_COT_SYSTEM = 'You are a helpful assistant that can solve math problems step by step.'

TURBO_COT_USER = '''
Let's solve the following math problems. You need to solve these math problems step by step. Here is one example how to do it,

Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

Answer:
Olivia had 23 dollars.
And she bought 5 bagels.
And each bagel costs 3 dollars.
So she spent 5 * 3 = 15 dollars.
So she has 23 - 15 = 8 dollars left.
So the answer is 8.


Now it's your turn. Here is another math problem:
Question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?



Question: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?



Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?



Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?



Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?



Question: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?



Question: Leah had 32 chocolates and her sister had 10 more chocolates than her. If they ate 35, how many pieces do they have left in total?
'''.strip()

TURBO_COT_ASSISTANT = '''
Answer:
Michael started with 58 golf balls.
And he lost 23 golf balls on tuesday.
So after losing 23 on tuesday, he had 58 -23 = 35.
And then he lost 2 more golf balls on wednesday.
So after losing 2 more on wednesday, he had 35 - 2 = 33 golf balls.
So the answer is 33.



Answer:
There were originally 9 computers.
And 5 more computers were added from monday to thursday.
There are 4 days between monday and thursday.
So 5 * 4 = 20 computers were added in total.
So there are 9 + 20 = 29 computers now.
So the answer is 29.



Answer:
Shawn started with 5 toys.
And he got 2 toys each from his mom and dad.
So he got 2 + 2 = 4 toys.
Therefore, he has 5 + 4 = 9 toys now.
So the answer is 9.



Answer:
Jason started with 20 lollipops.
Then he had 12 after giving some to Denny.
So he gave Denny 20 - 12 = 8 lollipops.
So the answer is 8.



Answer:
There are 15 trees originally.
And there were 21 trees after some more were planted.
So 21 - 15 = 6 trees were planted.
So the answer is 6.



Answer:
There are originally 3 cars.
And 2 more cars arrive.
So there are 3 + 2 = 5 cars now.
So the answer is 5.



Answer:
Originally, Leah had 32 chocolates.
And her sister had 10 more chocolates than her.
So her sister had 42 chocolates.
So in total they had 32 + 42 = 74 chocolates.
Then they ate 35 chocolates.
Therefore they had 74 - 35 = 39 chocolates left.
So the answer is 39.
'''.strip()


TURBO_PAL_SYSTEM = 'You are a helpful assistant that generates Python code to answer arithmetic questions. '

TURBO_PAL_USER = '''
Let's use python to solve math problems. You need to write python code to answer these math questions. Here is one example how to do it,

Answer the following question in Python: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

def solution():
    """Olivia has $23. She bought five bagels for $3 each. How much money does she have left?"""
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result

Now it's your turn.
Answer the following question in Python: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?



Answer the following question in Python: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?



Answer the following question in Python: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?



Answer the following question in Python: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?



Answer the following question in Python: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?



Answer the following question in Python: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?



Answer the following question in Python: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
'''.strip()


TURBO_PAL_ASSISTANT = '''
def solution():
    """Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?"""
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result



def solution():
    """There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"""
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between monday and thursday
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result



def solution():
    """Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"""
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result



def solution():
    """Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"""
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result



def solution():
    """Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"""
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = total_chocolates - chocolates_eaten
    result = chocolates_left
    return result



def solution():
    """If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"""
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result



def solution():
    """There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"""
    trees_initial = 15
    trees_after = 21
    trees_added = trees_after - trees_initial
    result = trees_added
    return result
'''.strip()


TURBO_SELECT_SYSTEM = '''You are a helpful assistant that can identify the correct answer to the math problem.'''

TURBO_SELECT_USER = '''There are two choices to the same math problem. One uses natural language to answer the question, while the other uses Python program to answer it. Either of them can correctly answer the math problem. You need to identify which choice can correctly answer the math problem. Here is one example how to do it,

Math problem: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

(A)
Answer:
Olivia had 23 dollars.
5 bagels for 3 dollars each will be 5 * 3 = 15 dollars.
So she has 23 - 15 = 8 dollars left.
So the answer is 8.

(B)
def solution():
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels + bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result

Which of the above two choices can correctly answer the math problem?
(A) can correctly answer the math problem. Because (B) adds the number of bagels to the cost of each bagel instead of multiplying them.

Now it's your turn. Here is another math problem and two choices.
Math Problem: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

(A)
Answer:
Michael started with 58 golf balls.
Then after losing 23 on tuesday, he had 58 -23 = 35.
After losing 2 more, he had 35 + 2 = 37 golf balls.
So the answer is 37.

(B)
def solution():
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result

Which of the above two choices can correctly answer the math problem?



Math problem: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

(A)
Answer:
There were originally 9 computers.
For each of 4 days from monday to thursday, 5 more computers were added.
So 5 * 4 = 20 computers were added.
So there are 9 + 20 = 29 computers now.
So the answer is 29.

(B)
def solution():
    computers_initial = 9
    computers_per_day = 5
    num_days = 5
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result

Which of the above two choices can correctly answer the math problem? 



Math Problem: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

(A)
Answer:
Shawn started with 5 toys.
If he got 2 toys from his mom and dad, then that is 2 more toys.
So he has 5 + 2 = 7 toys now.
So the answer is 7.

(B)
def solution():
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result

Which of the above two choices can correctly answer the math problem? 



Math problem: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

(A)
Answer:
There are 15 trees originally.
Then there were 21 trees after some more were planted.
So there must have been 21 - 15 = 6.
So the answer is 6.

(B)
def solution():
    trees_initial = 15
    trees_after = 21
    trees_added = trees_initial - trees_after
    result = trees_added
    return result

Which of the above two choices can correctly answer the math problem? 
'''.strip()


TURBO_SELECT_ASSISTANT = '''
(B) can correctly answer the math problem. Because (A) adds 2 more balls after losing 2 more on Wednesday instead of subtracting them.



(A) can correctly answer the math problem. Because (B) incorrectly uses 5 days instead of 4 days for the number of days computers were added.



(B) can correctly answer the math problem. Because (A) misunderstands the problem and thinks that Shawn got 2 toys from his mom and dad each instead of getting 2 toys from each of them.



(A) can correctly answer the math problem. Because (B) subtracts the final number of trees from the initial number of trees instead of subtracting the initial number of trees from the final number of trees.
'''.strip()


# === GPT-4 ===
GPT4_COT_SYSTEM = 'You are a helpful assistant that can solve math problems step by step.'

GPT4_COT_USER = '''
Let's solve the following math problems. You need to solve these math problems step by step. Here is one example how to do it,

Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

Answer:
Olivia had 23 dollars.
And she bought 5 bagels.
And each bagel costs 3 dollars.
So she spent 5 * 3 = 15 dollars.
So she has 23 - 15 = 8 dollars left.
So the answer is 8.


Now it's your turn. Here is another math problem:
Question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?



Question: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?



Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?



Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
'''.strip()

GPT4_COT_ASSISTANT = '''
Answer:
Michael started with 58 golf balls.
And he lost 23 golf balls on tuesday.
So after losing 23 on tuesday, he had 58 -23 = 35.
And then he lost 2 more golf balls on wednesday.
So after losing 2 more on wednesday, he had 35 - 2 = 33 golf balls.
So the answer is 33.



Answer:
There were originally 9 computers.
And 5 more computers were added from onday to thursday.
There are 4 days between monday and thursday.
So 5 * 4 = 20 computers were added in total.
So there are 9 + 20 = 29 computers now.
So the answer is 29.



Answer:
Shawn started with 5 toys.
And he got 2 toys each from his mom and dad.
So he got 2 + 2 = 4 toys.
Therefore, he has 5 + 4 = 9 toys now.
So the answer is 9.



Answer:
Jason started with 20 lollipops.
Then he had 12 after giving some to Denny.
So he gave Denny 20 - 12 = 8 lollipops.
So the answer is 8.
'''.strip()


GPT4_PAL_SYSTEM = 'You are a helpful assistant that can solve math problems by using Python code.'


GPT4_PAL_USER = '''
Let's use python to solve math problems. You need to write python code to answer these math problems. Here is one example how to do it,

Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

# solution in Python
def solution():
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result


Now it's your turn. Here is another math problem:
Question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

# solution in Python



Question: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

# solution in Python



Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

# solution in Python



Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

# solution in Python



'''.strip()


GPT4_PAL_ASSISTANT = '''
def solution():
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result



def solution():
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between monday and thursday
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result



def solution():
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result



def solution():
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result
'''.strip()

GPT4_SELECT_SYSTEM = '''You are a helpful assistant that can identify the correct answer to the math problem.'''

GPT4_SELECT_USER = '''
There are two choices to the same math problem. One uses natural language to answer the question, while the other uses Python code to answer it. Either of them can correctly answer the math problem. You need to identify which choice can correctly answer the math problem. Here is one example how to do it,

Math problem: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

(A)
Answer:
There were originally 9 computers.
For each of 4 days from monday to thursday, 5 more computers were added.
So 5 * 4 = 20 computers were added.
So there are 9 + 20 = 29 computers now.
So the answer is 29.

(B)
def solution():
    computers_initial = 9
    computers_added = 5
    computers_total = computers_initial + computers_added
    result = computers_total
    return result

Which of the above two choices can correctly answer the math problem?
(A) can correctly answer the math problem. Because (B) missed the fact that computers were added each day from monday to thursday.

Now it's your turn. Here is another math problem and two choices.
Math problem: A piece of square paper has a perimeter of 32 centimeters. Nicky's dog, Rocky, tore off 1/4 of the paper. What is the area of the remaining paper?

(A)
Answer:
A square has 4 equal sides.
The perimeter of the square paper is 32 centimeters.
So each side of the square is 32 / 4 = 8 centimeters.
The area of the whole square paper is side * side = 8 * 8 = 64 square centimeters.
Rocky tore off 1/4 of the paper.
So The area of the remaining paper is 1/4 * 64 = 16 square centimeters.
So the answer is 16.

(B)
def solution():
    perimeter = 32
    fraction_torn = 1 / 4
    area_total = (perimeter / 4) ** 2
    area_remaining = (1 - fraction_torn) * area_total
    result = area_remaining
    return result

Which of the above two choices can correctly answer the math problem?



Math problem: Bella has two times as many marbles as frisbees. She also has 20 more frisbees than deck cards. If she buys 2/5 times more of each item, what would be the total number of the items she will have if she currently has 60 marbles?

(A)
Answer:
Bella currently has 60 marbles.
She has two times as many marbles as frisbees, so she has 60 / 2 = 30 frisbees.
She has 20 more frisbees than deck cards, so she has 30 - 20 = 10 deck cards.
Now, she buys 2/5 times more of each item:
For marbles: 60 * (2/5) = 24 more marbles.
For frisbees: 30 * (2/5) = 12 more frisbees.
For deck cards: 10 * (2/5) = 4 more deck cards.
After buying more items, she will have:
Marbles: 60 + 24 = 84 marbles.
Frisbees: 30 + 12 = 42 frisbees.
Deck cards: 10 + 4 = 14 deck cards.
So, the total number of items she will have is 84 + 42 + 14 = 140.
So the answer is 140.

(B)
def solution():
    marbles_initial = 60
    frisbees_initial = marbles_initial * 2
    deck_cards_initial = frisbees_initial + 20
    marbles_bought = marbles_initial * 2 // 5
    frisbees_bought = frisbees_initial * 2 // 5
    deck_cards_bought = deck_cards_initial * 2 // 5
    marbles_total = marbles_initial + marbles_bought
    frisbees_total = frisbees_initial + frisbees_bought
    deck_cards_total = deck_cards_initial + deck_cards_bought
    total_items = marbles_total + frisbees_total + deck_cards_total
    result = total_items
    return result

Which of the above two choices can correctly answer the math problem? 



Math problem:: Pump A can fill a tank of water in 5 hours. Pump B can fill the same tank in 15 hours. How many minutes does it take the two pumps working together to fill the tank?

(A)
Answer:
Pump A can fill the tank in 5 hours.
So, Pump A can fill 1/5 of the tank in 1 hour.
Pump B can fill the tank in 15 hours.
So, Pump B can fill 1/15 of the tank in 1 hour.
When both pumps work together, they can fill (1/5 + 1/15) of the tank in 1 hour.
So they can fill (3/15 + 1/15) = 4/15 of the tank in 1 hour.
To convert 4/15 hours to minutes, we multiply by 60:
4/15 * 60 = 16 minutes.
So, the two pumps working together can fill the tank in 16 minutes.
So the answer is 16.

(B)
def solution():
    pump_a_rate = 1 / 5
    pump_b_rate = 1 / 15
    combined_rate = pump_a_rate + pump_b_rate
    time_to_fill = 1 / combined_rate
    time_to_fill_minutes = time_to_fill * 60  # Convert hours to minutes
    result = time_to_fill_minutes
    return result

Which of the above two choices can correctly answer the math problem?



Math problem: You can buy 4 apples or 1 watermelon for the same price. You bought 36 fruits evenly split between oranges, apples and watermelons, and the price of 1 orange is $0.50. How much does 1 apple cost if your total bill was $66?

(A)
Answer:
You bought 36 fruits evenly split between oranges, apples, and watermelons.
So you bought 36 / 3 = 12 of each fruit.
You bought 12 oranges and each orange costs $0.50.
So the cost of the oranges is 12 * $0.50 = $6.
Your total bill was $66, and the cost of the oranges was $6.
So the cost of the apples and watermelons combined is $66 - $6 = $60.
Assuming the price of watermelon is W, the price of one apple is A.
Knowing that you can buy 4 apples for the same price and that the price of one apple is A, then 1W=4A.
So we have the equation:
12A + 12W = $60 (total cost of apples and watermelons)
12A + 12(4A) = $60
60 A = $60
Then we know the price of one apple is A = $1
So the answer is 1.

(B)
def solution():
    total_fruits = 36
    total_bill = 66
    orange_price = 0.50
    fruits_per_type = total_fruits // 3
    oranges_cost = fruits_per_type * orange_price
    apples_watermelons_cost = total_bill - oranges_cost

    apple_price_ratio = 4
    watermelon_price_ratio = 1
    total_ratio = apple_price_ratio + watermelon_price_ratio

    apple_cost =  apple_price_ratio * (apples_watermelons_cost / total_ratio)
    apple_price = apple_cost / fruits_per_type

    result = apple_price
    return result

Which of the above two choices can correctly answer the math problem?
'''.strip()


GPT4_SELECT_ASSISTANT = '''
(B) can correctly answer the math problem. Because (A) incorrectly calculated the area of the torn-off portion instead of the remaining portion.



(A) can correctly answer the math problem. Because (B) incorrectly calculated the initial number of frisbees and deck_cards.



(B) can correctly answer the math problem. Because (A) incorrectly calculated the time to fill the tank.



(A) can correctly answer the math problem. Because (B) incorrectly calculates the apple_cost since 4 apples or 1 watermelon for the same price means 1 watermelon is 4 times the price of 1 apple. 
'''.strip()
