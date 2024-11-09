'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.arr=[-1]
        self.size=0
        self.comp=comparison_function
        for x in init_array:
            self.insert(x)
        pass
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.size += 1
        self.arr.append(value)
        index = self.size

        # Bubble up to maintain the max heap property
        while index > 1:
            parent = index // 2
            if self.comp(self.arr[index] , self.arr[parent]):
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                return
        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.size==0:
            return None
        mini=self.arr[1]
        self.deletion()
        # self.size-=1
        return mini
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.size==0:
            return None
        return self.arr[1]
        pass
    
    # You can add more functions if you want to

    def deletion(self):
        '''
        Arguments:
            None
        Description:
            Removes the root element and reorganizes the heap
        '''
        if self.size == 0:
            return
        
        # Move the last element to the root
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        self.arr.pop()  # Remove the last element
        
        i = 1
        while i <= self.size:
            left = 2 * i
            right = 2 * i + 1
            largest = i
            
            # Check left child
            if left <= self.size and self.comp(self.arr[left], self.arr[largest]):
                largest = left
            
            # Check right child
            if right <= self.size and self.comp(self.arr[right], self.arr[largest]):
                largest = right
            
            # If the largest value is not the current node
            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                i = largest
            else:
                break