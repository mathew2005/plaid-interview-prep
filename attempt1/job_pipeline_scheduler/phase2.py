def dedicated_worker(jobs, time_limit):
    total_job = 0
    for num_jobs, job_time, num_workers in jobs:
        group_time = 0
        while num_jobs > 0 and group_time + job_time <= time_limit:
            remaining = min(num_workers, num_jobs)
            num_jobs -= remaining
            group_time += job_time
            total_job += remaining
    return total_job


print(dedicated_worker([[5, 2, 2], [3, 4, 1]], 6) == 6)
print(dedicated_worker([[5, 12, 2], [3, 14, 1]], 6) == 0)
print(dedicated_worker([[5, 2, 2], [3, 4, 1]], 0) == 0)
print(dedicated_worker([[5, 2, 0], [3, 4, 0]], 6) == 0)
print(dedicated_worker([[5, 0, 2], [3, 0, 1]], 6) == 8)
print(dedicated_worker([[0, 2, 2], [0, 4, 1]], 6) == 0)
print(dedicated_worker([[5, 2, 2], [3, 4, 1]], 2) == 2)
assert dedicated_worker([[0,0,0]], 2) == 2