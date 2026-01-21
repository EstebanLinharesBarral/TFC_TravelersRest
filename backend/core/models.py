from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator


# Create your models here.

class User(User):
    image = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "Users"

class Campaing(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    class System(models.TextChoices):
        CINCOE = '5E', '5e'
        ONEDND = 'ONE', 'OneDnD'
        CTHULHU = 'CALL', 'Call of Cthulhu'
        PATHFINDER = 'PATH', 'Pathfinder'
    system = models.CharField(choices=System.choices, default=System.CINCOE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Relationship data
    users = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = "Campaings"

    def __str__(self):
        return self.title
    
class Session(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    #Relationship data
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sessions"

class Character(models.Model):
    name = models.CharField(max_length=25)
    race = models.CharField(max_length=25)
    background = models.CharField(max_length=25)
    image = models.CharField(max_length=200, blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    class Moral(models.TextChoices):
        LAWFUL = 'LAWFUL', 'Lawful'
        NEUTRAL = 'NEUTRAL', 'Neutral'
        CHAOTIC = 'CHAOTIC', 'Chaotic'
    moral = models.CharField(choices=Moral.choices, default=Moral.NEUTRAL)
    class Goodness(models.TextChoices):
        GOOD = 'GOOD', 'Good'
        NEUTRAL = 'NEUTRAL', 'Neutral'
        BAD = 'BAD', 'Bad'
    goodness = models.CharField(choices=Goodness.choices, default=Goodness.NEUTRAL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Relationship data
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Characters"

    def __str__(self):
        return self.name
    
class CharSheet(models.Model):
    strength = models.IntegerField(blank=True, default=8)
    dexterity = models.IntegerField(blank=True, default=8)
    constitution = models.IntegerField(blank=True, default=8)
    inteligence = models.IntegerField(blank=True, default=8)
    wisdom = models.IntegerField(blank=True, default=8)
    charisma = models.IntegerField(blank=True, default=8)
    level = models.IntegerField(blank=True, default=1)
    feats = models.TextField(blank=True, null=True)
    inventory = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    pg = models.IntegerField(blank=True, default=0)
    pg_e1 = models.IntegerField(blank=True, null=True)
    pg_e2 = models.IntegerField(blank=True, null=True)
    proficency = models.IntegerField(blank=True, default=0)
    speed = models.IntegerField(blank=True, default=30)
    atc_bonus = models.IntegerField(blank=True, default=1)
    inspiration = models.BooleanField(default=False)
    others_ca = models.IntegerField(blank=True, default=0)
    others_iniciative = models.IntegerField(blank=True, default=0)
    class ClassDnd(models.TextChoices):
        BARBARIAN = 'BARB', 'Barbarian'
        BARD = 'BARD', 'Bard'
        WARLOCK = 'WARL', 'Warlock'
        CLERIC = 'CLER', 'Cleric'
        DRUID = 'DRUID', 'Druid'
        RANGER = 'RANG', 'Ranger'
        WARRIOR = 'WARR', 'Warrior'
        SPELLCASTER = 'SPEL', 'Spellcaster'
        MAGE = 'MAGE', 'Mage'
        PALADIN = 'PAL', 'Paladin'
        MONK = 'MONK', 'Monk'
        ROGUE = 'ROG', 'Rogue'
    classdnd = models.CharField(choices=ClassDnd.choices, default=ClassDnd.WARRIOR)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Relationship data
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "CharSheets"

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    bonus = models.CharField(max_length=50)
    extra = models.TextField(blank=True, null=True)
    class Damage(models.TextChoices):
        SLASH = 'SLASH', 'Slashing'
        BLUDGE = 'BLUDGE', 'Bludgedning'
        PIERCE = 'PIERCE', 'Piercing'
    damage = models.CharField(choices=Damage.choices, default=Damage.SLASH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Relationship data
    charSheet = models.ForeignKey(CharSheet, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Weapons"

    def __str__(self):
        return self.name

class Armor(models.Model):
    name = models.CharField(max_length=50)
    ca = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    extra = models.TextField(blank=True, null=True)
    class Type(models.TextChoices):
        LIGHT = 'LIGHT', 'Light'
        MEDIUM = 'MEDIUM', 'Medium'
        HEAVY = 'HEAVY', 'Heavy'
        SHIELD = 'SHIELD', 'Shield'
    type = models.CharField(choices=Type.choices, default=Type.LIGHT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Relationship data
    charSheet = models.ForeignKey(CharSheet, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Armors"

    def __str__(self):
        return self.name
    
#RELATIONSHIPS BETWEEN MODELS
