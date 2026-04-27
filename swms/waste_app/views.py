from django.shortcuts import render
from .models import Bin
import math

def home(request):
    bins = Bin.objects.all()

    low = medium = full = 0

    for bin in bins:
        if bin.fill_level < 40:
            bin.status = "Low"
            bin.color = "green"
            low += 1
        elif bin.fill_level < 80:
            bin.status = "Medium"
            bin.color = "orange"
            medium += 1
        else:
            bin.status = "Full"
            bin.color = "red"
            full += 1

    context = {
        'bins': bins,
        'low': low,
        'medium': medium,
        'full': full
    }

    return render(request, 'home.html', context)


def find_route(start, bins):
    route = []
    current = start

    bins = bins.copy()

    while bins:
        nearest = min(
            bins,
            key=lambda b: math.sqrt((b.x - current[0])**2 + (b.y - current[1])**2)
        )
        route.append(nearest)
        current = (nearest.x, nearest.y)
        bins.remove(nearest)

    return route


def route_view(request):
    bins = Bin.objects.all()

    # Only full bins
    full_bins = [b for b in bins if b.fill_level > 70]

    start = (0, 0)
    end = (10, 10)

    route = find_route(start, full_bins)

    context = {
        'bins': bins,
        'route': route,
        'start_x': start[0],
        'start_y': start[1],
        'end_x': end[0],
        'end_y': end[1],
    }

    return render(request, 'route.html', context)