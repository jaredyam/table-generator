#!/usr/bin/env bash

if [ -d csv_converter ]; then
    echo "fatal: dependent package 'csv-converter' already exists"
else
    git clone https://github.com/jaredyam/csv-converter.git &&
        mv csv-converter/csv_converter ./ &&
        rm -rf csv-converter
fi
