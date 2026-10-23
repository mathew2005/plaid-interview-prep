# shared pool of k workers
# can take any job
# max num of jobs (completed within time_limit)

def shared_workers(jobs,k,time_limit):
    jobs.sort(key = lambda j:j[1])
    # [2,1] -> total += 2, time = 1
    # [4,3] -> total += 4 time = 6
    # total => 4
    # wokers transitioning
    # [[2,1], [4,3]] k = 3, time = 6
    # [2,1] -> [0,1] -> total += 2, time = 1
    for num_jobs, job_time in jobs:
        remaining_workers = max(0, k - num_jobs)
        total_workers = k + remaining_workers

        while num_jobs > 0:
            num_jobs -= min(num_jobs, total_workers)
    