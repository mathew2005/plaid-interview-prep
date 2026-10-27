# Plaid Interview: Job Pipeline Scheduler

You're building a job scheduler. Each job type comes in as a list, and you want to know how much work can be finished before a deadline.

## Part 1: Single worker

You're given a list of job groups, where each group is `[num_jobs, job_time]`, plus an integer `time_limit`. One worker processes jobs one at a time, in any order. Return the **maximum number of jobs** that can be completed within `time_limit`.

```
jobs = [[3, 2], [1, 5], [2, 1]]
time_limit = 8
-> 5
```

Do the two 1-unit jobs (time 2), then three 2-unit jobs (time 8).

## Part 2: Dedicated workers

Each group now has a third value: `[num_jobs, job_time, num_workers]`. Each group's workers only handle that group's jobs, and all workers run concurrently. Return the total number of jobs completed within `time_limit`.

```
jobs = [[5, 2, 2], [3, 4, 1]]
time_limit = 6
-> 6
```

Group 1: each worker can finish 3 jobs, so 6 total, capped at 5. Group 2: one worker finishes 1 job.

## Part 3 (likely follow-up)

Instead of dedicated workers, there's a **shared pool of `k` workers** that can take any job. Return the maximum number of jobs completed within `time_limit`.

```
jobs = [[4, 3], [2, 1]]
k = 2, time_limit = 5
-> 4
```

*Note: the original description didn't specify part 3; this is a guess based on the heap hint.*

## Edge cases to test

- `time_limit = 0`, or an empty job list
- A group with `num_jobs = 0` or `num_workers = 0`
- A job that takes longer than the whole time limit
- A job finishing exactly at `time_limit` (does it count?)
- Very large `num_jobs` (can you avoid looping job by job?)
- Duplicate `job_time` values across groups

## Prep tips

Practice problems using dictionaries, sets, and heaps. Write your own test cases while practicing: you'll get examples, but the interviewer will ask you to come up with edge cases and test them.

## Source

This problem was rebuilt from a single source: a message from someone who interviewed at Plaid. No outside websites or other references were used. Parts 1 and 2 come from that message; Part 3, the examples, and the edge-case list were written by Claude based on it.

Original message, word for word:

> hey bro, I got a pipeline question
> A 3 part problem and had to do use some math and a heap, like processing stages and jobs. It went chill tho, my interviewer was very nice. Now we wait :pray:make sure u practice problems with dictionaries, sets, and maybe heapsmake sure u also like write test cases during practice. They give you some example, but then they ask you like to think of edge cases and then test those
>
>
> Heres nore info:
>
>
> So u get a list of lists and each list has (num_jobs, job_time) and u get a time limit. Return the amount of jobs you can do given the time limit
>
> then u get a third item in the lists that has num_workers. Workers can complete jobs concurrently. Now return the num of jobs u can do
>
> This is for plaid