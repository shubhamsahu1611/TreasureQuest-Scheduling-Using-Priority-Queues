'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here

        def comp(crewmate1, crewmate2):
            return crewmate1.current_load < crewmate2.current_load
        
        # Create m crewmates and store in a heap
        self.crewmates = [crewmate.CrewMate() for _ in range(m)]
        self.crewmate_heap = heap.Heap(comp, self.crewmates)
        # arr=[0]*m

        # self.crewmates=heap.Heap(comp, arr)

        self.treasure_count=0
        self.treasure_list=[]
        self.crewmate_size=m
        pass
    
    def add_treasure(self, treasure_to_insert:treasure.Treasure):
        '''
        Arguments:
            treasure : Treasure : The tre asure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        self.treasure_count+=1
        self.treasure_list.append(treasure_to_insert)

        # Find the crewmate with the least load
        least_loaded_crewmate = self.crewmate_heap.extract()
        
        # Add the treasure to the crewmate's heap
        least_loaded_crewmate.treasure_list.append(treasure_to_insert)
        if least_loaded_crewmate.current_load> treasure_to_insert.arrival_time:
            least_loaded_crewmate.current_load+=treasure_to_insert.size
        else :least_loaded_crewmate.current_load+=(treasure_to_insert.size+treasure_to_insert.arrival_time)
        # least_loaded_crewmate.current_load+=treasure_to_insert.size
        # Reinsert the updated crewmate back into the crewmate heap
        self.crewmate_heap.insert(least_loaded_crewmate)

        pass
    



    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        


        # Write your code here
        ans=[]
        if self.treasure_count  <  self.crewmate_size:
            for x in self.treasure_list:
                x.completion_time=x.arrival_time+x.size
                ans.append(x)

        else:
            for i in range (1, len(self.crewmate_heap.arr)):
                if len(self.crewmate_heap.arr[i].treasure_list)==0:
                    continue
                # print(self.crewmate_heap.arr[i].current_load)
                self.crewmate_heap.arr[i].get_time(ans)
                # print(ans)
        def comp(x):
            return x.id

        ans=sorted(ans, key=comp)
        return ans

        
         

    # You can add more methods if required