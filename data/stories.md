## perfect path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt{"duration": "1"}
  - slot{"duration": "2"}
  - action_record_study
* goodbye
  - utter_goodbye

## not so perfect path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt{"duration": "11"}
  - slot{"duration": null}
  - utter_ask_duration
* study_attempt{"duration": "4"}
  - slot{"duration": null}
  - action_record_study
* goodbye
  - utter_goodbye

## ask duration path
* greet
  - utter_greet
  - action_check_past
  - utter_go_study_once
* study_attempt
  - utter_ask_duration
* inform{"duration": "2"}
  - slot{"duration": "2"}
  - action_record_study
* goodbye
  - utter_goodbye




<!-- ## study happy path not studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_not_study
  - utter_go_study_once
* study_attempt
  - study_form
  - form{"name": "study_form"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## study happy path studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_study
  - utter_go_study_once
* study_attempt
  - study_form
  - form{"name": "study_form"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## study unhappy path not studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_not_study
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

## study unhappy path studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_study
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

## study very unhappy path not studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_not_study
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

## study very unhappy path studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_study
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
* ask_identity
  - utter_iamabot
  - study_form
  - form{"name": null}
* goodbye
  - utter_goodbye

## stop but continue path not studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_not_study
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

## stop but continue path studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_study
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

## stop and confirm path not studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_not_study
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

## stop and confirm path studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_study
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

## chat stop but continue path not studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_not_study
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

## chat stop but continue path studied
* greet
  - utter_greet
  - action_fetch_past
  - utter_did_study
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
  - utter_affirmbot -->

