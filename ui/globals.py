#!/usr/bin/env python
#
# Lara Maia <dev@lara.click> 2015 ~ 2016
#
# The Steam Tools is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# The Steam Tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#

import logging

logger = logging.getLogger('SteamTools')


class Window:
    main = None
    profile = 0


class Logins:
    steam_check_page = 'https://steamcommunity.com/login/checkstoredlogin'
    steamgifts_check_page = 'https://www.steamgifts.com/account/profile/sync'
    steamcompanion_check_page ='https://steamcompanion.com/settings'
    steam_user = None
    steamgifts_user = None
    steamcompanion_user = None


class CardFarming:
    badge_set = {key: [] for key in ['gameID', 'gameName', 'cardCount', 'cardValue']}
    badge_current = 0
    game_start_time = None
    is_running = False


class FakeApp:
    id = None
    process = None
    is_running = False
