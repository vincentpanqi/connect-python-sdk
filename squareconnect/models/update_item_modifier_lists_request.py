# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class UpdateItemModifierListsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, item_ids=None, modifier_lists_to_enable=None, modifier_lists_to_disable=None):
        """
        UpdateItemModifierListsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'item_ids': 'list[str]',
            'modifier_lists_to_enable': 'list[str]',
            'modifier_lists_to_disable': 'list[str]'
        }

        self.attribute_map = {
            'item_ids': 'item_ids',
            'modifier_lists_to_enable': 'modifier_lists_to_enable',
            'modifier_lists_to_disable': 'modifier_lists_to_disable'
        }

        self._item_ids = item_ids
        self._modifier_lists_to_enable = modifier_lists_to_enable
        self._modifier_lists_to_disable = modifier_lists_to_disable

    @property
    def item_ids(self):
        """
        Gets the item_ids of this UpdateItemModifierListsRequest.
        The [CatalogItem](#type-catalogitem)s whose [CatalogModifierList](#type-catalogmodifierlist)s are being updated.

        :return: The item_ids of this UpdateItemModifierListsRequest.
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """
        Sets the item_ids of this UpdateItemModifierListsRequest.
        The [CatalogItem](#type-catalogitem)s whose [CatalogModifierList](#type-catalogmodifierlist)s are being updated.

        :param item_ids: The item_ids of this UpdateItemModifierListsRequest.
        :type: list[str]
        """

        self._item_ids = item_ids

    @property
    def modifier_lists_to_enable(self):
        """
        Gets the modifier_lists_to_enable of this UpdateItemModifierListsRequest.
        The set of [CatalogModifierList](#type-catalogmodifierlist)s (referenced by ID) to enable for the [CatalogItem](#type-catalogitem).

        :return: The modifier_lists_to_enable of this UpdateItemModifierListsRequest.
        :rtype: list[str]
        """
        return self._modifier_lists_to_enable

    @modifier_lists_to_enable.setter
    def modifier_lists_to_enable(self, modifier_lists_to_enable):
        """
        Sets the modifier_lists_to_enable of this UpdateItemModifierListsRequest.
        The set of [CatalogModifierList](#type-catalogmodifierlist)s (referenced by ID) to enable for the [CatalogItem](#type-catalogitem).

        :param modifier_lists_to_enable: The modifier_lists_to_enable of this UpdateItemModifierListsRequest.
        :type: list[str]
        """

        self._modifier_lists_to_enable = modifier_lists_to_enable

    @property
    def modifier_lists_to_disable(self):
        """
        Gets the modifier_lists_to_disable of this UpdateItemModifierListsRequest.
        The set of [CatalogModifierList](#type-catalogmodifierlist)s (referenced by ID) to disable for the [CatalogItem](#type-catalogitem).

        :return: The modifier_lists_to_disable of this UpdateItemModifierListsRequest.
        :rtype: list[str]
        """
        return self._modifier_lists_to_disable

    @modifier_lists_to_disable.setter
    def modifier_lists_to_disable(self, modifier_lists_to_disable):
        """
        Sets the modifier_lists_to_disable of this UpdateItemModifierListsRequest.
        The set of [CatalogModifierList](#type-catalogmodifierlist)s (referenced by ID) to disable for the [CatalogItem](#type-catalogitem).

        :param modifier_lists_to_disable: The modifier_lists_to_disable of this UpdateItemModifierListsRequest.
        :type: list[str]
        """

        self._modifier_lists_to_disable = modifier_lists_to_disable

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
