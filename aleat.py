#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random
import webapp


class servUrlAleat(webapp.webApp):

    def process(self, parsedRequest):
        rand_num = random.randrange(1000000)
        return ('200 OK',
                "<html><body>Hola. " +
                "<a href='" + str(rand_num) +
                "'>Dame otra</a>" +
                "</body></html>" +
                "\r\n")

if __name__ == "__main__":
    testWebApp = servUrlAleat("localhost", 1234)
