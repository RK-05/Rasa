# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests


class ActionGetName(Action):

    def name(self) -> Text:
        return "action_get_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("name")
        dispatcher.utter_message("Hey {},how may i help you??".format(name))

        return [SlotSet("name",name)] 

class ActionApi(Action):

    def name(self) -> Text:
        return "action_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = 'http://db09032f7ce8.ngrok.io/'
        myobj = {'college': 'somevalue'}

        x = requests.post(url, json = myobj)
        
        dispatcher.utter_message(x)

        return [] 
