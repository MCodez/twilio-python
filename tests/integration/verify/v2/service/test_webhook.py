# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base import serialize
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class WebhookTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .webhooks.create(friendly_name="friendly_name", event_types=['event_types'], webhook_url="webhook_url")

        values = {
            'FriendlyName': "friendly_name",
            'EventTypes': serialize.map(['event_types'], lambda e: e),
            'WebhookUrl': "webhook_url",
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/YWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "YWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "name",
                "event_types": [
                    "factor.deleted",
                    "factor.verified"
                ],
                "webhook_method": "POST",
                "webhook_url": "https://owlbank.twilio.com",
                "status": "enabled",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .webhooks.create(friendly_name="friendly_name", event_types=['event_types'], webhook_url="webhook_url")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .webhooks("YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks/YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/YWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "YWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "name",
                "event_types": [
                    "factor.deleted",
                    "factor.verified"
                ],
                "webhook_method": "POST",
                "webhook_url": "https://owlbank.twilio.com",
                "status": "disabled",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .webhooks("YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .webhooks("YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks/YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .webhooks("YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .webhooks("YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks/YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/YWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "YWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "name",
                "event_types": [
                    "factor.deleted",
                    "factor.verified"
                ],
                "webhook_method": "POST",
                "webhook_url": "https://owlbank.twilio.com",
                "status": "enabled",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .webhooks("YWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .webhooks.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "webhooks": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "webhooks"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .webhooks.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "webhooks": [
                    {
                        "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/YWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "YWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "name",
                        "event_types": [
                            "factor.deleted",
                            "factor.verified"
                        ],
                        "webhook_method": "POST",
                        "webhook_url": "https://owlbank.twilio.com",
                        "status": "enabled",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "webhooks"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .webhooks.list()

        self.assertIsNotNone(actual)
