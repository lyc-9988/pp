## study happy path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt
  - study_form
  - form{"name": "study_form"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## study unhappy path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt
  - study_form
  - form{"name": "study_form"}
* ask_identity
  - utter_iamabot
  - study_form
  - form{"name": null}
* goodbye
  - utter_goodbye

## study very unhappy path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt
  - study_form
  - form{"name": "study_form"}
* ask_identity
  - utter_iamabot
  - study_form
* bot_challenge
  - utter_affirmbot
  - study_form
* bot_challenge
  - utter_affirmbot
  - study_form
  - form{"name": null}
* goodbye
  - utter_goodbye


## stop but continue path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt
  - study_form
  - form{"name": "study_form"}
* not_study_attempt
  - utter_go_study_twice
  - utter_ask_stop
* deny
  - study_form
  - form{"name": null}
* goodbye
  - utter_goodbye


## stop and confirm path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt
  - study_form
  - form{"name": "study_form"}
* not_study_attempt
  - utter_go_study_twice
  - utter_ask_stop
* affirm
  - action_deactivate_form
  - form{"name": null}


## chat stop but continue path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt
  - study_form
  - form{"name": "study_form"}
* ask_identity
  - utter_iamabot
  - study_form
* not_study_attempt
  - utter_go_study_twice
  - utter_ask_stop
* deny
  - study_form
  - form{"name": null}
* goodbye
  - utter_goodbye


## bot challenge
* ask_identity
  - utter_iamabot
* bot_challenge
  - utter_affirmbot
