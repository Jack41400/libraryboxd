#imports for django functions and models
from django.conf import settings
from django.db import models
from django.utils import timezone

# User profile features -
class UserProfile(models.Model):
    """
    Extension of Django's built-in User model for libraryboxd-specific data.
    """
    # User var = one to one with django built in user model, cascade delete, related name is profile
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    # Phase 2+ candidate: allow private profiles
    is_private = models.BooleanField(
        default=False,
        help_text="If enabled, this user's profile and activity may be limited in visibility."
    )

    # Phase 2+ candidate: user’s 'top 3' or favorite books
    # For now just a ManyToMany placeholder; order can be handled later via through-model.
    favorite_books = models.ManyToManyField(
        'Book',
        blank=True,
        related_name='fans',
        help_text="Optional set of favorite books for this user."
    )

    # Basic audit fields
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for {self.user.username}"

class Book(models.Model):
    """
    Core catalog entry for a book in the private library.
    """
    title = models.CharField(max_length=255)
    # Keeping it simple: plain text author name(s) for Phase 1
    author = models.CharField(max_length=255, blank=True)

    # Optional metadata
    publication_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Year the book was first published (optional)."
    )
    isbn = models.CharField(
        max_length=20,
        blank=True,
        help_text="ISBN-10 or ISBN-13 (optional, not strictly validated)."
    )
    description = models.TextField(
        blank=True,
        help_text="Optional description / blurb."
    )
    cover_image_url = models.URLField(
        blank=True,
        help_text="Optional URL to a cover image."
    )

    # Library-specific fields for internal catalog use (optional)
    library_code = models.CharField(
        max_length=100,
        blank=True,
        help_text="Internal library identifier or call number (optional)."
    )

    # Audit fields
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title', 'author']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
        ]
        # You can enforce uniqueness loosely if you want; leaving it open for now:
        # unique_together = ('title', 'author', 'publication_year')

    def __str__(self):
        # Helpful representation in admin and elsewhere
        if self.author:
            return f"{self.title} — {self.author}"
        return self.title

class ReadingEntry(models.Model):
    """
    A user's reading log entry for a specific book.
    Multiple entries per (user, book) allowed to support re-reads.
    """
    class Rating(models.IntegerChoices):
        ONE = 1, "★☆☆☆☆"
        TWO = 2, "★★☆☆☆"
        THREE = 3, "★★★☆☆"
        FOUR = 4, "★★★★☆"
        FIVE = 5, "★★★★★"

    class Visibility(models.TextChoices):
        PUBLIC = 'public', 'Public'
        PRIVATE = 'private', 'Private'
        # Future: 'friends', 'unlisted', etc.

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reading_entries'
    )
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        related_name='reading_entries'
    )

    # When the user read/finished the book
    date_read = models.DateField(
        blank=True,
        null=True,
        help_text="Optional date when the book was read/finished."
    )

    rating = models.PositiveSmallIntegerField(
        choices=Rating.choices,
        blank=True,
        null=True,
        help_text="1–5 stars; optional if user doesn't want to rate."
    )

    review = models.TextField(
        blank=True,
        help_text="Optional review or comments about the book."
    )

    # Phase 2+ candidate: privacy per entry
    visibility = models.CharField(
        max_length=20,
        choices=Visibility.choices,
        default=Visibility.PUBLIC,
        help_text="Visibility of this entry (future feature; currently all treated as internal)."
    )

    # Structure for lightweight diary/history and auditability
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
        help_text="When this entry was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="When this entry was last updated."
    )

    # Optional simple 'is_active' for soft moderation
    is_active = models.BooleanField(
        default=True,
        help_text="Admins can deactivate entries instead of deleting (optional moderation tool)."
    )

    class Meta:
        ordering = ['-date_read', '-created_at']
        indexes = [
            models.Index(fields=['user', 'book']),
            models.Index(fields=['book']),
            models.Index(fields=['user']),
        ]
        # Note: multiple entries per user/book allowed intentionally
        # If later you want only one entry per (user, book, date_read), you can add a UniqueConstraint.

    def __str__(self):
        base = f"{self.user.username} – {self.book.title}"
        if self.date_read:
            return f"{base} on {self.date_read}"
        return base