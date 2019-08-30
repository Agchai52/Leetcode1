class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        '''
        0. Use hash table to count # of each task
        1. How many idle should be inserted to satisfy n
        2. Start from the task with most number
        3. No idle, num of different types > n, return n
        4. When to add idle, num of different types < n
        
        step1: create a hash table count {task:num}
        step2: Each loop, count different types of task (t): > n, continue; <= n, idle += n-t+1. then all num of task-1
        step3: Until all task num == 0, return len(tasks) + idle
        '''
        if n == 0: return len(tasks)
        val = len(tasks)
        count = collections.Counter(tasks)      
        most = count.most_common()[0][1]
        num_most = len([k for k, v in count.items() if v == most])
        time = (most - 1) * (n+1) + num_most
        return max(time, val)
