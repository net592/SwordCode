#!/usr/local/python27/bin/python
"""
用于CMDB绑定Salt配置数据
By xuzeming6 date20201211
"""
import sys
import yaml
import requests

 
def get_minion_classes(minion):
    headers = {'Authorization': 'Bearer joIZYleoZlIZBr3Q0fY7rPKrKGwtNL'}
    url = 'http://stree.jd.com/api/salt/hosts/{}/state'.format(minion)
 
    try:
        res = requests.get(url, headers=headers)
        states = res.json()['states']
    except Exception:
        states = []
 
    result = {
        'environment': 'base',
        'classes': states,
        'parameters': [],
    }
 
    print(yaml.safe_dump(result))
 
 
def main():
    if len(sys.argv) < 2:
        print("")
    minion = sys.argv[1]
    get_minion_classes(minion)
 
 
if __name__ == '__main__':
    main()