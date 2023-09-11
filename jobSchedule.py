class Job:
  def __init__(self,taskId, profit, deadline):
    self.taskId = taskId
    self.profit = profit
    self.deadline = deadline

def scheduleJobs(jobs, dlLimit):
  slots =[-1]*dlLimit
  maxProfit =0
  jobs.sort(key=lambda x: x.profit, reverse = True)

  for job in jobs:
    for i in reversed(range(job.deadline)):
      if i<dlLimit and slots[i]==-1:
        slots[i]= job.taskId
        maxProfit += job.profit
        break
        
  print("The scheduled jobs are: ", list(filter(lambda x: x!=-1, slots)))
  print("Maximum profit gained: ", maxProfit)


if __name__=='__main__':
  n = int(input("Enter the number of jobs: "))
  jobs =[]
  for i in range(n):
    taskId = int(input(f"Enter the task ID for job {i+1}: "))
    deadline = int(input(f"Enter the deadline for job {i+1}: "))
    profit= int(input(f"Enter the profit for job {i+1}: "))

    jobs.append(Job(taskId,profit,deadline))

  dlLimit = int(input("Enter the deadline limit: "))
  scheduleJobs(jobs, dlLimit)
  