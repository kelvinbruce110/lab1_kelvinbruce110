#!/bin/bash

if [ ! -d "archive" ]
then
    mkdir archive
fi

timestamp=$(date +"%Y%m%d-%H%M%S")

new_name="grades_$timestamp.csv"

if [ ! -f "grades.csv" ]
then
    echo "Error: grades.csv does not exist."
    exit 1
fi

mv grades.csv archive/$new_name

touch grades.csv

echo "$timestamp : grades.csv archived as $new_name" >> organizer.log
