from django.db import migrations


def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Address = apps.get_model("orm01", "address02")
    for addr in Address.objects.all():
        addr.name = f"{addr.my_name} {addr.my_addr}"
        addr.save()


class Migration(migrations.Migration):
    dependencies = [
        ("orm01", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]