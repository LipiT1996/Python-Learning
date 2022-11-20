"""
Quiz app:
Create a text file consisting of q/a, for example 1+1=2, 2+2=4, 3+6=9. 
Load the text file and split each equation leading to a list ['1+1=2', '2+2=4', '3+6=9']
make variable score to collect all the collect answer given by the user
for loop to separate question and answer using '=' as the separator
ans variable giving the equation as a question and asks user to input the answer.
Every time the user gets correct answer, the score increases by one.
wriitng the final result to the result.txt file
"""

file_content = open("questions.txt", 'r')
q_and_a = [i.strip() for i in file_content]
file_content.close()
print(q_and_a)

score = 0
total = len(q_and_a)


for i in q_and_a:
    q,a = i.split('=')
    ans = input(f'{q}:')

    if ans == a:
        score +=1

result_write = open('results.txt', 'w')
result_write.write(f"Your final score is {score}/{total}")
result_write.close



