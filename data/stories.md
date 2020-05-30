## happy path
* get_user_name
  - utter_start
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* get_user_name
  - utter_start
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2

* get_user_name
  - utter_start
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye

* get_user_name
  - utter_start
* greet
  - utter_greet
* goodbye
  - utter_goodbye

## bot challenge

* get_user_name
  - utter_start
* greet
  - utter_greet
* bot_challenge
  - utter_iamabot
