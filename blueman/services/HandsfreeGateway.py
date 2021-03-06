# coding=utf-8
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from blueman.Service import Service
from blueman.Sdp import HANDSFREE_SVCLASS_ID


class HandsfreeGateway(Service):
    __group__ = 'audio'
    __svclass_id__ = HANDSFREE_SVCLASS_ID
    __icon__ = "blueman-handsfree"
    __priority__ = 10
