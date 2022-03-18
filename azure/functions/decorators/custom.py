#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.
from typing import Optional

from azure.functions.decorators.core import Trigger, \
    InputBinding, OutputBinding, DataType


class CustomInputBinding(InputBinding):
    binding_name: str = ""

    @staticmethod
    def get_binding_name() -> str:
        return CustomInputBinding.binding_name

    def __init__(self,
                 name: str,
                 type: str,
                 data_type: Optional[DataType] = None,
                 **kwargs):
        self.type = type
        CustomInputBinding.binding_name = type
        super().__init__(name=name, data_type=data_type)


class CustomOutputBinding(OutputBinding):
    binding_name: str = ""

    @staticmethod
    def get_binding_name() -> str:
        return CustomOutputBinding.binding_name

    def __init__(self,
                 name: str,
                 type: str,
                 data_type: Optional[DataType] = None,
                 **kwargs):
        self.type = type
        CustomOutputBinding.binding_name = type
        super().__init__(name=name, data_type=data_type)


class CustomTrigger(Trigger):
    binding_name: str = ""

    @staticmethod
    def get_binding_name() -> str:
        return CustomTrigger.binding_name

    def __init__(self,
                 name: str,
                 type: str,
                 data_type: Optional[DataType] = None,
                 **kwargs):
        self.type = type
        CustomTrigger.binding_name = type
        super().__init__(name=name, data_type=data_type)
