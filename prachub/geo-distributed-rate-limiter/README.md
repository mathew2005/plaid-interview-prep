# Design a geo-distributed rate limiter

Source: https://prachub.com/interview-questions/design-a-geo-distributed-rate-limiter

- Type: System Design, Rate Limiting
- Difficulty: Easy
- Round: Technical Screen
- People solved (PracHub proxy, Oct 27, 2026): 758
- Date shown on PracHub: Feb 4, 2026
- Overlap note: rate limiter-related, but a different, system-design angle from attempt1/rate_limiter (per-second and sliding-window limiting). Added anyway, as requested.

## Summary

Design globally consistent rate limiting across regions, with per-API-key (and possibly per-IP/endpoint) limits that are not multiplied by the region count, low request-path latency, and tolerance for region failures. A follow-up compares prioritizing highest-cost tasks first versus maximizing task count.

## Status

Question only. No solution code yet.
