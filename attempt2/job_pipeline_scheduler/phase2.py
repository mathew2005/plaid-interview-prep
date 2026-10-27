def multiple_workers(jobs,time_limit):
    if not jobs or not time_limit: return 0
    total_jobs = 0
    for num_jobs, job_time, num_workers in jobs:
        group_time = time_limit
        max_jobs = (group_time // job_time) * num_workers
        total_jobs += min(num_jobs, max_jobs)

    return total_jobs

jobs1 = [[5, 2, 2], [3, 4, 1]]
time_limit1 = 6

jobs2 = [[9,2,10]]
time_limit2 = 8

jobs3 = []
time_limit3 = 10

jobs4 = [[9, 2,10]]
time_limit4 = 0

jobs5 = [[3, 2,10], [1, 300, 3]]
time_limit5 = 200

jobs6 = [[3, 0,0], [1, 0, 0]]
time_limit6 = 200

jobs7= [[3, 0, 0], [1, 0, 0]]
time_limit7 = 0


assert multiple_workers(jobs1,time_limit1) == 6
assert multiple_workers(jobs2,time_limit2) == 9
assert multiple_workers(jobs3,time_limit3) == 0
assert multiple_workers(jobs4,time_limit4) == 0
assert multiple_workers(jobs5,time_limit5) == 4
assert multiple_workers(jobs6,time_limit6) == 0
assert multiple_workers(jobs7,time_limit7) == 0