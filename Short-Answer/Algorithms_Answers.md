#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  Time : a  < nnn ->n^3. 
        --> incrementing by n^2, drop constant  --> when n is cubed so is the running time. 
        O(n)
    Space: O(c)?? -> `a` is reassigned in each iteration


b) Time -> nested loop, second loop runs in the same number in each iteration-->  O(n^2)


c) Time -> recursive calls, and decrements on each iteration --> O(n)

## Exercise II
determine maximum height it takes to drop egg and for it to not break


n= n-story building floors
f= current floor 

PLAN
possible binary search?? 
Time: O(log n)
Space: O(1)

lower= O
max= n


`start` = [lower, mid]
drop egg from `start` and if it breaks

adjust start and end bounds of the bottom half floor
and move towards the middle of the new formed bounds,
repeat the pattern until we find the floor level that it doesnt break and the floor level above that it breaks. 
we return current floor 




