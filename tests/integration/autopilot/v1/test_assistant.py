# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class AssistantTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants("UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2017-07-04T08:34:00Z",
                "date_updated": "2017-07-04T08:34:00Z",
                "friendly_name": "so so friendly",
                "latest_model_build_sid": null,
                "log_queries": true,
                "development_stage": "in-development",
                "needs_model_build": false,
                "sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "so-so-unique",
                "links": {
                    "field_types": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/FieldTypes",
                    "tasks": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                    "model_builds": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds",
                    "queries": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries",
                    "style_sheet": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/StyleSheet",
                    "defaults": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Defaults",
                    "dialogues": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Dialogues",
                    "webhooks": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"
                },
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "callback_url": "https://example.com/callback_url",
                "callback_events": "model_build_completed model_build_failed"
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants("UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://autopilot.twilio.com/v1/Assistants',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "assistants": [],
                "meta": {
                    "first_page_url": "https://autopilot.twilio.com/v1/Assistants?PageSize=50&Page=0",
                    "key": "assistants",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://autopilot.twilio.com/v1/Assistants?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "assistants": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2017-07-04T08:34:00Z",
                        "date_updated": "2017-07-04T08:34:00Z",
                        "friendly_name": "so so friendly",
                        "latest_model_build_sid": null,
                        "log_queries": true,
                        "development_stage": "in-development",
                        "needs_model_build": false,
                        "sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "so-so-unique",
                        "links": {
                            "field_types": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/FieldTypes",
                            "tasks": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                            "model_builds": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds",
                            "queries": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries",
                            "style_sheet": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/StyleSheet",
                            "defaults": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Defaults",
                            "dialogues": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Dialogues",
                            "webhooks": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"
                        },
                        "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "callback_url": "https://example.com/callback_url",
                        "callback_events": "model_build_completed model_build_failed"
                    }
                ],
                "meta": {
                    "first_page_url": "https://autopilot.twilio.com/v1/Assistants?PageSize=50&Page=0",
                    "key": "assistants",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://autopilot.twilio.com/v1/Assistants?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://autopilot.twilio.com/v1/Assistants',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2017-07-04T08:34:00Z",
                "date_updated": "2017-07-04T08:34:00Z",
                "friendly_name": "so so friendly",
                "latest_model_build_sid": null,
                "log_queries": true,
                "development_stage": "in-development",
                "needs_model_build": false,
                "sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "so-so-unique",
                "links": {
                    "field_types": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/FieldTypes",
                    "tasks": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                    "model_builds": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds",
                    "queries": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries",
                    "style_sheet": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/StyleSheet",
                    "defaults": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Defaults",
                    "dialogues": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Dialogues",
                    "webhooks": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"
                },
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "callback_url": "https://example.com/callback_url",
                "callback_events": "model_build_completed model_build_failed"
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants.create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants("UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2017-07-04T08:34:00Z",
                "date_updated": "2017-07-04T08:34:00Z",
                "friendly_name": "so so friendly",
                "latest_model_build_sid": null,
                "log_queries": true,
                "development_stage": "in-development",
                "needs_model_build": false,
                "sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "so-so-unique",
                "links": {
                    "field_types": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/FieldTypes",
                    "tasks": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                    "model_builds": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ModelBuilds",
                    "queries": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queries",
                    "style_sheet": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/StyleSheet",
                    "defaults": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Defaults",
                    "dialogues": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Dialogues",
                    "webhooks": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"
                },
                "url": "https://autopilot.twilio.com/v1/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "callback_url": "https://example.com/callback_url",
                "callback_events": "model_build_completed model_build_failed"
            }
            '''
        ))

        actual = self.client.autopilot.v1.assistants("UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.autopilot.v1.assistants("UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://autopilot.twilio.com/v1/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.autopilot.v1.assistants("UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
