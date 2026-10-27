import heapq


def shared_workers(jobs, k, time_limit):
    if not jobs or k <= 0:
        return 0

    # Each entry is (when the worker is free, worker_id).
    workers = [(0, worker_id) for worker_id in range(k)]
    heapq.heapify(workers)
    completed_jobs = 0

    # Try shorter jobs first. Groups have the form [num_jobs, job_time].
    for num_jobs, job_time in sorted(jobs, key=lambda job: job[1]):
        for _ in range(num_jobs):
            available_time, worker_id = heapq.heappop(workers)
            finish_time = available_time + job_time

            if finish_time > time_limit:
                return completed_jobs

            completed_jobs += 1
            heapq.heappush(workers, (finish_time, worker_id))

    return completed_jobs


if __name__ == "__main__":
    assert shared_workers([[4, 3], [2, 1]], 2, 5) == 4
    assert shared_workers([[2, 2], [2, 1]], 2, 3) == 4
    assert shared_workers([[3, 2]], 0, 5) == 0
    assert shared_workers([[3, 0]], 2, 0) == 3
