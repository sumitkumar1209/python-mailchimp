from __future__ import unicode_literals
from ..baseapi import BaseApi


class File(BaseApi):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.endpoint = 'file-manager/files'

    def all(self, **kwargs):
        return self._mc_client._get(url=self.endpoint, **kwargs)

    def create(self, data):
        return self._mc_client._post(url=self.endpoint, data=data)
