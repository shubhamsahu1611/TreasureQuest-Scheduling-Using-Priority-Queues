import heap

'''
    Python file to implement the class CrewMate
'''

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        def comp(node1, node2):
            if node1.size+node1.arrival_time < node2.size+node2.arrival_time:
                return True
            elif node1.size+node1.arrival_time > node2.size+node2.arrival_time:
                return False
            else:
                return node1.id<node2.id
        self.tre_heap=heap.Heap(comp, [])
        self.current_load=0
        self.last_updation=0
        self.treasure_list=[]
        pass

    def add_treasure_to_crewmate(self, treasure):
        current_time=treasure.arrival_time
        last_updated=self.last_updation
        diff=current_time-last_updated
        while diff > 0 and self.tre_heap.size > 0:
            if diff >= self.tre_heap.arr[1].size:
                current_processor=self.tre_heap.extract()
                diff-=current_processor.size
                # self.current_load-=current_processor.size
                last_updated+=current_processor.size
                # current_processor.size=1e200
                current_processor.completion_time=last_updated
                # self.tre_heap.insert(current_processor)
            else:
                self.tre_heap.arr[1].size -= diff
                # self.current_load-=diff
                # diff-=self.tre_heap.arr[1].size
                break

        self.last_updation=current_time
        self.tre_heap.insert(treasure)
        # self.current_load+=treasure.size

    def get_time(self, ans):
        for x in self.treasure_list:
            self.add_treasure_to_crewmate(x)
        
        temp=self.last_updation
        while self.tre_heap.size > 0:
            top_ele=self.tre_heap.extract()
            if top_ele and (top_ele.completion_time is None):
                temp+=top_ele.size
                top_ele.completion_time=temp
                ans.append(top_ele)
            elif top_ele: ans.append(top_ele) 

            
    

    


    
    # Add more methods if required