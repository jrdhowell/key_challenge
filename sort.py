

def solution(num_buns, num_required):
   
   #visited will store booleans to direct where
   #to place keys
   global visited
   visited = []


   #fuction to create next key's pattern
   #stored in global variable visited
   #funciton takes no argument
   #updates visited based on state visited is in
   
   def countup():
       
      visitcount = 0
      
     #count the number of visits (True)
      for x in range(len(visited)):
          if visited[x]:
              visitcount += 1
      
      #function to find the last visit space 
      #in first 'n' entries in the list
      def findnext(n):
          for x in range(len(visited)-n):
              if visited[x]:
                  tmp = x
          return tmp
       
     
      #find target: the current index in visited 
      #where the transformation to the next cycle state will begin
      #target with be the last visit (True) entry
      #that has a not visited (False) following it
      target = 0  
      for x in range(visitcount):
         target = findnext(x)
         if target != len(visited) - 1 - x:
             break
      

      #check to see if there are no visited (True)
      #with a non visited (False) following.
      #If there are none, the solution is complete
      if target == len(visited) - visitcount:
         check = True
         for x in range(visitcount):
            if not visited[target+x]:
                check = False
          
         if check:
             return
      
      
      #Tranform visited to the next state where the keys will go
      #if the final entry is visited, the target changes to not visited
      #and entry following target becomes visit (True)
      count = 0               
      if visited[len(visited)-1]:
           for x in range(len(visited)):
              
              if x == target:
                  visited[target] = False
                  for y in range(len(visited) - target - 1):
                      if visitcount - count > 0 :
                        visited[y + x + 1] = True
                      else:
                        visited[y + x + 1] = False
                      count += 1
                  return
              if visited[x]:
                  count+=1
                  
      #if the final entry is not visited
      #target become not visited (False)
      #entry following target becomes visited (True)
      visited[target] = False
      visited[target + 1] = True
   
   
   #ans will store solution (array of array to describe keys)
   ans = [[]]*num_buns
   #key will hold our current key
   key = 0
    

   #create initial visited state 
   for x in range(num_buns):
       visited.append(False)
   for x in range(len(visited) - num_required + 1):
        visited[x] = True
   
   #using check, we will check when solution is complete below
   check = False
   while not check:
      
      
      #add the key to our solution as directed by
      #visited
      for x in range(num_buns):
          if visited[x]:
              ans[x] = ans[x] + [key]
      
      #find the next state for visited
      countup()
      
      
      #increase key for next state
      key += 1  
      check = True
      
      #check if ans arrays are all the same lenghth.
      #if so, solution is complete
      for x in range(len(visited)):
        if len(ans[0]) != len(ans[x]):
            check = False
         
   return(ans)    


    
print(solution(6,5))

