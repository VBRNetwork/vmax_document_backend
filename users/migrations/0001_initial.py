# Generated by Django 3.1.5 on 2022-05-21 17:04

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(default='users/avatars/default.jpg', upload_to='users/avatars')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('partner_data_attribute_name', models.CharField(blank=True, max_length=255, null=True)),
                ('partner_name', models.CharField(blank=True, max_length=255, null=True)),
                ('partner_id', models.CharField(blank=True, max_length=255, null=True)),
                ('contract_id', models.CharField(blank=True, max_length=255, null=True)),
                ('contract_start_date', models.DateTimeField(blank=True, null=True)),
                ('contract_end_date', models.DateTimeField(blank=True, null=True)),
                ('total_sell_in_qty', models.IntegerField(blank=True, null=True)),
                ('drop_ship_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity_sold', models.IntegerField(blank=True, null=True)),
                ('partner_internal_transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('partner_requested_rebate_amount', models.FloatField(blank=True, null=True)),
                ('partner_comment', models.CharField(blank=True, max_length=255, null=True)),
                ('partner_product', models.CharField(blank=True, max_length=255, null=True)),
                ('is_store', models.CharField(choices=[('With Store', 'With Store'), ('No Store', 'No Store')], default='With Store', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AccountSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_type', models.CharField(blank=True, max_length=255, null=True)),
                ('sales_sheet_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sellin_sheet_name', models.CharField(blank=True, max_length=255, null=True)),
                ('inventory_sheet_name', models.CharField(blank=True, max_length=255, null=True)),
                ('transmission_method', models.CharField(blank=True, max_length=255, null=True)),
                ('handle_blank_rows', models.CharField(blank=True, max_length=10, null=True)),
                ('cleanup_sku', models.CharField(blank=True, max_length=10, null=True)),
                ('date_format', models.CharField(blank=True, default='%m/%d/%Y', max_length=255, null=True)),
                ('sku_column', models.CharField(blank=True, max_length=8, null=True)),
                ('transaction_date_column', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity_column', models.CharField(blank=True, max_length=255, null=True)),
                ('total_column', models.CharField(blank=True, max_length=255, null=True)),
                ('company_sold_to_column', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Invoice To', 'Invoice To'), ('Bill To', 'Bill To'), ('Ship To', 'Ship To'), ('End User', 'End User')], default='Invoice To', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('sell_from_company_id', models.CharField(max_length=255)),
                ('sell_from_company_name', models.CharField(max_length=255)),
                ('sell_from_company_address_1', models.CharField(max_length=255)),
                ('sell_from_company_address_2', models.CharField(max_length=255)),
                ('sell_from_company_city', models.CharField(max_length=255)),
                ('sell_from_company_postal_code', models.CharField(max_length=255)),
                ('sell_from_company_country_code', models.CharField(max_length=255)),
                ('sold_to_company_id', models.CharField(max_length=255)),
                ('sold_to_company_tax_id', models.CharField(max_length=255)),
                ('sold_to_company_name', models.CharField(max_length=255)),
                ('sold_to_company_address_1', models.CharField(max_length=255)),
                ('sold_to_company_address_2', models.CharField(max_length=255)),
                ('sold_to_company_city', models.CharField(max_length=255)),
                ('sold_to_company_postal_code', models.CharField(max_length=255)),
                ('sold_to_company_country_code', models.CharField(max_length=255)),
                ('sold_to_company_state_code', models.CharField(max_length=255)),
                ('sold_to_company_asian_address', models.CharField(max_length=255)),
                ('ship_to_company_id', models.CharField(max_length=255)),
                ('ship_to_company_tax_id', models.CharField(max_length=255)),
                ('ship_to_company_name', models.CharField(max_length=255)),
                ('ship_to_company_address_1', models.CharField(max_length=255)),
                ('ship_to_company_address_2', models.CharField(max_length=255)),
                ('ship_to_company_city', models.CharField(max_length=255)),
                ('ship_to_company_postal_code', models.CharField(max_length=255)),
                ('ship_to_company_country_code', models.CharField(max_length=255)),
                ('ship_to_company_state_code', models.CharField(max_length=255)),
                ('ship_to_company_asian_address', models.CharField(max_length=255)),
                ('end_user_company_id', models.CharField(max_length=255)),
                ('end_user_company_tax_id', models.CharField(max_length=255)),
                ('end_user_company_name', models.CharField(max_length=255)),
                ('end_user_company_address_1', models.CharField(max_length=255)),
                ('end_user_company_address_2', models.CharField(max_length=255)),
                ('end_user_company_city', models.CharField(max_length=255)),
                ('end_user_company_postal_code', models.CharField(max_length=255)),
                ('end_user_company_country_code', models.CharField(max_length=255)),
                ('end_user_company_state_code', models.CharField(max_length=255)),
                ('end_user_company_asian_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_description', models.CharField(max_length=255)),
                ('partner_purchase_price', models.FloatField()),
                ('partner_purchase_price_currency_code', models.CharField(max_length=255)),
                ('transaction_date', models.DateTimeField()),
                ('channel_partner_customer_invoice_id', models.CharField(max_length=255)),
                ('partner_sell_price', models.FloatField()),
                ('partner_sell_price_currency_code', models.CharField(max_length=255)),
                ('hp_serial_number', models.CharField(max_length=255)),
                ('partner_product_reference', models.CharField(max_length=255)),
                ('reserved_custom_field_1', models.CharField(max_length=255)),
                ('reserved_custom_field_2', models.CharField(max_length=255)),
                ('is_asian_address', models.BooleanField(default=False)),
                ('customer_online_order_date', models.DateTimeField()),
                ('on_hand_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deal_bundle_id_1', models.CharField(max_length=255)),
                ('deal_bundle_id_2', models.CharField(max_length=255)),
                ('deal_bundle_id_3', models.CharField(max_length=255)),
                ('deal_bundle_id_4', models.CharField(max_length=255)),
                ('deal_bundle_id_5', models.CharField(max_length=255)),
                ('deal_bundle_id_6', models.CharField(max_length=255)),
                ('deal_promo_id_1', models.CharField(max_length=255)),
                ('deal_promo_id_2', models.CharField(max_length=255)),
                ('deal_promo_id_3', models.CharField(max_length=255)),
                ('deal_promo_id_4', models.CharField(max_length=255)),
                ('deal_promo_id_5', models.CharField(max_length=255)),
                ('deal_promo_id_6', models.CharField(max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='users.accounts')),
            ],
        ),
        migrations.AddField(
            model_name='accounts',
            name='partner_products',
            field=models.ManyToManyField(related_name='accounts', to='users.Products'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='settings',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='users.accountsettings'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['username'], name='users_user_usernam_65d164_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['id'], name='users_user_id_1cecd0_idx'),
        ),
    ]