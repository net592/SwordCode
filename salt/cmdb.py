# -*- coding: utf-8 -*-
'''
"""
用于CMDB绑定Salt获取pillar数据
By xuzeming6 date20201211
"""
A module that adds data to the Pillar structure retrieved by an http request
 
 
Configuring the HTTP_JSON ext_pillar
====================================
 
Set the following Salt config to setup Foreman as external pillar source:
 
.. code-block:: yaml
 
  ext_pillar:
    - http_json:
        url: http://example.com/api/minion_id
        ::TODO::
        username: username
        password: password
 
Module Documentation
====================
'''
 
# Import python libs
from __future__ import absolute_import
import logging
 
# Import Salt libs
import salt.ext.six as six
 
 
def ext_pillar(minion_id,
               pillar,  # pylint: disable=W0613
               url=None):
    '''
    Read pillar data from HTTP response.
 
    :param url String to make request
    :returns dict with pillar data to add
    :returns empty if error
    '''
    # Set up logging
    log = logging.getLogger(__name__)
    #url = "http://itree.jd.com"
    headers = { "Authorization": "Bearer joIZYleoZlIZBr3Q0fY7rPKrKGwtNL" }
    host_info = __salt__['http.query'](url=url + "/api/hosts/" + minion_id, header_dict=headers, decode=True, decode_type='json')
    #stree = __salt__['http.query'](url=url + "/api/host/tag?host=" + minion_id, decode=True, decode_type='json')
    itree = __salt__['http.query'](url=url + "/api/stree/hosts/" + minion_id + "/services", header_dict=headers, decode=True, decode_type='json')
    data = {}
    log.info('minion_id: %s, stree: %s, host_info: %s' % (minion_id,host_info,itree) )
    if 'dict' in host_info and 'dict' in itree:
        data["host_info"] = host_info["dict"]["host"]
        data["itree"] = itree["dict"]["nodegroups"]
        return data
    log.error(str(itree) + "  " + minion_id)
    log.error(minion_id + ' Error caught on query to ' + url + '\nMore Info:\n')
 
    for k, v in six.iteritems(data):
        log.error(k + ' : ' + v)
 
    return {}