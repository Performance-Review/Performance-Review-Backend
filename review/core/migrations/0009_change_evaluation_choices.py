# Generated by Django 3.0 on 2020-01-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_personreview_final_submit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personreview',
            name='execution_rating',
            field=models.IntegerField(blank=True, choices=[(1, 'NEEDS_IMPROVEMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'SUPERB')], null=True),
        ),
        migrations.AlterField(
            model_name='personreview',
            name='leadership_rating',
            field=models.IntegerField(blank=True, choices=[(1, 'NEEDS_IMPROVEMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'SUPERB')], null=True),
        ),
        migrations.AlterField(
            model_name='personreview',
            name='presence_rating',
            field=models.IntegerField(blank=True, choices=[(1, 'NEEDS_IMPROVEMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'SUPERB')], null=True),
        ),
        migrations.AlterField(
            model_name='personreview',
            name='problem_solving_rating',
            field=models.IntegerField(blank=True, choices=[(1, 'NEEDS_IMPROVEMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'SUPERB')], null=True),
        ),
        migrations.AlterField(
            model_name='personreview',
            name='sahabiness_rating',
            field=models.IntegerField(blank=True, choices=[(1, 'NEEDS_IMPROVEMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'SUPERB')], null=True),
        ),
        migrations.AlterField(
            model_name='personreview',
            name='thought_leadership_rating',
            field=models.IntegerField(blank=True, choices=[(1, 'NEEDS_IMPROVEMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'SUPERB')], null=True),
        ),
        migrations.AlterField(
            model_name='projectcomment',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 'NEEDS_IMPROVEMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'SUPERB')], null=True),
        ),
        migrations.AlterField(
            model_name='projectreview',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 'NEEDS_IMPROVEMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'SUPERB')], null=True),
        ),
    ]