## happy path
* get_started
  - action_get_name
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* get_started
  - action_get_name
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2

* get_started
  - action_get_name
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye

* get_started
  - action_get_name
* greet
  - utter_greet
* goodbye
  - utter_goodbye

## bot challenge

* get_started
  - action_get_name
* greet
  - utter_greet
* bot_challenge
  - utter_iamabot

## New Story

* get_started
  - action_get_name
* greet
  - utter_greet
* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
    - utter_happy
* goodbye
    - utter_goodbye

## New Story

* get_started
  - action_get_name
* greet
  - utter_greet
