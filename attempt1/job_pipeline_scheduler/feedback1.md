# Feedback 1: Single-Worker and Multiple-Worker Problem

## Bottom line

The core ideas are on the right track, but both implementations need another pass before they are interview-ready. Phase 1's approach is correct but does unnecessary work. Phase 2 handles ordinary positive inputs but can hang when a group has jobs and zero workers.

## Feedback against Plaid's interview criteria

The interview guide lists **correctness, efficiency, organization & planning, code quality, testing, and communication** as evaluation areas. These estimates are based on the code, not an official Plaid score. Communication cannot be assessed from code alone.

| Area | Estimate | What the code shows |
|---|---:|---|
| Correctness | 6/10 | Phase 1's greedy choice is sound. Phase 2 works for normal positive inputs, but its zero-worker behavior is a correctness blocker. |
| Efficiency | 3/10 | Both implementations loop over jobs or worker rounds when the answer can be calculated arithmetically. |
| Organization & planning | 5/10 | The milestones are separated into clear functions, but the code does not show the assumptions or reasoning behind the approaches. |
| Code quality | 4/10 | The main logic is readable, but Phase 2 also runs tests on import, and the test setup has problems. |
| Testing | 3/10 | Edge cases are being considered, which is good. However, the tests print booleans instead of asserting results, and one expected result is wrong. |
| Communication | Not assessable | Code alone cannot show how clearly you talk through your plan or respond to feedback. |

## Phase 1: Single worker

In [`phase1.py`](./phase1.py), sorting job groups by duration is the right strategy: the shortest jobs let you complete the most jobs before the deadline. The example returns the expected answer.

The inefficiency is the inner loop over every job. With a very large job count, runtime grows with the number of jobs, even though each group can be handled in one calculation. After sorting, take as many jobs as fit:

```python
take = min(num_jobs, remaining_time // job_time)
```

Handle zero-duration jobs separately: if the count is positive, they all fit without consuming time. The current `jobs.sort(...)` also changes the caller's list; sorting a copy avoids that side effect.

## Phase 2: Dedicated workers

In [`phase2.py`](./phase2.py), the batching idea is directionally right, but repeating one loop per worker round is unnecessary. For a group with positive job duration:

```python
completed = min(num_jobs, num_workers * (time_limit // job_time))
```

Handle the boundary cases explicitly: zero workers means zero jobs; zero-duration jobs can all finish when there is at least one worker. In the current code, a group with jobs and zero workers never makes progress, so its loop does not end. The script's zero-worker test reaches that case.

There are also test-quality issues: the checks print `True`/`False` instead of failing when an expected result is wrong, and the last assertion expects 2 jobs from an input containing 0 jobs; it should expect 0. Keeping tests out of top-level module code also avoids executing them just by importing the function.

## How to present this in a one-hour interview

Spend a few minutes clarifying assumptions first: are counts, durations, and worker counts nonnegative; do jobs take a fixed duration; and does a zero-duration job count as complete? Then state the plan before coding:

1. **Single worker:** sort by duration, then consume each group in bulk. Explain that replacing a longer selected job with a shorter available one cannot increase total time, so shortest-first maximizes the count.
2. **Dedicated workers:** groups are independent; calculate each group's per-worker capacity from the deadline, multiply by its worker count, and cap at its available jobs.
3. Test the sample, exact-deadline completion, empty/zero counts, zero duration, zero workers, and a huge count. State the time complexity and any input assumptions.

That approach demonstrates the guide's planning and efficiency criteria while leaving time to test and adapt if the interviewer changes the requirements. The guide also says to talk through the approach before coding and to aim for a working solution across multiple milestones.
