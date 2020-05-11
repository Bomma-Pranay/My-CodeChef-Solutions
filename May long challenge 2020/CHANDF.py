Problem link  : https://www.codechef.com/MAY20B/problems/CHANDF/

My solution:

tc=int(input())
for xyz in range(tc):
    lis=list(map(int,input().split()))
    x,y,l,r=lis[0],lis[1],lis[2],lis[3]
    #print(x|y)
    if x==0 or y==0 :
        print(0)
    else:
        print((x|y))

'''
Chef and Bitwise Product Problem Code: CHANDF

Chef got interested in bits and wanted to learn about them, so his friend Pintu gave him a special function F(X,Y,Z)=(X∧Z)⋅(Y∧Z), where ∧ is the bitwise AND operator and X,Y,Z are non-negative integers.

Pintu wants Chef to maximise the function F(X,Y,Z) for given X and Y by choosing an appropriate Z. However, to make it interesting, Pintu also gave Chef limits L and R for Z. In other words, he wants Chef to find a non-negative integer Z (L≤Z≤R) such that F(X,Y,Z)=maxL≤k≤R(F(X,Y,k)). If there is more than one such value of Z, he should find the smallest one in the range [L,R].

Since Chef is busy cooking in the kitchen, he needs you to help him solve this problem.

Note: X, Y, L and R are chosen in such a way that maxL≤k≤R(F(X,Y,k)) never exceeds 262.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains four space-separated integers X, Y, L and R.
Output
For each test case, print a single line containing one integer ― the smallest value of Z in the given range that maximises F.

Constraints
1≤T≤105
0≤X,Y≤1012
0≤L≤R≤1012
Subtasks
Subtask #1 (15 points):

L=0
R≥2⋅max(X,Y)
Subtask #2 (25 points): L=0
Subtask #3 (60 points): original constraints

Example Input
2
7 12 4 17
7 12 0 8
Example Output
15
7
Explanation
Example case 1: Here, Z=15 maximises the function, since F(7,12,15)=84. It is impossible to reach F>84 with any Z in the given range.

Example case 2: The smallest Z which maximises F is Z=7, and the value of F for this Z is 28.
'''
