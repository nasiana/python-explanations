# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 00:15:30 2021

@author: owned
"""


x = 5
print(id(x))
for i in range(x):
    x = 2
    print(id(x))
    print(i)
    
    
"""
# Results from this code being executed 

140733102072336
140733102072240
0
140733102072240
1
140733102072240
2
140733102072240
3
140733102072240
4
"""
    
# Hey, yes, that is more or less what is happening. The objective was to see that what x references outside the for loop is different to what is inside. i.e. the memory reference to x used in range(x) is different to the memory that x is pointing to inside the for loop after we do x=2.
# This is why even if we change x inside the for loop, the loop still iterates the original 5 times. But in Andreea's example, the id of our_list is the same (we're changing the contents of the list, not the list itself) and so that does affect the number of iterations that the for loop runs for.
# Now, we might reasonably ask,  we're assigning x=2 every time within the for loop, why does the id of x therefore *not* change on every iteration?
# This is because python is smart enough to know that the value we are setting is constant and will never change, so it doesn't need to assign more memory, it can just reuse what it has already assigned. (This is totally something you don't need to know but in case anyone is interested and for completeness, this is a common optimisation called Hoisting )
    