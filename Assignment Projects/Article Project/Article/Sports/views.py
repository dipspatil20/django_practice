from django.shortcuts import render

# Create your views here.
cricket_data = [
    {
        'name': 'Virat Kohli',
        'country': 'India',
        'age': 37,
        'role': 'Batsman',
        'matches': 550
    },
    {
        'name': 'Rohit Sharma',
        'country': 'India',
        'age': 39,
        'role': 'Batsman',
        'matches': 480
    },
    {
        'name': 'Jasprit Bumrah',
        'country': 'India',
        'age': 32,
        'role': 'Bowler',
        'matches': 300
    },
    {
        'name': 'Babar Azam',
        'country': 'Pakistan',
        'age': 31,
        'role': 'Batsman',
        'matches': 350
    },
    {
        'name': 'Ben Stokes',
        'country': 'England',
        'age': 35,
        'role': 'All-rounder',
        'matches': 280
    }
]

chess_data = [
    {
        'name': 'Magnus Carlsen',
        'country': 'Norway',
        'age': 35,
        'title': 'Grandmaster',
        'rating': 2837
    },
    {
        'name': 'Hikaru Nakamura',
        'country': 'USA',
        'age': 38,
        'title': 'Grandmaster',
        'rating': 2816
    },
    {
        'name': 'Fabiano Caruana',
        'country': 'USA',
        'age': 34,
        'title': 'Grandmaster',
        'rating': 2773
    },
    {
        'name': 'D Gukesh',
        'country': 'India',
        'age': 20,
        'title': 'Grandmaster',
        'rating': 2750
    },
    {
        'name': 'Praggnanandhaa',
        'country': 'India',
        'age': 21,
        'title': 'Grandmaster',
        'rating': 2740
    }
]

hockey_data = [
    {
        'name': 'Harmanpreet Singh',
        'country': 'India',
        'age': 30,
        'position': 'Defender',
        'goals': 200
    },
    {
        'name': 'Manpreet Singh',
        'country': 'India',
        'age': 34,
        'position': 'Midfielder',
        'goals': 80
    },
    {
        'name': 'PR Sreejesh',
        'country': 'India',
        'age': 38,
        'position': 'Goalkeeper',
        'goals': 0
    },
    {
        'name': 'Arthur Van Doren',
        'country': 'Belgium',
        'age': 29,
        'position': 'Defender',
        'goals': 30
    },
    {
        'name': 'Tom Boon',
        'country': 'Belgium',
        'age': 34,
        'position': 'Forward',
        'goals': 150
    }
]

def cricket(request):
    return render(request, 'cricket.html',{'context':cricket_data})

def chess(request):
    return render(request,'chess.html', {'context':chess_data})

def hockey(request):
    return render(request,'hocky.html',{'context':hockey_data})

