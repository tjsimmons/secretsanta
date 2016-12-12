from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Person, Match
import json
import random


# Create your views here.
def index(request):
    persons = Person.objects.all().order_by('name')
    return render(request, 'secretsanta/index.html', {'persons': persons})


def details(request):
    if request.method == 'POST':
        person_id = request.POST['person']

        # check for an existing match
        match = Match.objects.filter(gifter_id=person_id)

        if len(match) == 0:
            matched = [match.giftee_id for match in Match.objects.all()] + [person_id]
            people_remaining = Person.objects.exclude(id__in=matched)

            if len(people_remaining) != 0:
                matched_person = random.choice(people_remaining)
                secret_key = ''.join(random.choice('0123456789ACBDEF') for i in range(6))

                person = Person.objects.get(id=person_id)
                person.secret_key = secret_key

                person.save()

                match = Match.objects.create(gifter=person, giftee=matched_person)
                match.save()

                return render(request, 'secretsanta/details.html', {'match': match, 'can_rematch': True})
            else:
                return HttpResponse(404)
        else:  # check the incoming secret key
            secret_key = request.POST['secret_key']

            try:
                person = Person.objects.get(id=person_id, secret_key=secret_key)
            except ObjectDoesNotExist:
                person = None

            if person is None:
                messages.error(request, 'Incorrect secret key')
                return render(request, 'secretsanta/index.html', {'persons': Person.objects.all()})
            else:
                match = Match.objects.get(gifter=person)

            return render(request, 'secretsanta/details.html', {'match': match, 'can_rematch': False})
    else:
        return HttpResponse(404)

    return HttpResponse(404)


def rematch(request, match_id):
    match = Match.objects.get(id=match_id)
    gifter = Person.objects.get(id=match.gifter.id)
    gifter.secret_key = None

    match.delete()
    gifter.save()

    return redirect('/secretsanta')


def check_person(request, person_id):
    response_data = {'found': False}

    try:
        person = Person.objects.get(id=person_id)
    except ObjectDoesNotExist:
        person = None

    if person is not None:
        response_data['found'] = person.secret_key is not None and person.secret_key != ""

    return HttpResponse(json.dumps(response_data), content_type='application/json')
