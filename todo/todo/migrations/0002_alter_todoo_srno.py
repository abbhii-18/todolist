from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoo',
            name='srno',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
