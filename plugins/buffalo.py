""" Buffalo Plugin (botwot plugins.buffalo) """

# Copyright 2015 Ray Schulz <https://rascul.io>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import random

from pyaib.plugins import keyword, plugin_class


@plugin_class
class Buffalo(object):
	def __init__(self, context, config):
		self.buffalos = [
			"a large",
			"a small",
			"a fat",
			"an old",
			"a smelly",
			"a decrepit",
			"a young",
			"a healthy",
			"a delicious",
			"an oversized",
			"a skinny",
			"a sickly",
			"a wildly winged"]
	
	
	@keyword("buffalo")
	def keyword_buffalo(self, context, msg, trigger, args, kargs):
		""" throw a buffalo """
		
		target_user = " ".join(args) or msg.sender
		
		context.PRIVMSG(
			msg.channel or msg.sender, 
			"\x01ACTION throws %s buffalo at %s\x01" % (random.choice(self.buffalos), target_user))