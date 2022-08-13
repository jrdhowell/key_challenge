# Code Challenge: Distributing Keys

Create a function, solution(num_buns, num_required), that takes two integers as arguments and 
returns a matrix (array of lists) representing distribution of keys to the number of volunteer (num_buns) 
to unlock a number of locks (num_required).

Distribution of the keys: Argument num_buns is the total number of volunteers able to hold the keys and
num_required is the number of locks. Keys (up to 10, labeled 0-9) must be distributed to volunteers in a
manner such that any set of the volunteers equaling the number of locks (num_required) will in total have a complete set of keys.
More than one volunteer may have the same key, but must use the least amount of type of keys and keys per type as possible.


<br/>
<br/>

**For example:**

num_buns = 4 
num_required = 4

Key distrubution:

[[0], [1], [2]. [3]]

<br/><br/>
**Or given:** 

num_buns = 4
num_required = 1

Key distribution: 

[[0], [0], [0], [0]]

<br/>
<br/>

## Code and Resources Used
**Python:** Python 3.8.10 <br/>
**Packages:** none <br/>
