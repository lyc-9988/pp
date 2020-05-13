from rasa_sdk import Action
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from typing import Text, List
import random
from datetime import datetime, timedelta
import os.path
import csv

dir_path = 'spreadsheet/'
file_path = 'spreadsheet/study_plans.csv'

# random.seed(1)


# class RandomLuckyNumber(Action):
#     def name(self):
#         return "action_lucky_number"

#     def run(self, dispatcher, tracker, domain):
#         return [SlotSet("lucky_number", random.randint(0, 1))]



class CheckYesterday(Action):
    def name(self):
        return "action_check_past"

    @staticmethod
    def find_plan(date) -> float:
        if not os.path.exists(dir_path):
            return -1
        else:
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['date'] == date:
                        return float(row['duration'])
                return 0

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any])
        # -> List[Dict[Text, Any]]

        yesterday = str(datetime.date(datetime.now() - timedelta(1)))

        study_hour=self.find_plan(yesterday)

        if study_hour > 0:
            message = 'You study time yesterday was: '\
            + str(study_hour) \
            + 'h. Great job! Keep going! :)'
        elif study_hour == 0:
            message = 'It seems like you didn\'t study yesterday. ' \
            + 'You may want to work harder( ^ω^)'
        else:
            message = 'Welcome. Nice to meet you.'

        dispatcher.utter_message(message)
        return []

# class RecordStudy(Action):
#     def name(self):
#         return "action_record_study"
#
#     @staticmethod
#     def check_plan(date):
#         if not os.path.exists(dir_path):
#             return False
#         else:
#             with open(file_path, 'r') as f:
#                 reader = csv.DictReader(f)
#                 for row in reader:
#                     if row['date'] == date:
#                         return True
#         return False
#
#     @staticmethod
#     def save_plan(duration):
#         if not os.path.exists(dir_path):
#             os.makedirs(dir_path)
#             with open(file_path, 'a') as f:
#                 attributes = ['date', 'duration']
#                 writer = csv.DictWriter(f, fieldnames=attributes)
#
#                 curr_date = str(datetime.date(datetime.now()))
#                 writer.writeheader()
#                 writer.writerow({'date' : curr_date, 'duration' : str(duration)})
#                 # save success
#                 return 1
#         else:
#             with open(file_path, 'a') as f:
#                 attributes = ['date', 'duration']
#                 writer = csv.DictWriter(f, fieldnames=attributes)
#                 curr_date = str(datetime.date(datetime.now()))
#
#                 if not RecordStudy.check_plan(curr_date):
#                     writer.writerow({'date' : curr_date, 'duration' : str(duration)})
#                     return 1
#                 else:
#                     # repeated date
#                     return -1
#
#     def run(self, dispatcher, tracker, domain):
#         # type: (CollectingDispatcher, Tracker, Dict[Text, Any])
#         # -> List[Dict[Text, Any]]
#
#         duration = tracker.get_slot('duration')
#         if self.save_plan(duration) == 1:
#             message = 'study duration: ' + str(duration)
#         else:
#             message = 'You have already made a plan today. Please come tomorrow.'
#         dispatcher.utter_message(message)

class StudyForm(FormAction):
    def name(self):
        return "study_form"

    @staticmethod
    def required_slots(tracker):
        return ["subject", "duration"]

    @staticmethod
    def check_plan(date):
        if not os.path.exists(dir_path):
            return False
        else:
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['date'] == date:
                        return True
        return False

    @staticmethod
    def save_plan(duration, subject):
        attributes = ['date', 'duration', 'subject']
        curr_date = str(datetime.date(datetime.now()))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            with open(file_path, 'a') as f:
                writer = csv.DictWriter(f, fieldnames=attributes)
                writer.writeheader()
                writer.writerow({'date' : curr_date, 'duration' : str(duration), 'subject' : str(subject)})
                # save success
                return 1
        else:
            with open(file_path, 'a') as f:
                writer = csv.DictWriter(f, fieldnames=attributes)
                if not StudyForm.check_plan(curr_date):
                    writer.writerow({'date' : curr_date, 'duration' : str(duration), 'subject' : str(subject)})
                    return 1
                else:
                    # repeated date
                    return 0

    def submit(self, dispatcher, tracker, domain):
        #type: (CollcetingDispatcher, Tracker, Dict[Text, Any])
        # -> List[Dict]

        duration = tracker.get_slot('duration')
        subject = tracker.get_slot('subject')
        if self.save_plan(duration, subject):
            message = 'You\'ve decided studying ' + str(duration) + 'h on ' + str(subject)
        else:
            message = 'You have already made a plan today. Please come tomorrow.'
        dispatcher.utter_message(message)
        return []

    def slot_mapping(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"subject" : [self.from_entity(entity="subject",
                                            intent=["inform",
                                                    "study_attempt"]),
                            self.from_text(intent=None)],
                "duration" : [self.from_entity(entity="subject",
                                            intent=["inform",
                                                    "study_attempt"]),
                            self.from_text(intent=None)]}

    # @staticmethod
    # def supported_subjects() -> List[Text]:
    #     #list of supported subjects for validation
    #     return ["math",
    #             "chemistry",
    #             "english",
    #             "computer science",
    #             "literature",
    #             "physiology",
    #             "physics",
    #             "french",
    #             "chinese",
    #             "japanese"]
    #
    # def validate_subject(self, value, dispatcher, tracker, domain):
    #     #type: (Text, CollectingDispatcher, Tracker, Dict[Text, Any])
    #     # -> Dict[Text, Any]
    #
    #     if value.lower() in self.supported_subjects():
    #         return {"subject": value}
    #     else:
    #         # not a supported subject, ask again
    #         return {"subject": None}

    @staticmethod
    def is_float(string):
        # (Text) -> bool
        try:
            float(string)
            return True
        except ValueError:
            return False

    def validate_duration(self, value, dispatcher, tracker, domain):
        #type: (Text, CollectingDispatcher, Tracker, Dict[Text, Any])
        # -> Dict[Text, Any]

        if self.is_float(value):
            if float(value)>=0 and float(value)<=10:
                return {"duration": value}
            elif float(value)<0:
                dispatcher.utter_message(response='utter_neg_hour')
                return {"duration": None}
            else:
                dispatcher.utter_message(response='utter_study_too_much')
                return {"duration": None}
        else:
            dispatcher.utter_message(response='utter_invalid_hour')
            return {"duration": None}
