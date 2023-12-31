# Generated by Django 3.2.23 on 2023-12-01 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vyaparapp', '0003_remove_purchasebilltransactionhistory_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_no', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField()),
                ('state_of_supply', models.CharField(blank=True, max_length=255, null=True)),
                ('paymenttype', models.CharField(blank=True, max_length=255, null=True)),
                ('cheque', models.CharField(blank=True, max_length=255, null=True)),
                ('upi', models.CharField(blank=True, max_length=255, null=True)),
                ('accountno', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('igst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('cgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('sgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('total_taxamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('adjustment', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('grandtotal', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('paidoff', models.IntegerField(blank=True, default=0, null=True)),
                ('totalbalance', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.party')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoiceTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(max_length=255)),
                ('done_by_name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('salesinvoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.salesinvoice')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('tax', models.CharField(blank=True, max_length=255, null=True)),
                ('totalamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.itemmodel')),
                ('salesinvoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.salesinvoice')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.staff_details')),
            ],
        ),
    ]
