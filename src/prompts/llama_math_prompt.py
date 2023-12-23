SYSTEM_MESSAGE = '''You are a helpful and brilliant assistant. You are a math expert who can identify the correct answer to the math problem.'''

# === Selector: Llama-2-7B-Chat ===
USER_7B_CHAT = '''There are two choices to the same math problem. One uses natural language to answer the question, while the other uses Python program to answer it. *ONLY ONE* of them can correctly answer the math problem. 
You need to check these two solutions carefully and identify which choice can correctly answer the math problem. 

Here is the math problem and two solutions to it.
Math problem: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

(A)
def solution():
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result
The result is 8.

(B)
Answer:
Olivia had 23 dollars.
5 bagels for 3 dollars each will be 5 + 3 = 8 dollars.
So she has 23 - 8 = 15 dollars left.
The answer is 15.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math Problem: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

(A)
def solution():
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial + golf_balls_lost_tuesday
    result = golf_balls_left
    return result
The result is 81.

(B)
Answer:
Michael started with 58 golf balls.
Then after losing 23 on tuesday, he had 58 -23 = 35.
After losing 2 more, he had 35 - 2 = 33 golf balls.
So the answer is 33.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

(A)
def solution():
    computers_initial = 9
    computers_per_day = 5
    num_days = 4
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result
The result is 29.

(B)
Answer:
There were originally 9 computers.
For each of 5 days from monday to thursday, 5 more computers were added.
So 5 * 5 = 25 computers were added.
So there are 9 + 25 = 34 computers now.
So the answer is 34.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math Problem: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

(A)
def solution():
    toys_initial = 5
    mom_dad_toys = 2
    total_received = mom_dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result
The result is 7.

(B)
Answer:
Shawn started with 5 toys.
If he got 2 toys from his mom and dad, then that is 4 more toys.
So he has 5 + 4 = 9 toys now.
So the answer is 9.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

(A)
def solution():
    trees_initial = 15
    trees_after = 21
    trees_added = trees_after - trees_initial
    result = trees_added
    return result
The result is 6.

(B)
Answer:
There are 15 trees originally.
Then there were 21 trees after some more were planted.
So there must have been 15 - 21 = -6.
So the answer is -6.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

(A)
def solution():
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = leah_chocolates - chocolates_eaten
    result = chocolates_left
    return result
The result is -3.

(B)
Answer:
Originally, Leah had 32 chocolates.
And her sister had 42.
So in total they had 32 + 42 = 74.
Then after eating 35, they had 74 - 35 = 39.
The answer is 39.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

(A)
def solution():
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result
The result is 5.

(B)
Answer:
There are originally 3 cars.
Then 2 more cars arrive.
So there are 3 + 2 = 5 cars.
So there are 5 + 2 = 7 cars now.
The answer is 7.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

(A)
def solution():
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial + jason_lollipops_after
    result = denny_lollipops
    return result
The result is 32.

(B)
Answer:
Jason started with 20 lollipops.
Then he had 12 after giving some to Denny.
So he gave Denny 20 - 12 = 8.
The answer is 8.

Which of the above two choices can correctly answer the math problem? (A) or (B)?
'''.strip()


ASSISTANT_7B_CHAT= '''(A) can correctly answer the math problem. Because (B) adds the number of bagels to the cost of each bagel instead of multiplying them.


(B) can correctly answer the math problem. Because (A) adds 2 more balls after losing 2 more on Wednesday instead of subtracting them.


(A) can correctly answer the math problem. Because (B) incorrectly uses 5 days instead of 4 days for the number of days computers were added.


(B) can correctly answer the math problem. Because (A) misunderstands the problem and thinks that Shawn got 2 toys from his mom and dad each instead of getting 2 toys from each of them.


(A) can correctly answer the math problem. Because (B) subtracts the final number of trees from the initial number of trees instead of subtracting the initial number of trees from the final number of trees.


(B) can correctly answer the math problem. Because (A) incorrectly subtracts the chocolates eaten only from Leah's chocolates instead of subtracting them from the total chocolates.


(A) can correctly answer the math problem. Because (B) incorrectly adds 2 cars twice instead of just adding them once.


(B) can correctly answer the math problem. Because (A) incorrectly adds the initial number of jason's lollipops and 12 instead of subtracting them.
'''.strip()


# === Selector: Llama-2-13B-Chat ===
USER_13B_CHAT = '''There are two choices to the same math problem. One uses natural language to answer the question, while the other uses Python program to answer it. *ONLY ONE* of them can correctly answer the math problem. 
You need to check these two solutions carefully and identify which choice can correctly answer the math problem. 

Here is the math problem and two solutions to it.
Math problem: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

(A)
Answer:
Olivia had 23 dollars.
5 bagels for 3 dollars each will be 5 * 3 = 15 dollars.
She has 23 - 15 = 8 dollars left.
The answer is 8.

(B)
def solution():
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels + bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result
The result is 15.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math Problem: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

(A)
Answer:
Michael started with 58 golf balls.
Then after losing 23 on tuesday, he had 58 -23 = 35.
After losing 2 more, he had 35 + 2 = 37 golf balls.
The answer is 37.

(B)
def solution():
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result
The result is 33.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

(A)
Answer:
There were originally 9 computers.
For each of 4 days from monday to thursday, 5 more computers were added.
5 * 4 = 20 computers were added.
So there are 9 + 20 = 29 computers now.
The answer is 29.

(B)
def solution():
    computers_initial = 9
    computers_per_day = 5
    num_days = 5
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result
The result is 34.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math Problem: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

(A)
Answer:
Shawn started with 5 toys.
If he got 2 toys from his mom and dad, then that is 2 more toys.
So he has 5 + 2 = 7 toys now.
The answer is 7.

(B)
def solution():
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result
The result is 9.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

(A)
Answer:
There are 15 trees originally.
Then there were 21 trees after some more were planted.
There must have been 21 - 15 = 6.
The answer is 6.

(B)
def solution():
    trees_initial = 15
    trees_after = 21
    trees_added = trees_initial - trees_after
    result = trees_added
    return result
The result is -6.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

(A)
Answer:
There are originally 3 cars.
Then 2 more cars arrive.
So there are 3 + 2 = 5 cars.
So there are 5 + 2 = 7 cars now.
The answer is 7.

(B)
def solution():
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result
The result is 5.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

(A)
Answer:
Originally, Leah had 32 chocolates.
And her sister had 42.
So in total they had 32 + 42 = 74.
Then after eating 35, they had 74 - 35 = 39.
The answer is 39.

(B)
def solution():
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = leah_chocolates - chocolates_eaten
    result = chocolates_left
    return result
The result is -3.

Which of the above two choices can correctly answer the math problem? (A) or (B)?




Math problem: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

(A)
Answer:
Jason started with 20 lollipops.
Then he had 12 after giving some to Denny.
So he gave Denny 20 + 12 = 32.
The answer is 32.

(B)
def solution():
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result
The result is 8.

Which of the above two choices can correctly answer the math problem? (A) or (B)?
'''.strip()


ASSISTANT_13B_CHAT = '''(A) can correctly answer the math problem. Because (B) adds the number of bagels to the cost of each bagel instead of multiplying them.


(B) can correctly answer the math problem. Because (A) adds 2 more balls after losing 2 more on Wednesday instead of subtracting them.


(A) can correctly answer the math problem. Because (B) incorrectly uses 5 days instead of 4 days for the number of days computers were added.


(B) can correctly answer the math problem. Because (A) misunderstands the problem and thinks that Shawn got 2 toys from his mom and dad each instead of getting 2 toys from each of them.


(A) can correctly answer the math problem. Because (B) subtracts the final number of trees from the initial number of trees instead of subtracting the initial number of trees from the final number of trees.


(B) can correctly answer the math problem. Because (A) incorrectly adds 2 cars twice instead of just adding them once.


(A) can correctly answer the math problem. Because (B) incorrectly subtracts the chocolates eaten only from Leah's chocolates instead of subtracting them from the total chocolates.


(B) can correctly answer the math problem. Because (A) incorrectly adds the initial and final number of lollipops instead of subtracting them to get the number of lollipops given to Denny.
'''.strip()
