import requests
import time
import pytz
from dateutil import parser
from datetime import datetime
import copy
import requests
from elasticsearch import Elasticsearch

from django.conf import settings

from service.models import ServiceModule
from servicetree.models import JoinTag
from hostman.models import HostStypeField

class SystemStatusHandler():
    def __init__(self, index='', doc_type=''):
        hosts = [
            {'host': '10.206.245.211', 'port': 9172}
        ]
        user = 'twxyp_w'
        passwd = '11ecf7ae0cbaf360174cf6e9501e8dad'
        self.client = Elasticsearch(hosts=hosts, http_auth=(user, passwd))

        self.index = index or 'stree_report_data_metric'
        self.doc_type = doc_type or 'system'

        self.result = {
            'rows': [],
            'columns': [],
        }

    def get_begin_end(self):
        start = int(time.time())
        begin = start - start % 60 - 60 * 9
        end = start + 60
        begin = datetime.fromtimestamp(begin)
        end = datetime.fromtimestamp(end)

        tzinfo = pytz.timezone(settings.TIME_ZONE)
        begin = tzinfo.localize(begin)
        end = tzinfo.localize(end)

        index_date = begin.strftime('%Y%m%d')
        self.index = '{}_{}'.format(self.index, index_date)

        begin = begin.strftime('%Y-%m-%dT%H:%M:%S%z')
        end = end.strftime('%Y-%m-%dT%H:%M:%S%z')
        return begin, end

    def get_es_data(self, service):
        begin, end = self.get_begin_end()
        # hostlist = self.get_service_hosts(service)
        query = {
            'size': 0,
            'query': {
                'bool': {
                    'must': [
                        {
                            'term': {
                                "type": "system"
                            }
                        },
                        {
                            'term': {
                                "skey.keyword": service
                            }
                        },
                        {
                            'range': {
                                'now': {
                                    'gte': begin,
                                    'lt': end,
                                }
                            }
                        }
                    ]
                }
            },
            'aggs': {
                'hostname': {
                    'terms': {
                        'size': 10000,
                        'field': 'hostname.keyword'
                    },
                    'aggs': {
                        'now': {
                            'top_hits': {
                                'sort': [
                                    {
                                        'now': {
                                            'order': 'desc'
                                        }
                                    }
                                ],
                                'size': 1
                            }
                        }
                    }
                }
            }
        }
        data = self.client.search(index=self.index, doc_type=self.doc_type, body=query)
        hosts = {}
        for d in data['aggregations']['hostname']['buckets']:
            source = d['now']['hits']['hits'][0]['_source']
            hostname = source['hostname']
            dt = parser.parse(source['now'])
            source['now'] = dt.strftime('%Y-%m-%d %H:%M:%S')
            if hostname not in hosts:
                hosts[hostname] = source
            else:
                if source['now'] > hosts[hostname]['now']:
                    hosts[hostname] = source
        return list(hosts.values())

    def get_columns(self, service):
        # md = ServiceModule.objects.filter(service__skey__startswith=service)[0]
        # fields = HostStypeField.objects.filter(stype__name=md.service_type).all()
        result = []
        result.append({
            'field': 'hostname',
            'fieldName': '主机',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'cpu_percent',
            'fieldName': 'CPU使用率',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'mem_percent',
            'fieldName': '内存使用率',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'disk_percent',
            'fieldName': '硬盘使用率',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'hdd_write_MBps',
            'fieldName': 'HDD写入MBps',
            'show': False,
            'searchType': 'text',
        })
        result.append({
            'field': 'hdd_read_MBps',
            'fieldName': 'HDD读取MBps',
            'show': False,
            'searchType': 'text',
        })
        result.append({
            'field': 'ssd_write_MBps',
            'fieldName': 'SSD写入MBps',
            'show': False,
            'searchType': 'text',
        })
        result.append({
            'field': 'ssd_read_MBps',
            'fieldName': 'SSD读取MBps',
            'show': False,
            'searchType': 'text',
        })
        result.append({
            'field': 'disk_write_iops',
            'fieldName': '写入IOPS',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'disk_read_iops',
            'fieldName': '读取IOPS',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'net_send_Mbps',
            'fieldName': '发送带宽Mbps',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'net_recv_Mbps',
            'fieldName': '接收带宽Mbps',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'loadavg_1m_percpu',
            'fieldName': 'load 1m',
            'show': True,
            'searchType': 'text',
        })
        result.append({
            'field': 'loadavg_5m_percpu',
            'fieldName': 'load 5m',
            'show': False,
            'searchType': 'text',
        })
        result.append({
            'field': 'loadavg_15m_percpu',
            'fieldName': 'load 15m',
            'show': False,
            'searchType': 'text',
        })
        return result

    def get_service_hosts(self, service):
        '''query srv hosts'''
        schema = ['corp', 'owt', 'pdl', 'srv']
        length = len(service.split('.'))
        hosts = []
        skeys = service.split('.')
        tag = '&'.join(['{}={}'.format(schema[i], skeys[i]) for i in range(length)])
        joins = JoinTag.objects.filter(name=tag).all()
        for join in joins:
            hosts.extend(list(join.host.all().values_list('name', flat=True)))
        return hosts

    def get_data(self, service):

        self.result['columns'] = self.get_columns(service)
        self.result['rows'] = self.get_es_data(service)

        row_hosts = [h['hostname'] for h in self.result['rows']]
        hosts = self.get_service_hosts(service)
        for host in set(hosts) - set(row_hosts):
            self.result['rows'].append({
                'hostname': host,
                'cpu_percent': '',
                'mem_percent': '',
                'disk_percent': '',
                'hdd_write_MBps': '',
                'hdd_read_MBps': '',
                'ssd_write_MBps': '',
                'ssd_read_MBps': '',
                'net_send_Mbps': '',
                'net_recv_Mbps': '',
            })
        return self.result
