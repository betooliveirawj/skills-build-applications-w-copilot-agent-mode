from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient, ASCENDING

# Sample superhero data
test_users = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]
test_teams = [
    {"name": "Marvel", "members": ["ironman@marvel.com", "cap@marvel.com", "widow@marvel.com"]},
    {"name": "DC", "members": ["superman@dc.com", "batman@dc.com", "wonderwoman@dc.com"]},
]
test_activities = [
    {"user_email": "superman@dc.com", "activity": "Flight", "duration": 60},
    {"user_email": "ironman@marvel.com", "activity": "Suit Training", "duration": 45},
]
test_leaderboard = [
    {"team": "Marvel", "points": 150},
    {"team": "DC", "points": 120},
]
test_workouts = [
    {"name": "Strength", "description": "General strength workout"},
    {"name": "Agility", "description": "Agility and speed drills"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert test data
        db.users.insert_many(test_users)
        db.teams.insert_many(test_teams)
        db.activities.insert_many(test_activities)
        db.leaderboard.insert_many(test_leaderboard)
        db.workouts.insert_many(test_workouts)

        # Ensure unique index on email
        db.users.create_index([("email", ASCENDING)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
