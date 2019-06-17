# oq-guru
Better way to get help with Objective questions

My setup for this example:  
MAX_right_count = **2**  
MAX_WRONG_count = **20**  
MAX_ITERATIONS = **20**

**Eg:**  
**Questions** = [q1,q2,q3]  
1st iteration:  
```
q1.answer = a and my answer was a:  
    q1.right_count = 1  
q2.answer = b but my answer was a:  
    q2.wrong_count = 1  
q3.answer = c but my answer was a:  
    q3.wrong_count = 1  
```
    (questions sorted at the end of the first iteration):  

**Questions** = [q2,q3,q1]  
2nd iteration:  
```
q2.answer = b but my answer was a:  
    q2.right_count = 1  
    q2.wrong_count = 1  
q3.answer = c but my answer was a:  
    q3.wrong_count = 2  
q1.answer = a and my answer was a:  
    q1.right_count = 2
```
    
    (questions sorted at the end of the this iteration):  

**Questions** = [q3,q2] (q1 is deleted because I got it right 2 times contenously)  
#### and so on... until max iterations is reached or until I get all questions right 2 times in a row.

## Use case: I want to take PSC Nepal test for computer operator
50 multiple choice questions are asked in the exams and if you ace it you are through the first phase.  
There are about 5000 multiple choice questions in a book I got recently to prepare for the exams.  

### How does it help?
**Step 1:** I input those 5000 questions into this app.  
**Step 2:** I go through all the questions in the first iteration and this app keeps track of  
how many times I got any particular question wrong and right.  
**Step 3:** Once I go through all the questions, questions are sorted based on their wrong_count  
and previous position.  
**(The question with the most wrong_count gets to me first in the next iteration)**  
**(The question with 2 countenous right_count gets deleted leaving me with less questions every iteration)**  
**Step 4:** I save and use time more efficiently.  
