from .models import Player, Team, Match, Action
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Player)
def publish_player_created(sender, instance: Player, created: bool, **kwargs):
    if created:
        print(f"Player {instance.name} created!")

@receiver(post_save, sender=Team)
def publish_team_created(sender, instance: Team, created: bool, **kwargs):
    if created:
        print(f"Team {instance.name} created!")

@receiver(post_save, sender=Match)
def publish_match_created(sender, instance: Match, created: bool, **kwargs):
    if created:
        print("Match created!")

@receiver(post_save, sender=Match)
def publish_new_match_result(sender, instance: Match, created: bool, **kwargs):
    if not created:
        print("Match result updated!")

@receiver(post_save, sender=Action)
def publish_action_added(sender, instance: Action, created: bool, **kwargs):
    if created:
        print("Action added!")