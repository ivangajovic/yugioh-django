# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 06:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_title', models.CharField(max_length=300)),
                ('c_set', models.CharField(max_length=300)),
                ('c_edition', models.CharField(max_length=50)),
                ('c_image', models.FileField(upload_to='')),
                ('c_description', models.TextField()),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('procure_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-procure_date',),
                'permissions': (('can_view_ctrls', 'Can View CTRLS'),),
            },
        ),
        migrations.CreateModel(
            name='CardRarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('common', 'Common'), ('short print', 'Short Print'), ('rare', 'Rare'), ('super rare', 'Super Rare'), ('ultra rare', 'Ultra Rare'), ('secret rare', 'Secret Rare'), ('ultimate rare', 'Ultimate Rare'), ('ghost rare', 'Ghost Rare'), ('platinum rare', 'Platinum Rare'), ('prismatic secret rare', 'Prismatic Secret Rare'), ('extra secret rare', 'Extra Secret Rare'), ('platinum secret rare', 'Platinum Secret Rare'), ('normal parallel rare', 'Normal Parallel Rare'), ('super parallel rare', 'Super Parallel Rare'), ('ultra parallel rare', 'Ultra Parallel Rare'), ('starfoil rare', 'Starfoil Rare'), ('mosaic rare', 'Mosaic Rare'), ('shatterfoil rare', 'Shatterfoil Rare'), ('gold rare', 'Gold Rare'), ('gold secret rare', 'gold secret Rare'), ('ghost/gold rare', 'Ghost/Gold Rare')], help_text='Select rarity of the card', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('monster', 'Monster'), ('spell', 'Spell'), ('trap', 'Trap')], help_text='Enter card type', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonsterAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('flip', 'Flip'), ('toon', 'Toon'), ('spirit', 'Spirit'), ('union', 'Union'), ('gemini', 'Gemini')], help_text='If aplicable, choose monster ability', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonsterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('aqua', 'Aqua'), ('beast', 'Beast'), ('beast-warrior', 'Beast-Warrior'), ('cyberse', 'Cyberse'), ('dinosaur', 'Dinosaur'), ('divine-beast', 'Divine-Beast'), ('dragon', 'Dragon'), ('fairy', 'Fairy'), ('fiend', 'Fiend'), ('fish', 'Fish'), ('insect', 'Insect'), ('machine', 'Machine'), ('plant', 'Plant'), ('psychic', 'Psychic'), ('pyro', 'Pyro'), ('reptile', 'Reptile'), ('rock', 'Rock'), ('sea-serpent', 'Sea-Serpent'), ('spellcaster', 'Spellcaster'), ('thunder', 'Thunder'), ('warrior', 'Warrior'), ('winged-beast', 'Winged-Beast'), ('wyrm', 'Wyrm'), ('zombie', 'Zombie')], help_text='If monster card, choose monster type', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonsterType1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('normal', 'Normal'), ('effect', 'Effect')], help_text='If monster card, choose card subtype', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonsterType2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('ritual', 'Ritual'), ('fusion', 'Fusion'), ('synchro', 'Synchro'), ('xyz', 'Xyz'), ('pendulum', 'Pendulum'), ('link', 'Link'), ('token', 'Token')], help_text='If monster card, choose card subtype', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpellTrapType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('normal', 'Normal'), ('continuous', 'Continuous'), ('field', 'Field'), ('equip', 'Equip'), ('quick-play', 'Quick-Play'), ('ritual', 'Ritual'), ('counter', 'Counter')], help_text='If spell or trap card, choose card subtype', max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='card_rarity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_rarity', to='ygocard.CardRarity'),
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_type', to='ygocard.CardType'),
        ),
        migrations.AddField(
            model_name='card',
            name='monster_ability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster_ability', to='ygocard.MonsterAbility'),
        ),
        migrations.AddField(
            model_name='card',
            name='monster_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster_type', to='ygocard.MonsterType'),
        ),
        migrations.AddField(
            model_name='card',
            name='monster_type_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster_type_1', to='ygocard.MonsterType1'),
        ),
        migrations.AddField(
            model_name='card',
            name='monster_type_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster_type_2', to='ygocard.MonsterType2'),
        ),
        migrations.AddField(
            model_name='card',
            name='spell_trap_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell_trap_type', to='ygocard.SpellTrapType'),
        ),
    ]
