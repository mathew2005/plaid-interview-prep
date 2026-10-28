# [User Consent Scope Tracker](https://demo.gothamloop.com/company/plaid?qid=396cbb56-99c1-4000-b5d5-7ff6d4b77ce1)

- Source: GothamLoop, Plaid Interview Question Bank (demo, free question)
- Type: Coding
- Popularity: Popular! 9/10, frequency indicated Very high in the bank list
- Topics: Hash Tables, Simulation
- Round / difficulty: none shown for this question on the page
- Status: click the title above for the full question on GothamLoop

## Summary

Tracking consent for connected bank-account data over time, in 3 parts:

1. Current active scopes: which scopes remain active for each user/item.
2. Historical scope check: whether a particular scope was active at a given time.
3. Product permission check: whether a product call would be permitted at a given time based on its required scopes.

## Overlap notes

- Consent / scope tracking over time is a new topic in this repo, distinct from attempt1/routing_number (bank identifier mapping) and attempt1/rate_limiter.
- The historical check and permission check parts make this a state-over-time simulation, so it pairs well with the pipeline and rate limiter practice in attempt1/.

No solution code is included yet - that is for working on in Codespaces.
