# Copyright (C) 2014 Okami, okami@fuzetsu.info

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from djradicale.models import DBCollection, DBProperties

from . import DAVClient


class DjRadicaleTestCase(TestCase):
    DATA_CASES = {
        # PUT #################################################################
        'PUT': {
            'request': '''BEGIN:VCALENDAR
CALSCALE:GREGORIAN
PRODID:-//Ximian//NONSGML Evolution Calendar//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:/freeassociation.sourceforge.net/Europe/Moscow
X-LIC-LOCATION:Europe/Moscow
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19300621T000000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19810401T000000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19811001T000000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19820401T000000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19821001T000000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19830401T000000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19831001T000000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19840401T000000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19840930T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19850331T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19850929T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19860330T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19860928T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19870329T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19870927T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19880327T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19880925T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19890326T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19890924T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19900325T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19900930T030000
TZOFFSETFROM:+0300
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:EEST
DTSTART:19910331T020000
TZOFFSETFROM:+0200
TZOFFSETTO:+0300
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:EET
DTSTART:19910929T030000
TZOFFSETFROM:+0300
TZOFFSETTO:+0200
END:STANDARD
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19920119T020000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19920329T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19920927T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19930328T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19930926T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19940327T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19940925T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19950326T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19950924T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19960331T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19961027T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19970330T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19971026T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19980329T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19981025T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:19990328T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:19991031T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20000326T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20001029T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20010325T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20011028T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20020331T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20021027T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20030330T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20031026T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20040328T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20041031T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20050327T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20051030T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20060326T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20061029T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20070325T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20071028T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20080330T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20081026T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20090329T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20091025T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
TZNAME:MSD
DTSTART:20100328T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20101031T030000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20110327T020000
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:STANDARD
BEGIN:STANDARD
TZNAME:MSK
DTSTART:20141026T020000
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
UID:20160729T101032Z-9313-1000-4291-10@localhost
DTSTAMP:20160729T063824Z
DTSTART;TZID=/freeassociation.sourceforge.net/Europe/Moscow:
 20160721T090000
DTEND;TZID=/freeassociation.sourceforge.net/Europe/Moscow:
 20160721T093000
SEQUENCE:2
SUMMARY:zzzzz
CLASS:PUBLIC
TRANSP:OPAQUE
CREATED:20160729T101116Z
LAST-MODIFIED:20160729T101116Z
END:VEVENT
END:VCALENDAR
''',
            'response': '',
        },
        # REPORT ##############################################################
        'REPORT': {
            'request': (
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                '<C:calendar-multiget xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:caldav">'
                '<D:prop><D:getetag/><C:calendar-data/></D:prop>'
                '<D:href>{url}</D:href></C:calendar-multiget>\n'
            ),
            'response': '''<?xml version='1.0' encoding='utf-8'?>
<multistatus xmlns="DAV:" xmlns:C="urn:ietf:params:xml:ns:caldav"><response><href>/radicale/user/calendar.ics/20160729T101032Z-9313-1000-4291-10_localhost-20160729T101116Z.ics</href><propstat><prop><getetag>"7e542ba33f6239c2fb6171ee1dec39c583e6462488c84c9b78e0361676ffb816"</getetag><C:calendar-data>BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
PRODID:-//Ximian//NONSGML Evolution Calendar//EN
BEGIN:VTIMEZONE
TZID:/freeassociation.sourceforge.net/Europe/Moscow
BEGIN:STANDARD
DTSTART:19300621T000000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19811001T000000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19821001T000000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19831001T000000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19840930T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19850929T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19860928T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19870927T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19880925T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19890924T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19900930T030000
TZNAME:MSK
TZOFFSETFROM:+0300
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19910929T030000
TZNAME:EET
TZOFFSETFROM:+0300
TZOFFSETTO:+0200
END:STANDARD
BEGIN:STANDARD
DTSTART:19920119T020000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19920927T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19930926T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19940925T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19950924T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19961027T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19971026T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19981025T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19991031T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20001029T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20011028T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20021027T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20031026T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20041031T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20051030T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20061029T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20071028T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20081026T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20091025T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20101031T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20110327T020000
TZNAME:MSK
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:STANDARD
BEGIN:STANDARD
DTSTART:20141026T020000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19810401T000000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19820401T000000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19830401T000000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19840401T000000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19850331T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19860330T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19870329T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19880327T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19890326T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19900325T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19910331T020000
TZNAME:EEST
TZOFFSETFROM:+0200
TZOFFSETTO:+0300
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19920329T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19930328T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19940327T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19950326T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19960331T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19970330T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19980329T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19990328T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20000326T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20010325T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20020331T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20030330T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20040328T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20050327T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20060326T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20070325T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20080330T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20090329T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20100328T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
X-LIC-LOCATION:Europe/Moscow
END:VTIMEZONE
BEGIN:VEVENT
UID:20160729T101032Z-9313-1000-4291-10@localhost
DTSTART;TZID=/freeassociation.sourceforge.net/Europe/Moscow:20160721T090000
DTEND;TZID=/freeassociation.sourceforge.net/Europe/Moscow:20160721T093000
CLASS:PUBLIC
CREATED:20160729T101116Z
DTSTAMP:20160729T063824Z
LAST-MODIFIED:20160729T101116Z
SEQUENCE:2
SUMMARY:zzzzz
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
</C:calendar-data></prop><status>HTTP/1.1 200 OK</status></propstat></response></multistatus>''',
        },
        # GET #################################################################
        'GET': {
            'request': '',
            'response': '''BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
PRODID:-//Ximian//NONSGML Evolution Calendar//EN
BEGIN:VTIMEZONE
TZID:/freeassociation.sourceforge.net/Europe/Moscow
BEGIN:STANDARD
DTSTART:19300621T000000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19811001T000000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19821001T000000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19831001T000000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19840930T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19850929T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19860928T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19870927T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19880925T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19890924T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19900930T030000
TZNAME:MSK
TZOFFSETFROM:+0300
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19910929T030000
TZNAME:EET
TZOFFSETFROM:+0300
TZOFFSETTO:+0200
END:STANDARD
BEGIN:STANDARD
DTSTART:19920119T020000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19920927T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19930926T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19940925T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19950924T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19961027T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19971026T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19981025T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:19991031T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20001029T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20011028T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20021027T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20031026T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20041031T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20051030T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20061029T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20071028T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20081026T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20091025T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20101031T030000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:STANDARD
DTSTART:20110327T020000
TZNAME:MSK
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:STANDARD
BEGIN:STANDARD
DTSTART:20141026T020000
TZNAME:MSK
TZOFFSETFROM:+0400
TZOFFSETTO:+0300
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19810401T000000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19820401T000000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19830401T000000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19840401T000000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19850331T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19860330T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19870329T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19880327T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19890326T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19900325T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19910331T020000
TZNAME:EEST
TZOFFSETFROM:+0200
TZOFFSETTO:+0300
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19920329T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19930328T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19940327T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19950326T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19960331T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19970330T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19980329T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:19990328T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20000326T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20010325T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20020331T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20030330T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20040328T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20050327T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20060326T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20070325T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20080330T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20090329T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
BEGIN:DAYLIGHT
DTSTART:20100328T020000
TZNAME:MSD
TZOFFSETFROM:+0300
TZOFFSETTO:+0400
END:DAYLIGHT
X-LIC-LOCATION:Europe/Moscow
END:VTIMEZONE
BEGIN:VEVENT
UID:20160729T101032Z-9313-1000-4291-10@localhost
DTSTART;TZID=/freeassociation.sourceforge.net/Europe/Moscow:20160721T090000
DTEND;TZID=/freeassociation.sourceforge.net/Europe/Moscow:20160721T093000
CLASS:PUBLIC
CREATED:20160729T101116Z
DTSTAMP:20160729T063824Z
LAST-MODIFIED:20160729T101116Z
SEQUENCE:2
SUMMARY:zzzzz
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
''',
        },
    }

    maxDiff = None

    def setUp(self):
        User.objects.create_user(username='user', password='password')
        DBCollection.objects.create(path="user/calendar.ics", parent_path="user")
        DBProperties.objects.create(path="user/calendar.ics", text='{"tag": "VCALENDAR"}')
        self.client = DAVClient()

    def report(self, name):
        path = reverse('djradicale:application', kwargs={
            'url': 'user/calendar.ics/',
        })
        response = self.client.report(
            path, data=self.DATA_CASES['REPORT']['request'].format(**{
                'url': '{}{}'.format(path, name),
            }))
        self.assertEqual(response.status_code, 207)
        # split the strings to avoid lf/crlf problems
        self.assertEqual(
            response.content.decode().split(),
            self.DATA_CASES['REPORT']['response'].split())

    def put(self, name):
        path = reverse('djradicale:application', kwargs={
            'url': 'user/calendar.ics/{}'.format(name),
        })
        response = self.client.put(
            path, data=self.DATA_CASES['PUT']['request'].format(**{
                'name': name,
            }))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.content.decode(),
            self.DATA_CASES['PUT']['response'])

    def get(self, name):
        path = reverse('djradicale:application', kwargs={
            'url': 'user/calendar.ics/{}'.format(name),
        })
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        # split the strings to avoid lf/crlf problems
        self.assertEqual(
            response.content.decode().split(),
            self.DATA_CASES['GET']['response'].split()
        )

    def test_everything(self):
        self.client.http_auth('user', 'password')
        # create
        name = '20160729T101032Z-9313-1000-4291-10_localhost-20160729T101116Z.ics'
        self.put(name=name)
        self.get(name=name)
        self.report(name=name)
