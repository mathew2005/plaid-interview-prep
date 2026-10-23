def single_worker(jobs, time_limit):
    total_time, total_jobs = 0, 0
    jobs.sort(key=lambda j:j[1])
    for num_jobs, job_time in jobs:
        for _ in range(num_jobs):
            if total_time + job_time > time_limit:
                return total_jobs
            total_time += job_time
            total_jobs += 1

    return total_jobs

