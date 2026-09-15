# TODO List

0. Asyncs
1. Admin role
2. Status codes instead of objects returned
3. Annotation fix instead of dict, schemas
4. Error Handling ( Checks on successful returning/updating/creating information)
5. Safe Delete
6. Add season description(AI tools/Google search/Api Request)
7. Change URL ADDRESSES TO REST
8. Docker + Kubernetes
9. Migration to POSTGRESQL/MYSQL
10. Microservices(Authorisation + Logging)
11. Review episode schema

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
