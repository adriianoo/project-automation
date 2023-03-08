#!/bin/bash

function create() {
    
    python create.py
    cd ~/repos
    mkdir new-repository
    cd new-repository
}
create