# Generated by Django 4.1.5 on 2023-02-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')),
                ('attempt_status', models.CharField(max_length=20, verbose_name='Статус попытки')),
                ('answer', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, verbose_name='Контактный email')),
                ('name', models.CharField(max_length=250, verbose_name='ФИО')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Тема сообщения')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Sending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.TimeField(verbose_name='Время рассылки')),
                ('period', models.CharField(choices=[('per day', 'раз в день'), ('per week', 'раз в неделю'), ('per month', 'раз в месяц')], default='per month', max_length=20, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('completed', 'завершена'), ('created', 'создана'), ('launched', 'запущена')], default='completed', max_length=20, verbose_name='Статус')),
            ],
        ),
    ]
