# Copyright 2012 Hewlett-Packard Development Company, L.P. All Rights Reserved.
#
# Author: Kiall Mac Innes <kiall@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from moniker.tests.test_agent import AgentTestCase


class AgentServiceTest(AgentTestCase):
    __test__ = True

    def setUp(self):
        super(AgentServiceTest, self).setUp()
        self.service = self.get_agent_service()

    def test_start_and_stop(self):
        # Ensures the start/stop actions don't raise
        self.service.start()
        self.service.stop()
