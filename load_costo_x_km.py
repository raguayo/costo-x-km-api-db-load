import requests
import json
import pymysql.cursors
from datetime import datetime
from ast import literal_eval
from pprint import pprint

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "costxkm"
DB_CHARSET = "utf8mb4"


def add_devices(cursor):
    DEVICE_URL = "http://gps.nextop.vip/api/devices"
    DEVICE_PARAMS = {"all":"true"}

    #retrieve devices from restful get request to nextop api
    response_device = requests.get(DEVICE_URL, DEVICE_PARAMS, auth=('nextop','nextop123'))
    json_device = response_device.json()
    # pprint(json_device)
    num_devices_added = 0;

    # id = 0
    # name = ""
    # uniqueId = ""
    # status = ""
    # diabled = 0
    # lastUpdate = None
    # dtm_last_update = None
    # positionId = 0
    # groupId = 0;
    # phone = ""
    # model = ""
    # contact = ""
    # category = ""
    # geofenceIds = ""
    # attributes = None

    for device in json_device:
        device_dictionary = {};
        for key, value in device.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                device_dictionary['id'] = value
                # id = value
            elif key == 'name':
                device_dictionary['name'] = value
                # name = value
            elif key == 'uniqueId':
                device_dictionary['uniqueId'] = value
                # uniqueId = value
            elif key == 'status':
                device_dictionary['status'] = value
                # status = value
            elif key == 'disabled':
                device_dictionary['disabled'] = value
                # disabled = value
            elif key == 'lastUpdate':
                device_dictionary['lastUpdate'] = value

                # str_last_update = value
                # dtm_last_update_full = datetime.strptime(str_last_update, '%Y-%m-%dT%H:%M:%S.%f%z')
                # dtm_last_update_no_tz = dtm_last_update_full.replace(tzinfo=None)
                # str_last_update = dtm_last_update_no_tz.strftime('%Y-%m-%d %H:%M:%S')
                # dtm_last_update = datetime.strptime(str_last_update, '%Y-%m-%d %H:%M:%S')

            elif key == 'positionId':
                device_dictionary['positionId'] = value
                # positionId = value
            elif key == 'groupId':
                device_dictionary['groupId'] = value
                # groupId = value
            elif key == 'phone':
                device_dictionary['phone'] = value
                # phone = value
            elif key == 'model':
                device_dictionary['model'] = value
                # model = value
            elif key == 'contact':
                device_dictionary['contact'] = value
                # contact = value
            elif key == 'category':
                device_dictionary['category'] = value
                # category = value
            elif key == 'geofenceIds':
                device_dictionary['geofenceIds'] = value
                # geofenceIds = value
            elif key == 'attributes':
                device_dictionary['attributes'] = value

            # pprint(device_dictionary.get("name"))

        # str_last_update = device_dictionary.get("lastUpdate")
        # dtm_last_update_full = datetime.strptime(str_last_update, '%Y-%m-%dT%H:%M:%S.%f%z')
        # dtm_last_update_no_tz = dtm_last_update_full.replace(tzinfo=None)
        # str_last_update = dtm_last_update_no_tz.strftime('%Y-%m-%d %H:%M:%S')
        # dtm_last_update = datetime.strptime(str_last_update, '%Y-%m-%d %H:%M:%S')
        # print("dtm_last_update = ", dtm_last_update)
        # print("type(dtm_last_update) = ", type(dtm_last_update))

        # print("dtm_last_update = ", dtm_last_update)

        add_device = """INSERT INTO `device`(`id`, `name`, `uniqueId`, `status`, `disabled`, `lastUpdate`, `positionId`, `groupId`, `phone`, `model`, `contact`, `category`, `geofenceIds`, `attributes`) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""

        # insert_device = """INSERT INTO device(id, name, uniqueId, status, disabled, lastUpdate, positionId, groupId, phone, model, contact, category, geofenceIds) VALUES(id, name, uniqueId, status, disabled, dtm_last_update, positionId, groupId, phone, model, contact, category, geofenceIds)"""


        data_device = (device_dictionary.get("id"), device_dictionary.get("name"), device_dictionary.get("uniqueId"), device_dictionary.get("status"), device_dictionary.get("disabled"), device_dictionary.get("lastUpdate"), device_dictionary.get("positionId"), device_dictionary.get("groupId"), device_dictionary.get("phone"), device_dictionary.get("model"), device_dictionary.get("contact"), device_dictionary.get("category"), device_dictionary.get("geofenceIds"), device_dictionary.get("attributes"))

        # insert a new device
        num_devices_added += cursor.execute(add_device, data_device)
    if num_devices_added > 0:
        print("Successfully added " + str(num_devices_added) + " device row(s).")
    else:
        print("No data returned from API so no device rows added.")
        # num_devices_added += cursor.execute(insert_device)
    # print("Successfully added " + str(num_devices_added) + " device row.")

def add_statistics(cursor):
    STATISTICS_URL= "http://gps.nextop.vip/api/statistics"
    statistics_from = "2018-10-22T18:30:00Z"
    statistics_to = "2018-12-02T18:30:00Z"
    STATISTICS_PARAMS = {'from':statistics_from, 'to':statistics_to}

    #retrieve statistics from restful get request to nextop api
    response_statistics = requests.get(STATISTICS_URL, STATISTICS_PARAMS, auth=('nextop','nextop123'))
    json_statistics = response_statistics.json()
    # pprint(json_statistics)
    num_stats_added = 0;

    for statistic in json_statistics:
        statistic_dictionary = {};
        for key, value in statistic.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                statistic_dictionary['id'] = value
            elif key == 'activeDevices':
                statistic_dictionary['activeDevices'] = value
            elif key == 'activeUsers':
                statistic_dictionary['activeUsers'] = value
            elif key == 'captureTime':
                statistic_dictionary['captureTime'] = value
            elif key == 'geocoderRequests':
                statistic_dictionary['geocoderRequests'] = value
            elif key == 'geolocationRequests':
                statistic_dictionary['geolocationRequests'] = value
            elif key == 'mailSent':
                statistic_dictionary['mailSent'] = value
            elif key == 'messagesReceived':
                statistic_dictionary['messagesReceived'] = value
            elif key == 'messagesStored':
                statistic_dictionary['messagesStored'] = value
            elif key == 'requests':
                statistic_dictionary['requests'] = value
            elif key == 'smsSent':
                statistic_dictionary['smsSent'] = value

            # pprint(statistic_dictionary.get("activeDevices"))

        add_statistic = """INSERT INTO statistic(id, captureTime, activeUsers, activeDevices, requests, messagesReceived, messagesStored, geocoderRequests, geolocationRequests, mailSent, smsSent) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""

        data_statistic = (statistic_dictionary.get("id"), statistic_dictionary.get("captureTime"), statistic_dictionary.get("activeUsers"), statistic_dictionary.get("activeDevices"), statistic_dictionary.get("requests"), statistic_dictionary.get("messagesReceived"), statistic_dictionary.get("messagesStored"), statistic_dictionary.get("geocoderRequests"), statistic_dictionary.get("geolocationRequests"), statistic_dictionary.get("mailSent"), statistic_dictionary.get("smsSent"))

        # insert a new statistic
        num_stats_added += cursor.execute(add_statistic, data_statistic)
    if num_stats_added > 0:
        print("Successfully added " + str(num_stats_added) + " statistic row(s).")
    else:
        print("No data returned from API so no statistic rows added.")

def add_attributes(cursor):
    ATTRIBUTES_URL= "http://gps.nextop.vip/api/attributes/computed"
    ATTRIBUTES_PARAMS = {"all":"true"}

    #retrieve attributes from restful get request to nextop api
    response_attributes = requests.get(ATTRIBUTES_URL, ATTRIBUTES_PARAMS, auth=('nextop','nextop123'))
    json_attributes = response_attributes.json()
    # pprint(json_attributes)
    num_attributes_added = 0;

    for attribute in json_attributes:
        attribute_dictionary = {};
        for key, value in attribute.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                attribute_dictionary['id'] = value
            elif key == 'description':
                attribute_dictionary['description'] = value
            elif key == 'attribute':
                attribute_dictionary['attribute'] = value
            elif key == 'expression':
                attribute_dictionary['expression'] = value
            elif key == 'type':
                attribute_dictionary['type'] = value

            # pprint(attribute_dictionary.get("attribute"))

        add_attribute = """INSERT INTO attribute(id, description, attribute, expression, type) VALUES("%s", "%s", "%s", "%s", "%s")"""

        data_attribute = (attribute_dictionary.get("id"), attribute_dictionary.get("description"), attribute_dictionary.get("attribute"), attribute_dictionary.get("expression"), attribute_dictionary.get("type"))

        # insert a new attribute
        num_attributes_added += cursor.execute(add_attribute, data_attribute)
    if num_attributes_added > 0:
        print("Successfully added " + str(num_attributes_added) + " attribute row(s).")
    else:
        print("No data returned from API so no attribute rows added.")

def add_calendars(cursor):
    CALENDARS_URL= "http://gps.nextop.vip/api/calendars"
    CALENDARS_PARAMS = {"all":"true"}

    #retrieve calendars from restful get request to nextop api
    response_calendars = requests.get(CALENDARS_URL, CALENDARS_PARAMS, auth=('nextop','nextop123'))
    json_calendars = response_calendars.json()
    # pprint(json_calendars)
    num_calendars_added = 0;

    for calendar in json_calendars:
        calendar_dictionary = {};
        for key, value in calendar.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                calendar_dictionary['id'] = value
            elif key == 'name':
                calendar_dictionary['name'] = value
            elif key == 'data':
                calendar_dictionary['data'] = value

            # pprint(calendar_dictionary.get("name"))

        add_calendar = """INSERT INTO calendar(id, name, data) VALUES("%s", "%s", "%s")"""

        data_calendar = (calendar_dictionary.get("id"), calendar_dictionary.get("name"), calendar_dictionary.get("data"))

        # insert a new calendar
        num_calendars_added += cursor.execute(add_calendar, data_calendar)
    if num_calendars_added > 0:
        print("Successfully added " + str(num_calendars_added) + " calendar row(s).")
    else:
        print("No data returned from API so no calendar rows added.")

def add_commands(cursor):
    COMMANDS_URL= "http://gps.nextop.vip/api/commands"
    COMMANDS_PARAMS = {"all":"true"}

    #retrieve commands from restful get request to nextop api
    response_commands = requests.get(COMMANDS_URL, COMMANDS_PARAMS, auth=('nextop','nextop123'))
    json_commands = response_commands.json()
    # pprint(json_commands)
    num_commands_added = 0;

    for command in json_commands:
        command_dictionary = {};
        for key, value in command.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                command_dictionary['id'] = value
            elif key == 'deviceId':
                command_dictionary['deviceId'] = value
            elif key == 'description':
                command_dictionary['description'] = value
            elif key == 'type':
                command_dictionary['type'] = value

            # pprint(command_dictionary.get("description"))

        add_command = """INSERT INTO command(id, deviceId, description, type) VALUES("%s", "%s", "%s", "%s")"""

        data_command = (command_dictionary.get("id"), command_dictionary.get("deviceId"), command_dictionary.get("description"), command_dictionary.get("type"))

        # insert a new command
        num_commands_added += cursor.execute(add_command, data_command)
    if num_commands_added > 0:
        print("Successfully added " + str(num_commands_added) + " command row(s).")
    else:
        print("No data returned from API so no command rows added.")

def add_command_types(cursor):
    COMMAND_TYPES_URL= "http://gps.nextop.vip/api/commands/types"

    #retrieve command types from restful get request to nextop api
    response_command_types = requests.get(COMMAND_TYPES_URL, auth=('nextop','nextop123'))
    json_command_types = response_command_types.json()
    # pprint(json_command_types)
    num_command_types_added = 0;

    for command_type in json_command_types:
        command_type_dictionary = {};
        for key, value in command_type.items():
            #print(str(key) + ": " + str(value))
            if key == 'type':
                command_type_dictionary['type'] = value
            # pprint(command_type_dictionary.get("type"))

        add_command_type = """INSERT INTO command_type(type) VALUES("%s")"""

        data_command_type = (command_type_dictionary.get("type"))

        # insert a new command type
        num_command_types_added += cursor.execute(add_command_type, data_command_type)
    if num_command_types_added > 0:
        print("Successfully added " + str(num_command_types_added) + " command type row(s).")
    else:
        print("No data returned from API so no command type rows added.")

def add_drivers(cursor):
    DRIVERS_URL= "http://gps.nextop.vip/api/drivers"
    DRIVERS_PARAMS = {"all":"true"}

    #retrieve drivers from restful get request to nextop api
    response_drivers = requests.get(DRIVERS_URL, DRIVERS_PARAMS, auth=('nextop','nextop123'))
    json_drivers = response_drivers.json()
    # pprint(json_drivers)
    num_drivers_added = 0;

    for driver in json_drivers:
        driver_dictionary = {};
        for key, value in driver.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                driver_dictionary['id'] = value
            elif key == 'name':
                driver_dictionary['name'] = value
            elif key == 'uniqueId':
                driver_dictionary['uniqueId'] = value

            # pprint(driver_dictionary.get("name"))

        add_driver = """INSERT INTO driver(id, name, uniqueId) VALUES("%s", "%s", "%s")"""

        data_driver = (driver_dictionary.get("id"), driver_dictionary.get("name"), driver_dictionary.get("uniqueId"))

        # insert a new driver
        num_drivers_added += cursor.execute(add_driver, data_driver)
    if num_drivers_added > 0:
        print("Successfully added " + str(num_drivers_added) + " driver row(s).")
    else:
        print("No data returned from API so no driver rows added.")

def add_geofences(cursor):
    GEOFENCES_URL= "http://gps.nextop.vip/api/geofences"
    GEOFENCES_PARAMS = {"all":"true"}

    #retrieve geofences from restful get request to nextop api
    response_geofences = requests.get(GEOFENCES_URL, GEOFENCES_PARAMS, auth=('nextop','nextop123'))
    json_geofences = response_geofences.json()
    # pprint(json_geofences)
    num_geofences_added = 0;

    for geofence in json_geofences:
        geofence_dictionary = {};
        for key, value in geofence.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                geofence_dictionary['id'] = value
            elif key == 'name':
                geofence_dictionary['name'] = value
            elif key == 'description':
                geofence_dictionary['description'] = value
            elif key == 'area':
                geofence_dictionary['area'] = value
            elif key == 'calendarId':
                geofence_dictionary['calendarId'] = value

            # pprint(geofence_dictionary.get("name"))

        add_geofence = """INSERT INTO geofence(id, name, description, area, calendarId) VALUES("%s", "%s", "%s", "%s", "%s")"""

        data_geofence = (geofence_dictionary.get("id"), geofence_dictionary.get("name"), geofence_dictionary.get("description"), geofence_dictionary.get("area"), geofence_dictionary.get("calendarId"))

        # insert a new geofence
        num_geofences_added += cursor.execute(add_geofence, data_geofence)
    if num_geofences_added > 0:
        print("Successfully added " + str(num_geofences_added) + " geofence row(s).")
    else:
        print("No data returned from API so no geofence rows added.")

def add_groups(cursor):
    GROUPS_URL= "http://gps.nextop.vip/api/groups"
    GROUPS_PARAMS = {"all":"true"}

    #retrieve groups from restful get request to nextop api
    response_groups = requests.get(GROUPS_URL, GROUPS_PARAMS, auth=('nextop','nextop123'))
    json_groups = response_groups.json()
    # pprint(json_groups)
    num_groups_added = 0;

    for group in json_groups:
        group_dictionary = {};
        for key, value in driver.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                group_dictionary['id'] = value
            elif key == 'name':
                group_dictionary['name'] = value
            elif key == 'groupId':
                group_dictionary['groupId'] = value

            # pprint(driver_dictionary.get("name"))

        add_group = """INSERT INTO group(id, name, groupId) VALUES("%s", "%s", "%s")"""

        data_group = (group_dictionary.get("id"), group_dictionary.get("name"), group_dictionary.get("groupId"))

        # insert a new group
        num_groups_added += cursor.execute(add_group, data_group)
    if num_groups_added > 0:
        print("Successfully added " + str(num_groups_added) + " group row(s).")
    else:
        print("No data returned from API so no group rows added.")

def add_maintenances(cursor):
    MAINTENANCE_URL= "http://gps.nextop.vip/api/maintenances"
    MAINTENANCE_PARAMS = {"all":"true"}

    #retrieve maintenances from restful get request to nextop api
    response_maintenances = requests.get(MAINTENANCE_URL, MAINTENANCE_PARAMS, auth=('nextop','nextop123'))
    json_maintenances = response_maintenances.json()
    # pprint(json_maintenances)
    num_maintenances_added = 0;

    for maintennce in json_maintenances:
        maintenance_dictionary = {};
        for key, value in maintenance.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                maintenance_dictionary['id'] = value
            elif key == 'name':
                maintenance_dictionary['name'] = value
            elif key == 'type':
                maintenance_dictionary['type'] = value
            elif key == 'start':
                maintenance_dictionary['start'] = value
            elif key == 'period':
                maintenance_dictionary['period'] = value

            # pprint(data_maintenance.get("name"))

        add_maintenance = """INSERT INTO maintenance(id, name, type, start, period) VALUES("%s", "%s", "%s", "%s", "%s")"""

        data_maintenance = (maintenance_dictionary.get("id"), maintenance_dictionary.get("name"), maintenance_dictionary.get("type"), maintenance_dictionary.get("start"), maintenance_dictionary.get("period"))

        # insert a new maintenance
        num_maintenances_added += cursor.execute(add_maintenance, data_maintenance)
    if num_maintenances_added > 0:
        print("Successfully added " + str(num_maintenances_added) + " maintenance row(s).")
    else:
        print("No data returned from API so no maintenance rows added.")

def add_notifications(cursor):
    NOTIFICATIONS_URL= "http://gps.nextop.vip/api/notifications"
    NOTIFICATIONS_PARAMS = {'all':'true'}

    #retrieve notifications from restful get request to nextop api
    response_notifications = requests.get(NOTIFICATIONS_URL, NOTIFICATIONS_PARAMS, auth=('nextop','nextop123'))
    json_notifications = response_notifications.json()
    # pprint(json_notifications)
    num_notifications_added = 0;

    for notification in json_notifications:
        notification_dictionary = {};
        for key, value in notification.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                notification_dictionary['id'] = value
            elif key == 'type':
                notification_dictionary['type'] = value
            elif key == 'notificators':
                # print("notificators key with value(s): ", value)
                # trim whitespace, parse by comma separated
                str_notifications = value.strip()
                notifications_list = str_notifications.split(",")
                notification_dictionary["web"] = 0
                notification_dictionary["mail"] = 0
                notification_dictionary["sms"] = 0
                for alert in notifications_list:
                    print("alert -> ", alert)
                    if alert == "web":
                        notification_dictionary['web'] = 1
                    if alert == "mail":
                        notification_dictionary['mail'] = 1
                    if alert == "sms":
                        notification_dictionary["sms"] = 1
            elif key == 'always':
                notification_dictionary['always'] = value
            elif key == 'calendarId':
                notification_dictionary['calendarId'] = value

            # pprint(notification_dictionary.get("type"))

        add_notification = """INSERT INTO notification(id, type, always, web, mail, sms, calendarId) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s")"""

        data_notification = (notification_dictionary.get("id"), notification_dictionary.get("type"), notification_dictionary.get("always"), notification_dictionary.get("web"), notification_dictionary.get("mail"), notification_dictionary.get("sms"), notification_dictionary.get("calendarId"))

        # insert a new statistic
        num_notifications_added += cursor.execute(add_notification, data_notification)
    if num_notifications_added > 0:
        print("Successfully added " + str(num_notifications_added) + " notification row(s).")
    else:
        print("No data returned from API so no notification rows added.")

def add_notification_types(cursor):
    NOTIFICATION_TYPES_URL= "http://gps.nextop.vip/api/notifications/types"

    #retrieve notification types from restful get request to nextop api
    response_notification_types = requests.get(NOTIFICATION_TYPES_URL, auth=('nextop','nextop123'))
    json_notification_types = response_notification_types.json()
    pprint(json_notification_types)
    num_notification_types_added = 0;

    for notification_type in json_notification_types:
        notification_type_dictionary = {};
        for key, value in notification_type.items():
            #print(str(key) + ": " + str(value))
            if key == 'type':
                notification_type_dictionary['type'] = value
            # pprint(notification_type_dictionary.get("type"))

        add_notification_type = """INSERT INTO notification_type(type) VALUES("%s")"""

        data_notification_type = (notification_type_dictionary.get("type"))

        # insert a new notification type
        num_notification_types_added += cursor.execute(add_notification_type, data_notification_type)
    if num_notification_types_added > 0:
        print("Successfully added " + str(num_notification_types_added) + " notification type row(s).")
    else:
        print("No data returned from API so no notification type rows added.")

def add_positions(cursor):
    POSITION_URL = "http://gps.nextop.vip/api/positions"

    #retrieve positions from restful get request to nextop api
    response_position = requests.get(POSITION_URL, auth=('nextop','nextop123'))
    json_position = response_position.json()
    # pprint(json_position)
    num_positions_added = 0;

    for position in json_position:
        position_dictionary = {}
        # print("position type: ", type(position))
        for key, value in position.items():
            #print(str(key) + ": " + str(value))
            if key == 'id':
                position_dictionary['id'] = value
            elif key == 'attributes':
                position_dictionary['attributes'] = value

                #TODO: try wrapping open and close brackets around value for json_str and then set to position_dictionary['attributes']
                # json_str = "{"
                # print("attributes value type is: ", type(value))
                # for key, value in value.items():
                #     json_str += "'" + str(key) + "':'" + str(value) + "',"
                    # print("key: ", key, ", value: ", value)
                # json_str += "}"
                # print("json_str = ", json_str)
                # position_dictionary['attributes'] = json_str
                # print("position_dictionary['attributes'] = ", position_dictionary['attributes'])
                # print("type(json_str): ", type(json_str))
            elif key == 'deviceId':
                position_dictionary['deviceId'] = value
            elif key == 'type':
                position_dictionary['type'] = value
            elif key == 'protocol':
                position_dictionary['protocol'] = value
            elif key == 'serverTime':
                position_dictionary['serverTime'] = value
            elif key == 'deviceTime':
                position_dictionary['deviceTime'] = value
            elif key == 'fixTime':
                position_dictionary['fixTime'] = value
            elif key == 'outdated':
                position_dictionary['outdated'] = value
            elif key == 'valid':
                position_dictionary['valid'] = value
            elif key == 'latitude':
                position_dictionary['latitude'] = value
            elif key == 'longitude':
                position_dictionary['longitude'] = value
            elif key == 'altitude':
                position_dictionary['altitude'] = value
            elif key == 'speed':
                position_dictionary['speed'] = value
            elif key == 'course':
                position_dictionary['course'] = value
            elif key == 'address':
                position_dictionary['address'] = value
            elif key == 'accuracy':
                position_dictionary['accuracy'] = value
            elif key == 'network':
                position_dictionary['network'] = value


        add_position = """INSERT INTO `position`(`id`, `attributes`, `deviceId`, `type`, `protocol`, `serverTime`, `deviceTime`, `fixTime`, `outdated`, `valid`, `latitude`, `longitude`, `altitude`, `speed`, `course`, `address`, `accuracy`, `network`) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""

        data_position = (position_dictionary.get("id"), position_dictionary.get("attributes"), position_dictionary.get("deviceId"), position_dictionary.get("type"), position_dictionary.get("protocol"), position_dictionary.get("serverTime"), position_dictionary.get("deviceTime"), position_dictionary.get("fixTime"), position_dictionary.get("outdated"), position_dictionary.get("valid"), position_dictionary.get("latitude"), position_dictionary.get("longitude"), position_dictionary.get("altitude"), position_dictionary.get("speed"), position_dictionary.get("course"), position_dictionary.get("address"), position_dictionary.get("accuracy"), position_dictionary.get("network"))

        # insert a new device
        # num_positions_added += cursor.execute(add_position, data_position)
    if num_positions_added > 0:
        print("Successfully added " + str(num_positions_added) + " position row(s).")
    else:
        print("No data returned from API so no position rows added.")

def add_servers(cursor):
    SERVER_URL = "http://gps.nextop.vip/api/server"
    SERVER_PARAMS = {'all':'true'}

    #retrieve positions from restful get request to nextop api
    response_server = requests.get(SERVER_URL, SERVER_PARAMS, auth=('nextop','nextop123'))
    json_server = response_server.json()
    # pprint(json_server)
    # print("json_server datatype: ", type(json_server))
    num_servers_added = 0;

    server_dictionary = {}
    server = None
    if type(server) == 'dict':
        for server in json_server:
            # print("type(server) = ", type(server))
            for key, value in server.items():
                # print(str(key) + ": " + str(value))
                if key == 'id':
                    server_dictionary['id'] = value
                elif key == 'attributes':
                    server_dictionary['attributes'] = value
                elif key == 'registration':
                    server_dictionary['registration'] = value
                elif key == 'readonly':
                    server_dictionary['readonly'] = value
                elif key == 'deviceReadonly':
                    server_dictionary['deviceReadonly'] = value
                elif key == 'limitCommands':
                    server_dictionary['limitCommands'] = value
                elif key == 'map':
                    server_dictionary['map'] = value
                elif key == 'bingKey':
                    server_dictionary['bingKey'] = value
                elif key == 'mapUrl':
                    server_dictionary['mapUrl'] = value
                elif key == 'poiLayer':
                    server_dictionary['poiLayer'] = value
                elif key == 'latitude':
                    server_dictionary['latitude'] = value
                elif key == 'longitude':
                    server_dictionary['longitude'] = value
                elif key == 'zoom':
                    server_dictionary['zoom'] = value
                elif key == 'twelveHourFormat':
                    server_dictionary['twelveHourFormat'] = value
                elif key == 'version':
                    server_dictionary['version'] = value
                elif key == 'forceSettings':
                    server_dictionary['forceSettings'] = value
                elif key == 'coordinateFormat':
                    server_dictionary['coordinateFormat'] = value
    else:
        server_dictionary['id'] = json_server['id']
        server_dictionary['attributes'] = json_server['attributes']
        server_dictionary['registration'] = json_server['registration']
        server_dictionary['readonly'] = json_server['readonly']
        server_dictionary['deviceReadonly'] = json_server['deviceReadonly']
        server_dictionary['limitCommands'] = json_server['limitCommands']
        server_dictionary['map'] = json_server['map']
        server_dictionary['bingKey'] = json_server['bingKey']
        server_dictionary['mapUrl'] = json_server['mapUrl']
        server_dictionary['poiLayer'] = json_server['poiLayer']
        server_dictionary['latitude'] = json_server['latitude']
        server_dictionary['longitude'] = json_server['longitude']
        server_dictionary['zoom'] = json_server['zoom']
        server_dictionary['twelveHourFormat'] = json_server['twelveHourFormat']
        server_dictionary['version'] = json_server['version']
        server_dictionary['forceSettings'] = json_server['forceSettings']
        server_dictionary['coordinateFormat'] = json_server['coordinateFormat']

    add_server = """INSERT INTO `server`(`id`, `attributes`, `registration`, `readonly`, `deviceReadonly`, `limitCommands`, `map`, `bingKey`, `mapUrl`, `poiLayer`, `latitude`, `longitude`, `zoom`, `twelveHourFormat`, `version`, `forceSettings`, `coordinateFormat`) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""

    data_server = (server_dictionary.get("id"), server_dictionary.get("attributes"), server_dictionary.get("registration"), server_dictionary.get("readonly"), server_dictionary.get("deviceReadonly"), server_dictionary.get("limitCommands"), server_dictionary.get("map"), server_dictionary.get("bingKey"), server_dictionary.get("mapUrl"), server_dictionary.get("poiLayer"), server_dictionary.get("latitude"), server_dictionary.get("longitude"), server_dictionary.get("zoom"), server_dictionary.get("twelveHourFormat"), server_dictionary.get("version"), server_dictionary.get("forceSettings"), server_dictionary.get("coordinateFormat"))

    # insert a new device
    num_servers_added += cursor.execute(add_server, data_server)
    if num_servers_added > 0:
        print("Successfully added " + str(num_servers_added) + " server row(s).")
    else:
        print("No data returned from API so no server rows added.")

try:
    # connect to costxkm db
    cnx = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset=DB_CHARSET, cursorclass=pymysql.cursors.DictCursor)

    # cursor to use for all database inserts
    cursor = cnx.cursor()

    # add_devices(cursor)
    # add_statistics(cursor)
    # add_attributes(cursor)
    # add_calendars(cursor)
    # add_commands(cursor)
    # add_command_types(cursor)
    # add_drivers(cursor)
    # add_geofences(cursor)
    # add_groups(cursor)
    # add_maintenances(cursor)
    # add_notifications(cursor)
    # add_notification_types(cursor)
    # add_positions(cursor)
    add_servers(cursor)

    # commit data to db
    cnx.commit()

except pymysql.InternalError as err:
    code, message = err.args
    print("Code: ", code, ", Message: ", message)
except pymysql.err.IntegrityError as err:
    print("INTEGRITY ERROR! ADDING REDUNDANT DATA IS NOT ALLOWED!!")
    # row already exists so perhaps do an update instead of an add

    # POSSIBLE TODO: CHANGE THIS TO UPDATE BASED ON ACTUAL API PAYLOAD
    # cursor.execute ("""
    #    UPDATE tblTableName
    #    SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s
    #    WHERE Server=%s
    # """, (Year, Month, Day, Hour, Minute, ServerID))

    # update_device = """UPDATE device SET name=%s, uniqueId=%s, status=%s, disabled=%s, lastUpdate=%s, positionId=%s, groupId=%s, phone=%s, model=%s, contact=%s, category=%s, geofenceIds=%s WHERE id = 69"""
    # cursor.execute(update_device)

    # cnx.commit()
finally:
    print("closing cursor...")
    cursor.close()
    print("closing db connection......")
    cnx.close()














def add_table_row(cursor, tablename, rowdict):
    # filter out keys that are not column names
    cursor.execute("describe %s" % tablename)
    allowed_keys = set(row[0] for row in cursor.fethall())
    keys = allowed_keys.intersection(rowdict)

    if len(rowdict) > len(keys):
        unknown_keys = set(rowdict) - allowed_keys
        print >> sys.stderr, "skipping keys:", ", ".join(unknown_keys)

    columns = ", ".join(keys)
    values_template = ", ".join(["%s"] * len(keys))

    sql = "INSERT INTO %s (%s) VALUES (%s)" % (tablename, columns, values_template)
    values = tuple(rowdict[key] for key in keys)
    cursor.execute(sql, values)
