import requests
import xmltodict


def build_url(method_name):
    return f"{ABNService.BASE_URL}/{method_name}"


def get_guid():
    return 'YOUR-GUID-AUTHENTICATION-KEY'


class ABNService:

    BASE_URL = 'https://abr.business.gov.au/ABRXMLSearch/AbrXmlSearch.asmx'
    SEARCH_BY_NAME_URL = 'ABRSearchByNameAdvancedSimpleProtocol2017'
    SEARCH_BY_ABN_URL = 'SearchByABNv202001'
    SEARCH_BY_ACN_URL = 'SearchByASICv201408'
    INCLUDE_HISTORICAL_DETAILS = 'Y'
    SEARCH_WIDTH = 'narrow'

    @staticmethod
    def search_by_abn_get(abn):
        response = requests.get(
            f"{ABNService.BASE_URL}/{ABNService.SEARCH_BY_ABN_URL}?searchString={abn}&includeHistoricalDetails="
            f"{ABNService.INCLUDE_HISTORICAL_DETAILS}&authenticationGuid={get_guid()}")

        data = xmltodict.parse(response.text, dict_constructor=dict)['ABRPayloadSearchResults']['response']

        if 'exception' in data.keys():
            return {'exception': 'ABN Not Found'}
        else:
            return data['businessEntity202001']

    @staticmethod
    def search_by_abn_post(abn):
        payload = {
            'searchString': abn,
            'includeHistoricalDetails': ABNService.INCLUDE_HISTORICAL_DETAILS,
            'authenticationGuid': get_guid()
        }

        response = requests.request(
            method='post',
            url=build_url(ABNService.SEARCH_BY_ABN_URL),
            data=payload
        )

        # converting xml data to dict. dict_construct=dict prevents from creating OrderedDicts
        data = xmltodict.parse(response.text, dict_constructor=dict)['ABRPayloadSearchResults']['response']

        if 'exception' in data.keys():
            return {'exception': 'ABN Not Found'}
        else:
            return data['businessEntity202001']

    @staticmethod
    def search_by_acn_get(acn):
        response = requests.get(f"{ABNService.BASE_URL}/{ABNService.SEARCH_BY_ACN_URL}?searchString={acn}"
                                f"&includeHistoricalDetails={ABNService.INCLUDE_HISTORICAL_DETAILS}"
                                f"&authenticationGuid={get_guid()}")

        data = xmltodict.parse(response.text, dict_constructor=dict)['ABRPayloadSearchResults']['response']

        if 'exception' in data.keys():
            return {'exception': 'ACN Not Found'}
        else:
            return data['businessEntity201408']

    @staticmethod
    def search_by_acn_post(acn):
        payload = {
            'searchString': acn,
            'includeHistoricalDetails': ABNService.INCLUDE_HISTORICAL_DETAILS,
            'authenticationGuid': get_guid()
        }

        response = requests.request(
            method='post',
            url=build_url(ABNService.SEARCH_BY_ACN_URL),
            data=payload
        )

        # converting xml data to dict. dict_construct=dict prevents from creating OrderedDicts
        data = xmltodict.parse(response.text, dict_constructor=dict)['ABRPayloadSearchResults']['response']

        if 'exception' in data.keys():
            return {'exception': 'ACN Not Found'}
        else:
            return data['businessEntity201408']

    @staticmethod
    def search_by_name_get(name, postcode='', max_search_result='20'):
        response = requests.get(
            f"{ABNService.BASE_URL}/{ABNService.SEARCH_BY_NAME_URL}?name={name}"
            f"&postcode={postcode}&legalName='Y'&tradingName='Y'&businessName='Y'&activeABNsOnly='Y'&NSW='Y'&SA='Y'"
            f"&ACT='Y'&VIC='Y'&WA='Y'&NT='Y'&QLD='Y'&TAS='Y'&authenticationGuid={get_guid()}&searchWidth=''&"
            f"minimumScore=''&maxSearchResults={max_search_result}")

        data = xmltodict.parse(response.text, dict_constructor=dict)['ABRPayloadSearchResults']['response']

        if 'exception' in data.keys():
            return {'exception': 'Business Not Found'}
        else:
            return data['searchResultsList']['searchResultsRecord']

    @staticmethod
    def search_by_name_post(name, postcode='', max_search_result=''):
        """
            :param name: business name to be searched
            :param postcode: (optional) postcode of a state
            :param max_search_result: (optional) number of records to be returned in a single response
            :return:
                    1. list of businesses if more than one business exists
                    2. dictionary object consisting business info if only a single business exists
                    3. dictionary object consisting exception if no business is found
        """

        if len(name.split()) == 1:
            ABNService.SEARCH_WIDTH = 'typical'

        payload = {
            'name': name,
            'postcode': postcode,
            'legalName': 'Y',
            'tradingName': 'Y',
            'businessName': 'Y',
            'activeABNsOnly': 'Y',
            'NSW': 'Y',
            'SA': 'Y',
            'ACT': 'Y',
            'VIC': 'Y',
            'WA': 'Y',
            'NT': 'Y',
            'QLD': 'Y',
            'TAS': 'Y',
            'authenticationGuid': get_guid(),
            'searchWidth': ABNService.SEARCH_WIDTH,
            'minimumScore': '',
            'maxSearchResults': max_search_result,
        }

        response = requests.request(
            method='post',
            url=build_url(ABNService.SEARCH_BY_NAME_URL),
            data=payload
        )

        data = xmltodict.parse(response.text, dict_constructor=dict)['ABRPayloadSearchResults']['response']

        if 'exception' in data.keys():
            return {'exception': 'Business Not Found'}
        else:
            return data['searchResultsList']['searchResultsRecord']
