# Read Me please

## Follow & Feed

### Follow user
POST /api/accounts/follow/<user_id>/  (Auth required)
- Follows the specified user.

### Unfollow user
POST /api/accounts/unfollow/<user_id>/  (Auth required)
- Unfollows the specified user.

### Get feed
GET /api/feed/  (Auth required)
- Returns paginated posts from users the authenticated user follows.
- Supports search (?search=term) and ordering (?ordering=-created_at).
