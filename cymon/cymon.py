import json
import requests
from urllib import quote_plus

class Cymon(object):

    def __init__(self, auth_token=None, endpoint='https://cymon.io/api/nexus/v1'):
        self.endpoint = endpoint
        self.session = requests.Session()
        self.session.headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
        }
        if auth_token:
            self.session.headers.update({'Authorization': 'Token {0}'.format(auth_token)})

    def get(self, method, params=None):
        r = self.session.get(self.endpoint + method, params=params)
        r.raise_for_status()
        return r

    def post(self, method, params, headers=None):
        r = self.session.post(self.endpoint + method, data=json.dumps(params), headers=headers)
        r.raise_for_status()
        return r
    
    def list(self):
        r = self.get('')
        return json.loads(r.text)

    def ip_lookup(self, ip_addr):
        r = self.get('/ip/' + ip_addr)
        return json.loads(r.text)

    def ip_events(self, ip_addr):
        r = self.get('/ip/' + ip_addr + '/events')
        return json.loads(r.text)

    def ip_domains(self, ip_addr):
        r = self.get('/ip/' + ip_addr + '/domains')
        return json.loads(r.text)

    def ip_urls(self, ip_addr):
        r = self.get('/ip/' + ip_addr + '/urls')
        return json.loads(r.text)
        
    def ip_timeline(self, ip_addr):
        r = self.get('/ip/' + ip_addr + '/timeline') 
        return json.loads(r.text)

    def domain_lookup(self, name):
        r = self.get('/domain/' + name)
        return json.loads(r.text)
    
    def domain_events(self, name):
        '''Not sure if this is functioning on Cymon.io'''
        r = self.get('/domain/' + name + '/events')
        return json.loads(r.text)

    def url_lookup(self, location):
        r = self.get('/url/' + quote_plus(location))
        return json.loads(r.text)

    def ip_blacklist(self, tag, days=1):
        ''' supported tags: malware, botnet, spam, phishing, dnsbl, blacklist '''
        r = self.get('/blacklist/ip/' + tag + '/?days=%d' %(days))
        return json.loads(r.text)

    def domain_blacklist(self, tag, days=1):
        ''' supported tags: malware, botnet, spam, phishing, dnsbl, blacklist '''
        r = self.get('/blacklist/domain/' + tag + '/?days=%d' %(days))
        return json.loads(r.text)
        
    def domain_dga(self, name):
        r = self.get('/dga/' + name)
        return json.loads(r.text)