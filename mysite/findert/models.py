from django.db import models

# Create your models here.

class Player(models.Model) :
    Rank_choise = (
        ('Silver I', 'Silver I'),
        ('Silver II', 'Silver II'),
        ('Silver III', 'Silver III'),
        ('Silver IV', 'Silver IV'),
        ('Silver Elite', 'Silver Elite'),
        ('Silver Elite Master', 'Silver Elite Master'),
        ('Gold Nova I', 'Gold Nova I'),
        ('Gold Nova II', 'Gold Nova II'),
        ('Gold Nova III', 'Gold Nova III'),
        ('Gold Nova Master', 'Gold Nova Master'),
        ('Master Guardian I', 'Master Guardian I'),
        ('Master Guardian II', 'Master Guardian II'),
        ('Master Guardian Elite', 'Master Guardian Elite'),
        ('Distinguished Master Guardian', 'Distinguished Master Guardian'),
        ('Legendary Eagle', 'Legendary Eagle'),
        ('Legendary Eagle Master', 'Legendary Eagle Master'),
        ('Supreme Master First Class', 'Supreme Master First Class'),
        ('The Global Elite', 'The Global Elite'),
    )

    Skill_choise = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
    )

    Language_choise = (
        ('English', 'English'),
        ('Russian', 'Russian'),
        ('Ukrainian', 'Ukrainian'),
    )

    Goal_choise = (
        ('To have fun', 'To have fun'),
        ('To play competitively', 'To play competitively'),
        ('To become a pro', 'To become a pro'),
    )

    Region_choise = (
        ('EU East', 'EU East'),
        ('America', 'America'),
        ('CIS', 'CIS'),
    )

    Country_choise = (
        ('Ukraine', 'Ukraine'),
        ('Russia', 'Russia'),
        ('USA', 'USA'),
    )

    MainRole_choise = (
        ('Assault', 'Assault'),
        ('Sniper', 'Sniper'),
        ('Support', 'Support'),
    )

    TacticalRole_choise = (
        ('Captain', 'Captain'),
        ('Coach', 'Coach'),
        ('Strategist', 'Strategist'),
    )

    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    player_name = models.CharField(max_length=100)
    player_password = models.CharField(max_length=100)
    player_email = models.CharField(max_length=100)
    faceit_link = models.CharField(max_length=100)
    steam_link = models.CharField(max_length=100)
    player_country = models.CharField(max_length=100, choices=Country_choise)
    player_region = models.CharField(max_length=100, choices=Region_choise)
    player_goal = models.CharField(max_length=100, choices=Goal_choise)
    player_language = models.CharField(max_length=100, choices=Language_choise)
    player_skill = models.CharField(max_length=100, choices=Skill_choise)
    player_rank = models.CharField(max_length=100, choices=Rank_choise)
    player_mainrole = models.CharField(max_length=100, choices=MainRole_choise)
    player_tacticalrole = models.CharField(max_length=100, choices=TacticalRole_choise)

class Team(models.Model):

    Language_choise = (
        ('English', 'English'),
        ('Russian', 'Russian'),
        ('Ukrainian', 'Ukrainian'),
        ('Polish', 'Polish'),
        ('Swedish', 'Swedish'),
        ('German', 'German'),
        ('French', 'French'),
    )

    Goal_choise = (
        ('To have fun', 'To have fun'),
        ('To play competitively', 'To play competitively'),
        ('To become a pro', 'To become a pro'),
    )

    Region_choise = (
        ('EU East', 'EU East'),
        ('EU West', 'EU West'),
        ('EU South', 'EU South'),
        ('America', 'America'),
        ('CIS', 'CIS'),
        ('India', 'India'),
        ('Oceania', 'Oceania'),
    )

    Country_choise = (
        ('Ukraine', 'Ukraine'),
        ('Russia', 'Russia'),
        ('Germany', 'Germany'),
        ('USA', 'USA'),
        ('Sweden', 'Sweden'),
        ('Poland', 'Poland'),
        ('Spain', 'Spain'),
        ('Serbia', 'Serbia'),
        ('France', 'France'),
        ('Belarus', 'Belarus'),
    )

    team_name = models.CharField(max_length=100)
    team_goal = models.CharField(max_length=100, choices=Goal_choise)
    team_country = models.CharField(max_length=100, choices=Country_choise)
    team_language = models.CharField(max_length=100, choices=Language_choise)
    team_region = models.CharField(max_length=100, choices=Region_choise)