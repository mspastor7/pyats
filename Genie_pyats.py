# created by Mariano Pastor

from genie.conf import Genie
import csv
testbed = Genie.init("default_testbed.yaml")

device_interface_details = {}

for device in testbed.devices:
    testbed.devices[device].connect()
    interface_details = testbed.devices[device].parse("show interfaces")
    device_interface_details[device] = interface_details

interfaces_file = "interfaces.csv"
report_fields = ["Device", "Interface", "MAC Address"]

with open(interfaces_file, "w") as f:
    writer = csv.DictWriter(f, report_fields)
    writer.writeheader()

    for device, interfaces in device_interface_details.items():
        for interface, details in interfaces.items():
            writer.writerow(
                {
                    "Device": device,
                    "Interface": interface,
                    "MAC Address": details["mac_address"]
                }
            )

