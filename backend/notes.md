# TODO List

0. Asyncs
1. Review delete cruds/routers(fix one return object another different https)
2. Make use of UUID
3. Admin role
4. Status codes instead of objects returned
5. Annotation fix instead of dict, schemas
6. Error Handling ( Checks on successful returning/updating/creating information)
7. Safe Delete
8. Pagination
9. Add season description(AI tools/Google search/Api Request)
10. Change URL ADDRESSES TO REST
11. Docker + Kubernetes
12. Migration to POSTGRESQL/MYSQL
13. Microservices(Authorisation + Logging)
14. Review episode schema
15.

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
