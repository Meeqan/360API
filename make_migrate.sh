#!/usr/bin/env bash

clear

. ./.env

if [ -f ./.env ]
then
    if test -n "$DJANGO_PROJECT"
    then

        if [ -d $DJANGO_PROJECT ]; then

            echo '---------- Generating migrations ----------'
            cd $DJANGO_PROJECT && python manage.py makemigrations
        else
            echo '\n\n'
            echo "--> The directory you specified doesn't exit"
            echo '\n\n'


        fi

    else
        echo '\n\n'
        echo "--> Please set the value of DJANGO_PROJECT to the root dir of you django project:"
        echo "--> Example: DJANGO_PROJECT='root_dir_of_django_project'"
        echo '\n\n'

    fi
else
    echo '\n\n'
    echo '--> Please create a ".env" file and add the following'
    echo "--> Example: DJANGO_PROJECT='root_dir_of_django_project'"
    echo '\n\n'

fi




