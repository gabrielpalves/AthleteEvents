from django.http import JsonResponse
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import sqlite3
import csv

@api_view(['GET', 'POST', 'REMOVE_ALL', 'FILL'])
def events_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse({'events': serializer.data})
    
    if request.method == 'POST':
        if not cant_repeat(request.data):
            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Message": "Data is already in the database"}, status=status.HTTP_208_ALREADY_REPORTED)
    
    if request.method == 'REMOVE_ALL':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()

        sql = 'DELETE FROM olympics_event'
        cur = con.cursor()
        cur.execute(sql)

        con.commit()
        con.close()
        return Response({'Message': 'Removed all data from the database'}, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'FILL':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()

        cur.execute("create table if not exists olympics_event (id integer, event_key integer, Name text, Sex text, Age integer, Height integer, Weight integer,\
        Team text, NOC text, Games text, Year integer, Season text, City text, Sport text, Event text, Medal text)")

        cur.execute("SELECT id FROM olympics_event")
        ids = cur.fetchall()
        try:
            last_id = ids[-1]
        except:
            last_id = (0,)

        a_file = open("athlete_events.csv")
        rows = csv.reader(a_file)

        # gotta add the "id" to the table to insert in the database
        count = int(last_id[0])+1
        first = True
        rows2insert = []
        for row in rows:
            if first:
                first = False
                continue
            row.insert(0,count)
            count += 1
            rows2insert.append(tuple(row))
        cur.executemany("INSERT INTO olympics_event VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows2insert)

        con.commit()
        con.close()
        return Response({"Message": "Database filled with athlete_events.csv"}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, id):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if not cant_repeat(request.data):
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message": "Data is already in the database"}, status=status.HTTP_208_ALREADY_REPORTED)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def cant_repeat(data):
    
    data_tuple = (data['Name'],
    data['Sex'],
    data['Age'],
    data['Height'],
    data['Weight'],
    data['Team'],
    data['NOC'],
    data['Games'],
    data['Year'],
    data['Season'],
    data['City'],
    data['Sport'],
    data['Event'],
    data['Medal'])

    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    cur.execute("SELECT Name, Sex, Age, Height, Weight, Team, NOC, Games, Year, Season, City, Sport, Event, Medal FROM olympics_event")
    count = 0
    for row in cur.fetchall():
        if row == data_tuple:
            con.close()
            return True
    con.close()
    return False