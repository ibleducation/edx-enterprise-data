# -*- coding: utf-8 -*-
"""
Client for connecting to a Vertica database.
"""
from __future__ import absolute_import, unicode_literals

from logging import getLogger

import vertica_python


LOGGER = getLogger(__name__)


class VerticaClient(object):
    """
    Client for connecting to Vertica.
    """

    def __init__(self, host, username, password):
        """
        Instantiate a new client using the Django settings to determine the vertica credentials.

        If there are none configured, throw an exception.
        """
        self.connection_info = {
            'host': host,
            'user': username,
            'password': password,
            'database': 'warehouse',
        }

        self.connection = None

    def connect(self):
        """
        Open a connection to Vertica.
        """
        self.connection = vertica_python.connect(**self.connection_info)

    def close_connection(self):
        """
        Close the connection to vertica.
        """
        self.connection.close()
        self.connection = None

    def stream_results(self, query):
        """
        Streams the results for a query using the current connection.
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        for row in cursor.iterate():
            yield row

    def fetch_results(self, query):
        """
        Fetches all of the results for a query using the current connection.
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
