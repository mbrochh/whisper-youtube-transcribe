# Slides branch

This branch contains the slides for the talk that I gave on 2023-05-05 at
the library@harbourfront.

## Running the slides

* clone this repo 
* `git checkout slides`
* `cd slidev`
* run `npm install`
* run `npm run dev`
* browse to `http://localhost:3030/`

## Building the slides

* `git checkout slides`
* `cd slidev`
* run `npm run build`
* `rm -rf ../docs`
* run `mv dist ../docs`
* commit and push