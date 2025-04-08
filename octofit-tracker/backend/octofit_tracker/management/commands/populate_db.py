from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))
        self.stdout.write(self.style.SUCCESS(f'Users before population: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Teams before population: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities before population: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries before population: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts before population: {Workout.objects.count()}'))

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Existing data cleared.'))

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='password123'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='password123'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='password123'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@mhigh.edu', password='password123'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2], users[3], users[4])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=95),
            Leaderboard(_id=ObjectId(), user=users[3], score=85),
            Leaderboard(_id=ObjectId(), user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS(f'Users after population: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Teams after population: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities after population: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries after population: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts after population: {Workout.objects.count()}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
