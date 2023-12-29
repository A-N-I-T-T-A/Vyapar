# Generated by Django 3.2.23 on 2023-12-19 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0018_additionalloan_loanaccounts_loanhistory_makepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_item',
            name='taxamount',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.party'),
        ),
    ]
