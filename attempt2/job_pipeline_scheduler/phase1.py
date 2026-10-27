def single_worker(jobs, time_limit):
    if not time_limit or not jobs: return 0
    jobs.sort(key=lambda j:j[1])
    total_job = 0
    for num_jobs, job_time in jobs:
        if not job_time: return 0
        max_jobs = time_limit // job_time
        total_job += min(num_jobs,max_jobs)
        time_limit -= min(num_jobs, max_jobs) * job_time
        
        if num_jobs >= max_jobs or time_limit <= 0:
            return total_job
    
    return total_job

jobs1 = [[3, 2], [1, 5], [2, 1]]
time_limit1 = 8

jobs2 = [[9,2]]
time_limit2 = 8

jobs3 = []
time_limit3 = 10

jobs4 = [[3, 2], [1, 5], [2, 1]]
time_limit4 = 0

jobs5 = [[3, 2], [1, 5]]
time_limit5 = 200

jobs6 = [[3, 0], [1, 0]]
time_limit6 = 200

jobs7= [[3, 0], [1, 0]]
time_limit7 = 0


assert single_worker(jobs1,time_limit1) == 5
assert single_worker(jobs2,time_limit2) == 4
assert single_worker(jobs3,time_limit3) == 0
assert single_worker(jobs4,time_limit4) == 0
assert single_worker(jobs5,time_limit5) == 4
assert single_worker(jobs6,time_limit6) == 0
assert single_worker(jobs7,time_limit7) == 0