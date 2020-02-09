import logging
import logstash
import sys
import requests

class ElkServer:
    ip = '107.23.247.185'
    udp_port = 5959

myIp = None
try:
    myIp = requests.get('https://checkip.amazonaws.com').text.strip()
    print('my ip: {}'.format(myIp))
except:
    logger.error('python-logstash: error resolving IP')

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler(ElkServer.ip, ElkServer.udp_port, version=1))

logger.error('python-logstash: test logstash error message.')
logger.info('python-logstash: test logstash info message.')
logger.warning('python-logstash: test logstash warning message.')
 
# add extra field to logstash message
extra = {
    'python-version': 'python version: ' + repr(sys.version_info),
    'ip': myIp
}
logger.info('python-logstash: test extra fields', extra=extra)