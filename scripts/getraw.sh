#!/usr/bin/env bash

COMPET=tabular-playground-series-sep-2021
DATADIR=./data/raw
mkdir -p "$DATADIR"
kaggle competitions download -c "$COMPET" -p "$DATADIR"
unzip -n "$DATADIR/$COMPET.zip" -d "$DATADIR"
