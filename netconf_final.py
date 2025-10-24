from ncclient import manager
import xmltodict

import sendtexttowebex
import requests
import json


def create(student_id, router_ip, roomIdToGetMessages, ACCESS_TOKEN):
    netconf_config = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                    <name>{student_id}</name>
                    <description>Created via NETCONF</description>
                </Loopback>
            </interface>
        </native>
    </config>
    """


    try:
        # ใช้ router_ip ที่ส่งเข้ามา
        with manager.connect(
            host=router_ip,
            port=830,
            username="admin",
            password="cisco",
            hostkey_verify=False
        ) as m:
            netconf_reply = m.edit_config(target='running', config=netconf_config)
            xml_data = netconf_reply.xml
            print(xml_data)
            if '<ok/>' in xml_data:
                sendtexttowebex.send_message_webex(roomIdToGetMessages, ACCESS_TOKEN, "Loopback created successfully")
    except Exception as e:
        sendtexttowebex.send_message_webex(roomIdToGetMessages, ACCESS_TOKEN, f"Error: {e}")



def delete(student_id, router_ip, roomIdToGetMessages, ACCESS_TOKEN):
    netconf_config = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback operation="delete">
                    <name>{student_id}</name>
                </Loopback>
            </interface>
        </native>
    </config>
    """


    try:
        # ใช้ router_ip ที่ส่งเข้ามา
        with manager.connect(
            host=router_ip,
            port=830,
            username="admin",
            password="cisco",
            hostkey_verify=False
        ) as m:
            netconf_reply = m.edit_config(target='running', config=netconf_config)
            xml_data = netconf_reply.xml
            print(xml_data)
            if '<ok/>' in xml_data:
                sendtexttowebex.send_message_webex(roomIdToGetMessages, ACCESS_TOKEN, "Loopback delet successfully")
    except Exception as e:
        sendtexttowebex.send_message_webex(roomIdToGetMessages, ACCESS_TOKEN, f"Error: {e}")



# def disable():
#     netconf_config = """<!!!REPLACEME with YANG data!!!>"""

#     try:
#         netconf_reply = netconf_edit_config(netconf_config)
#         xml_data = netconf_reply.xml
#         print(xml_data)
#         if '<ok/>' in xml_data:
#             return "<!!!REPLACEME with proper message!!!>"
#     except:
#         print("Error!")

# def netconf_edit_config(netconf_config):
#     return  m.<!!!REPLACEME with the proper Netconf operation!!!>(target="<!!!REPLACEME with NETCONF Datastore!!!>", config=<!!!REPLACEME with netconf_config!!!>)


# def status():
#     netconf_filter = """<!!!REPLACEME with YANG data!!!>"""

#     try:
#         # Use Netconf operational operation to get interfaces-state information
#         netconf_reply = m.<!!!REPLACEME with the proper Netconf operation!!!>(filter=<!!!REPLACEME with netconf_filter!!!>)
#         print(netconf_reply)
#         netconf_reply_dict = xmltodict.<!!!REPLACEME with the proper method!!!>(netconf_reply.xml)

#         # if there data return from netconf_reply_dict is not null, the operation-state of interface loopback is returned
#         if <!!!REPLACEME with the proper condition!!!>:
#             # extract admin_status and oper_status from netconf_reply_dict
#             admin_status = <!!!REPLACEME!!!>
#             oper_status = <!!!REPLACEME !!!>
#             if admin_status == 'up' and oper_status == 'up':
#                 return "<!!!REPLACEME with proper message!!!>"
#             elif admin_status == 'down' and oper_status == 'down':
#                 return "<!!!REPLACEME with proper message!!!>"
#         else: # no operation-state data
#             return "<!!!REPLACEME with proper message!!!>"
#     except:
#        print("Error!")
