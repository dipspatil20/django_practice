from django.shortcuts import render

# Create your views here.
disaster_data = [
    {
        'title': 'Floods in Assam',
        'date': 'June 2026',
        'location': 'Assam',
        'type': 'Flood'
    },
    {
        'title': 'Cyclone in Odisha',
        'date': 'May 2026',
        'location': 'Odisha',
        'type': 'Cyclone'
    },
    {
        'title': 'Earthquake in Northeast India',
        'date': 'April 2026',
        'location': 'Northeast India',
        'type': 'Earthquake'
    },
    {
        'title': 'Landslide in Himachal Pradesh',
        'date': 'July 2026',
        'location': 'Himachal Pradesh',
        'type': 'Landslide'
    },
    {
        'title': 'Heavy Rainfall in Kerala',
        'date': 'August 2026',
        'location': 'Kerala',
        'type': 'Heavy Rainfall'
    }
]


national_security_data = [
    {
        'title': 'Border Security Exercise',
        'date': 'June 2026',
        'location': 'Ladakh',
        'organization': 'Indian Army'
    },
    {
        'title': 'Naval Security Exercise',
        'date': 'May 2026',
        'location': 'Indian Ocean',
        'organization': 'Indian Navy'
    },
    {
        'title': 'Cyber Security Awareness Program',
        'date': 'April 2026',
        'location': 'New Delhi',
        'organization': 'CERT-In'
    },
    {
        'title': 'Coastal Security Exercise',
        'date': 'March 2026',
        'location': 'Mumbai',
        'organization': 'Indian Coast Guard'
    },
    {
        'title': 'Defence Technology Exercise',
        'date': 'February 2026',
        'location': 'New Delhi',
        'organization': 'DRDO'
    }
]


political_data = [
    {
        'title': 'Parliament Session',
        'date': 'July 2026',
        'location': 'New Delhi',
        'category': 'Parliament'
    },
    {
        'title': 'State Assembly Session',
        'date': 'June 2026',
        'location': 'Maharashtra',
        'category': 'State Politics'
    },
    {
        'title': 'Election Commission Meeting',
        'date': 'May 2026',
        'location': 'New Delhi',
        'category': 'Election'
    },
    {
        'title': 'New Government Scheme',
        'date': 'April 2026',
        'location': 'India',
        'category': 'Government Scheme'
    },
    {
        'title': 'Cabinet Meeting',
        'date': 'March 2026',
        'location': 'New Delhi',
        'category': 'Government'
    }
]

def disaster(request):
    return render(request, 'disasters.html',{'context':disaster_data})

def national(request):
    return render(request, 'national_sec.html',{'context':national_security_data})

def political(request):
    return render(request, 'political.html',{'context':political_data})

def current_affairs(request):
    return render(request, 'current_affairs.html')