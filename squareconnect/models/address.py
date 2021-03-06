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


class Address(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address_line_1=None, address_line_2=None, address_line_3=None, locality=None, sublocality=None, sublocality_2=None, sublocality_3=None, administrative_district_level_1=None, administrative_district_level_2=None, administrative_district_level_3=None, postal_code=None, country=None, first_name=None, last_name=None, organization=None):
        """
        Address - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_line_1': 'str',
            'address_line_2': 'str',
            'address_line_3': 'str',
            'locality': 'str',
            'sublocality': 'str',
            'sublocality_2': 'str',
            'sublocality_3': 'str',
            'administrative_district_level_1': 'str',
            'administrative_district_level_2': 'str',
            'administrative_district_level_3': 'str',
            'postal_code': 'str',
            'country': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'organization': 'str'
        }

        self.attribute_map = {
            'address_line_1': 'address_line_1',
            'address_line_2': 'address_line_2',
            'address_line_3': 'address_line_3',
            'locality': 'locality',
            'sublocality': 'sublocality',
            'sublocality_2': 'sublocality_2',
            'sublocality_3': 'sublocality_3',
            'administrative_district_level_1': 'administrative_district_level_1',
            'administrative_district_level_2': 'administrative_district_level_2',
            'administrative_district_level_3': 'administrative_district_level_3',
            'postal_code': 'postal_code',
            'country': 'country',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'organization': 'organization'
        }

        self._address_line_1 = address_line_1
        self._address_line_2 = address_line_2
        self._address_line_3 = address_line_3
        self._locality = locality
        self._sublocality = sublocality
        self._sublocality_2 = sublocality_2
        self._sublocality_3 = sublocality_3
        self._administrative_district_level_1 = administrative_district_level_1
        self._administrative_district_level_2 = administrative_district_level_2
        self._administrative_district_level_3 = administrative_district_level_3
        self._postal_code = postal_code
        self._country = country
        self._first_name = first_name
        self._last_name = last_name
        self._organization = organization

    @property
    def address_line_1(self):
        """
        Gets the address_line_1 of this Address.
        The first line of the address.  Fields that start with `address_line` provide the address's most specific details, like street number, street name, and building name. They do *not* provide less specific details like city, state/province, or country (these details are provided in other fields).

        :return: The address_line_1 of this Address.
        :rtype: str
        """
        return self._address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1):
        """
        Sets the address_line_1 of this Address.
        The first line of the address.  Fields that start with `address_line` provide the address's most specific details, like street number, street name, and building name. They do *not* provide less specific details like city, state/province, or country (these details are provided in other fields).

        :param address_line_1: The address_line_1 of this Address.
        :type: str
        """

        self._address_line_1 = address_line_1

    @property
    def address_line_2(self):
        """
        Gets the address_line_2 of this Address.
        The second line of the address, if any.

        :return: The address_line_2 of this Address.
        :rtype: str
        """
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2):
        """
        Sets the address_line_2 of this Address.
        The second line of the address, if any.

        :param address_line_2: The address_line_2 of this Address.
        :type: str
        """

        self._address_line_2 = address_line_2

    @property
    def address_line_3(self):
        """
        Gets the address_line_3 of this Address.
        The third line of the address, if any.

        :return: The address_line_3 of this Address.
        :rtype: str
        """
        return self._address_line_3

    @address_line_3.setter
    def address_line_3(self, address_line_3):
        """
        Sets the address_line_3 of this Address.
        The third line of the address, if any.

        :param address_line_3: The address_line_3 of this Address.
        :type: str
        """

        self._address_line_3 = address_line_3

    @property
    def locality(self):
        """
        Gets the locality of this Address.
        The city or town of the address.

        :return: The locality of this Address.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Address.
        The city or town of the address.

        :param locality: The locality of this Address.
        :type: str
        """

        self._locality = locality

    @property
    def sublocality(self):
        """
        Gets the sublocality of this Address.
        A civil region within the address's `locality`, if any.

        :return: The sublocality of this Address.
        :rtype: str
        """
        return self._sublocality

    @sublocality.setter
    def sublocality(self, sublocality):
        """
        Sets the sublocality of this Address.
        A civil region within the address's `locality`, if any.

        :param sublocality: The sublocality of this Address.
        :type: str
        """

        self._sublocality = sublocality

    @property
    def sublocality_2(self):
        """
        Gets the sublocality_2 of this Address.
        A civil region within the address's `sublocality`, if any.

        :return: The sublocality_2 of this Address.
        :rtype: str
        """
        return self._sublocality_2

    @sublocality_2.setter
    def sublocality_2(self, sublocality_2):
        """
        Sets the sublocality_2 of this Address.
        A civil region within the address's `sublocality`, if any.

        :param sublocality_2: The sublocality_2 of this Address.
        :type: str
        """

        self._sublocality_2 = sublocality_2

    @property
    def sublocality_3(self):
        """
        Gets the sublocality_3 of this Address.
        A civil region within the address's `sublocality_2`, if any.

        :return: The sublocality_3 of this Address.
        :rtype: str
        """
        return self._sublocality_3

    @sublocality_3.setter
    def sublocality_3(self, sublocality_3):
        """
        Sets the sublocality_3 of this Address.
        A civil region within the address's `sublocality_2`, if any.

        :param sublocality_3: The sublocality_3 of this Address.
        :type: str
        """

        self._sublocality_3 = sublocality_3

    @property
    def administrative_district_level_1(self):
        """
        Gets the administrative_district_level_1 of this Address.
        A civil entity within the address's country. In the US, this is the state.

        :return: The administrative_district_level_1 of this Address.
        :rtype: str
        """
        return self._administrative_district_level_1

    @administrative_district_level_1.setter
    def administrative_district_level_1(self, administrative_district_level_1):
        """
        Sets the administrative_district_level_1 of this Address.
        A civil entity within the address's country. In the US, this is the state.

        :param administrative_district_level_1: The administrative_district_level_1 of this Address.
        :type: str
        """

        self._administrative_district_level_1 = administrative_district_level_1

    @property
    def administrative_district_level_2(self):
        """
        Gets the administrative_district_level_2 of this Address.
        A civil entity within the address's `administrative_district_level_1`. In the US, this is the county.

        :return: The administrative_district_level_2 of this Address.
        :rtype: str
        """
        return self._administrative_district_level_2

    @administrative_district_level_2.setter
    def administrative_district_level_2(self, administrative_district_level_2):
        """
        Sets the administrative_district_level_2 of this Address.
        A civil entity within the address's `administrative_district_level_1`. In the US, this is the county.

        :param administrative_district_level_2: The administrative_district_level_2 of this Address.
        :type: str
        """

        self._administrative_district_level_2 = administrative_district_level_2

    @property
    def administrative_district_level_3(self):
        """
        Gets the administrative_district_level_3 of this Address.
        A civil entity within the address's `administrative_district_level_2`, if any.

        :return: The administrative_district_level_3 of this Address.
        :rtype: str
        """
        return self._administrative_district_level_3

    @administrative_district_level_3.setter
    def administrative_district_level_3(self, administrative_district_level_3):
        """
        Sets the administrative_district_level_3 of this Address.
        A civil entity within the address's `administrative_district_level_2`, if any.

        :param administrative_district_level_3: The administrative_district_level_3 of this Address.
        :type: str
        """

        self._administrative_district_level_3 = administrative_district_level_3

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Address.
        The address's postal code.

        :return: The postal_code of this Address.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Address.
        The address's postal code.

        :param postal_code: The postal_code of this Address.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Address.
        The address's country, in ISO 3166-1-alpha-2 format.

        :return: The country of this Address.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Address.
        The address's country, in ISO 3166-1-alpha-2 format.

        :param country: The country of this Address.
        :type: str
        """

        self._country = country

    @property
    def first_name(self):
        """
        Gets the first_name of this Address.
        Optional first name when it's representing recipient.

        :return: The first_name of this Address.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Address.
        Optional first name when it's representing recipient.

        :param first_name: The first_name of this Address.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Address.
        Optional last name when it's representing recipient.

        :return: The last_name of this Address.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Address.
        Optional last name when it's representing recipient.

        :param last_name: The last_name of this Address.
        :type: str
        """

        self._last_name = last_name

    @property
    def organization(self):
        """
        Gets the organization of this Address.
        Optional organization name when it's representing recipient.

        :return: The organization of this Address.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this Address.
        Optional organization name when it's representing recipient.

        :param organization: The organization of this Address.
        :type: str
        """

        self._organization = organization

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
