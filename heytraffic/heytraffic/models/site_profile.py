from django.db import models
from django.contrib.sites.models import Site


class SiteProfileManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related(
            'site',
        )


class SiteProfile(models.Model):

    site = models.OneToOneField(
        Site,
        primary_key=True,
    )

    # Client Section
    client_count = models.PositiveIntegerField(
        verbose_name='고객 숫자',
        blank=True,
        null=True,
        help_text="",
    )
    social_account_count = models.PositiveIntegerField(
        verbose_name='소셜 계정 숫자',
        blank=True,
        null=True,
        help_text="",
    )
    social_activity_count = models.PositiveIntegerField(
        verbose_name='소셜 활동 숫자',
        blank=True,
        null=True,
        help_text="",
    )

    objects = SiteProfileManager()

    class Meta:
        default_related_name = 'site_profile'

    def __str__(self):
        return self.site.__str__()
