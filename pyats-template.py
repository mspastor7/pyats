# created by Eric Velandia

from pyats.topology import loader

testbed = loader.load('default_testbed.yaml')

for dev_name,dev_object in testbed.devices.items():
   print("I am device {d}".format(d=dev_name))
   dev_object.connect()
   dev_object.execute('config term', allow_state_change=True)
   dev_object.execute('ip access-list standard ACCESO_SNMP')
   dev_object.execute('permit host 10.181.15.28 log')
