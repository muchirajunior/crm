# Generated by Django 5.0.6 on 2024-07-07 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business_partners', '0002_alter_businesspartner_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stage', models.CharField(choices=[('qualification', 'Qualification'), ('proposal', 'Proposal'), ('negotiation', 'Negotiation'), ('closed_won', 'Closed Won'), ('closed_lost', 'Closed Lost')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('sales_person', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_partners.businesspartner')),
            ],
        ),
    ]
