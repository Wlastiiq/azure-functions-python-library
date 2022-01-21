#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from azure.functions.decorators.core import Trigger


class EventHubTrigger(Trigger):

    def __init__(self, name, connection):
        self.connection = connection
        super(EventHubTrigger, self).__init__(name)

    @staticmethod
    def get_binding_name():
        return "EventHubTrigger"

    def get_dict_repr(self):
        return {"connection": self.connection,
                "name": self.name}