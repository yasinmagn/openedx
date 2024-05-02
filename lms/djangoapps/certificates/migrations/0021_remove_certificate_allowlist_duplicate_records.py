# Generated by Django 2.2.19 on 2021-03-11 19:31

from django.db import migrations
from django.db.models import Count, Min


class Migration(migrations.Migration):
    """
    Delete all the duplicate records in the `CERTIFICATES_CERTIFICATEWHITELIST` table.
    """

    def remove_duplicate_entries(apps, schema_editor):
        CertificateWhitelist = apps.get_model('certificates', 'CertificateWhitelist')

        allowlist_duplicates = (
            CertificateWhitelist.objects.values("user_id", "course_id")
            .annotate(first_entry_id=Min("id"), num_entries=Count("id"))
            .filter(num_entries__gt=1)
        )

        # delete the duplicates, excluding the original allowlist entry for the user/course-run combo
        for duplicate in allowlist_duplicates:
            (
                CertificateWhitelist.objects
                .filter(user_id=duplicate["user_id"], course_id=duplicate["course_id"])
                .exclude(id=duplicate["first_entry_id"])
                .delete()
            )

    dependencies = [
        ('certificates', '0020_remove_existing_mgmt_cmd_args'),
    ]

    operations = [
        migrations.RunPython(remove_duplicate_entries, reverse_code=migrations.RunPython.noop)
    ]
