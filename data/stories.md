## happy path
  - utter_start
* greet
  - action_hello_world
* mood_great
  - utter_happy

## sad path 1
  - utter_start
* greet
  - action_hello_world
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2

  - utter_start
* greet
  - action_hello_world
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
  - utter_start
* goodbye
  - utter_goodbye

## bot challenge
  - utter_start
* bot_challenge
  - utter_iamabot

## New Story
  - utter_start
* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
    - utter_happy
* goodbye
    - utter_goodbye

## New Story
  - utter_start
* greet
    - action_hello_world
* unclear
    - action_default_fallback

## New Story
  - utter_start
* greet
    - action_hello_world
* deny
    - utter_goodbye
* unclear
    - action_default_fallback

## New Story
  - utter_start
* greet
    - action_hello_world
* mood_great
    - utter_happy
* unclear
    - action_default_fallback

## New Story
  - utter_start
* greet
    - action_hello_world
* unclear
    - utter_unclear
