# Phase 1

## Models
- [Book](#book)
- [Reading Entry](#reading-entry)
- [User Profile](#user-profile)

### Book
Core catalog entry (title + author required; everything else optional). Prepared for future metadata expansion (e.g., tags, external IDs).

Simple title and author plain text fields. ISBN-10 or ISBN-13 not strictly validated. Optional metadata and linking to hosted image url. Internal library call numbers.

### Reading Entry
A log entry for “user read book at time T, rated X, optional review”. Multiple entries per book per user are allowed (re-reads).

```Visibility``` class for future private accounts.

Additional ```Rating``` class for users to rate 1-5.

Optional date finished for accurate diary tracking.

```is_active```flag for easy admin / soft moderation.

*Note: multiple entries per book for single user allowed intentionally.*

### User Profile
Uses extension of django built-in ```AUTH_USER_MODEL``` profile in a ```Models.OneToOneField```. Cascade delete (```models.CASCADE```)

Includes ```is_private``` flag for users to hide their profiles from public view. Uses django ```models.BooleanField```.

Placeholder ```favorite_books``` with ```Models.ManyToManyField```. Order can be handled later via through model.