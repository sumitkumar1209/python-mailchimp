from __future__ import unicode_literals
from ..baseapi import BaseApi


class AutomationRemovedSubscriber(BaseApi):

    def __init__(self, *args, **kwargs):
        super(AutomationRemovedSubscriber, self).__init__(*args, **kwargs)
        self.endpoint = 'automations'

    def all(self, workflow_id='', **kwargs):
        """
        Return information about subscribers who have been removed from an Automation workflow.
        """
        return self._mc_client._get(url=self._build_path(workflow_id, 'removed-subscribers'), **kwargs)

    def create(self, workflow_id='', data=None):
        """
        Removes a subscriber from a specific Automation workflow.
        """
        return self._mc_client._post(
            url=self._build_path(workflow_id, 'removed-subscribers'),
            data=data)
