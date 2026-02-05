# TODO List

1. Make use of UUID
2. Admin role

3. Status codes instead of objects returned
4. Error Handling
5. Safe Delete
6. Pagination
7. Add season description(AI tools/Google search/Api Request)
8. Change URL ADDRESSES TO REST
9. Docker + Kubernetes
10. Migration to POSTGRESQL/MYSQL
11. Microservices(Authorisation + Logging)
12. Review episode schema
13.

```markdown
    15. Bulk Quote Import
    POST /quotes/bulk
    Payload: list of quotes.

    16. Soft Deletes
    Instead of deleting:
    is_deleted = true

    17. Integrity Rules
    Examples:
    Quote must belong to an episode from the same season
    Catchphrase length limit

    18. Caching Popular Endpoints
    Cache:
    random quote
    top characters

    19. Background Stats Calculation
    Recalculate:
    most quoted character
    most quoted episode

    20. Versioned API (v2)

    Example change:

    return full actor info in character response

    Feature → Kubernetes Mapping
    Feature K8s Skill
    Health checks Liveness / readiness probes
    Stats jobs CronJobs
    Background tasks Workers
    Caching Redis pod
    API versioning Canary deployments
```
