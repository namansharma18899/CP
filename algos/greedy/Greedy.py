import functools

"""
About Greedy : Greedy is an algorithmic paradigm where we move to the solution step
 by step and at every step we choose the solution with the immediate and most benifit among others. 
So the problems where choosing the most locally optimum leads to the globally most
 optimum solution on compounding.
 Note : It's only applicable in cerain scenaios and not everywhere.
 It is applicable in : 
 1. Fractional Knapsack
 2. Dijkstra
 3. Hullman coding
 4. Travelling salesmen
 5. Job Sequencing
"""
# todo : FRACTIONAL KNAPSACK PROBLEM 


class JobSequence():
    def __init__(self,job_id,job_deadline,profit):
        self.jobid,self.job_deadline,self.profit=\
            job_id,job_deadline,profit
    
def calculate_most_profit(list_of_jobs : list):
    # sort wrt deadline and choose max profit in each deadline
    sorted_jobs = sorted(list_of_jobs,key=lambda job: job.job_deadline)
    previous_deadline = sorted_jobs[0].job_deadline
    result = [[sorted_jobs[0].jobid,sorted_jobs[0].profit]]
    for index, each_job in enumerate(sorted_jobs):
        if previous_deadline< each_job.job_deadline:
            result.append([each_job.jobid,each_job.profit])
        else: # when Equal 
            if each_job.profit > result[len(result)-1][1]:
                result.pop()
                result.append([each_job.jobid,each_job.profit])        
    return [x[0] for x in result]

class FractionalKnapsack():
    def __init__(self,start_time,end_time):
        self.start = start_time
        self.end = end_time    

    def __sort__(self):
        
        pass

def calculate_most_activities(list_of_activities: list):
    result = list()
    sorted_list = sorted(list_of_activities,key=lambda x: x.end)
    previous_end_time = sorted_list[0].start
    for index,activity in enumerate(list_of_activities):
        if previous_end_time<=activity.start:
            result.append(index)
            previous_end_time = activity.end        
    return [index(activity) for activity in 
    list_of_activities if activity in result]

if __name__=='__main__':
    arr = [FractionalKnapsack(10, 20),
        FractionalKnapsack(12, 25),
        FractionalKnapsack(20, 30)
    ]
    arr = [JobSequence('a', 1, 10),
    JobSequence('a', 4, 20),
    JobSequence('b', 10, 10),
    JobSequence('c', 1, 40),
    JobSequence('d', 1, 30),
    ]
    print(calculate_most_profit(arr))