#!/usr/bin/env bash

if [[ ! -d csv-converter ]]; then
    git clone https://github.com/jaredyam/csv-converter.git &&
        mv csv-converter/csv_converter ./ &&
        rm -rf csv-converter
fi
