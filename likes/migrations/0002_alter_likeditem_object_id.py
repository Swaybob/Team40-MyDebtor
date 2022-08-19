

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeditem',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeditem',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]

