from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_dynamic_link"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link="http://www.facebook.com/"
        # dispatcher.utter_message(text="Hello World!")
        print("Link: ",tracker.get_slot('LINK'))
        text=tracker.latest_message['text']
        print(text)
        dispatcher.utter_template("utter_info",tracker,link=Link)
        return []