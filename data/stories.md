## happy path
* greet
  - action_get_name
* mood_great
  - utter_happy

## sad path 1
* greet
  - action_hello_world
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2

* greet
  - action_hello_world
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye

* goodbye
  - utter_goodbye

## bot challenge

* bot_challenge
  - utter_iamabot

## New Story

* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
    - utter_happy
* goodbye
    - utter_goodbye

## New Story

* greet
    - action_get_name

## New Story

* deny
    - action_get_name
    - action_hello_world
* unclear
    - action_hello_world
* name
    - action_hello_world
