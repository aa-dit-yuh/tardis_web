import yaml
import urllib2

f = open('tardis_basic.yml', 'r')

testYaml = yaml.load(f)
print testYaml
