from django.shortcuts import render

# Create your views here.
bollywood_movies = [
    {
        'name': '3 Idiots',
        'dir': 'Rajkumar Hirani',
        'imdb': 8.4,
        'hero': 'Aamir Khan',
        'heroine': 'Kareena Kapoor'
    },
    {
        'name': 'Dangal',
        'dir': 'Nitesh Tiwari',
        'imdb': 8.3,
        'hero': 'Aamir Khan',
        'heroine': 'Fatima Sana Shaikh'
    },
    {
        'name': 'Chhichhore',
        'dir': 'Nitesh Tiwari',
        'imdb': 8.3,
        'hero': 'Sushant Singh Rajput',
        'heroine': 'Shraddha Kapoor'
    },
    {
        'name': 'Zindagi Na Milegi Dobara',
        'dir': 'Zoya Akhtar',
        'imdb': 8.2,
        'hero': 'Hrithik Roshan',
        'heroine': 'Katrina Kaif'
    },
    {
        'name': 'Barfi!',
        'dir': 'Anurag Basu',
        'imdb': 8.1,
        'hero': 'Ranbir Kapoor',
        'heroine': 'Priyanka Chopra'
    }
]

sandalwood_movies = [
    {
        'name': 'KGF: Chapter 1',
        'dir': 'Prashanth Neel',
        'imdb': 8.2,
        'hero': 'Yash',
        'heroine': 'Srinidhi Shetty'
    },
    {
        'name': 'Kantara',
        'dir': 'Rishab Shetty',
        'imdb': 8.5,
        'hero': 'Rishab Shetty',
        'heroine': 'Sapthami Gowda'
    },
    {
        'name': '777 Charlie',
        'dir': 'Kiranraj K',
        'imdb': 8.0,
        'hero': 'Rakshit Shetty',
        'heroine': 'Sangeetha Sringeri'
    },
    {
        'name': 'Kirik Party',
        'dir': 'Rishab Shetty',
        'imdb': 8.0,
        'hero': 'Rakshit Shetty',
        'heroine': 'Rashmika Mandanna'
    },
    {
        'name': 'Ugramm',
        'dir': 'Prashanth Neel',
        'imdb': 8.0,
        'hero': 'Sriimurali',
        'heroine': 'Hariprriya'
    }
]

mollywood_movies = [
    {
        'name': 'Drishyam',
        'dir': 'Jeethu Joseph',
        'imdb': 8.6,
        'hero': 'Mohanlal',
        'heroine': 'Meena'
    },
    {
        'name': 'Premam',
        'dir': 'Alphonse Puthren',
        'imdb': 8.3,
        'hero': 'Nivin Pauly',
        'heroine': 'Sai Pallavi'
    },
    {
        'name': 'Bangalore Days',
        'dir': 'Anjali Menon',
        'imdb': 8.3,
        'hero': 'Dulquer Salmaan',
        'heroine': 'Nazriya Nazim'
    },
    {
        'name': 'Kumbalangi Nights',
        'dir': 'Madhu C. Narayanan',
        'imdb': 8.5,
        'hero': 'Fahadh Faasil',
        'heroine': 'Anna Ben'
    },
    {
        'name': 'Lucifer',
        'dir': 'Prithviraj Sukumaran',
        'imdb': 7.5,
        'hero': 'Mohanlal',
        'heroine': 'Manju Warrier'
    }
]

def sandal(request):
    return render(request, 'sandalwood.html', {'context':sandalwood_movies})

def molly(request):
    return render(request, 'mollyhood.html',{'context':mollywood_movies})

def bolly(request):
    return render(request,'bollywood.html',{'context':bollywood_movies})
