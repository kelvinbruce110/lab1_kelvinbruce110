#!/bin/bash
#!/bin/bash

if [ ! -d "archive" ]
then
    mkdir archive
fi

timestamp=$(date +"%Y%m%d-%H%M%S")

new_name="grades_$timestamp.csv"

mv grades.csv archive/$new_name

touch grades.csv

echo "$timestamp : grades.csv archived as $new_name" >> organizer.log
