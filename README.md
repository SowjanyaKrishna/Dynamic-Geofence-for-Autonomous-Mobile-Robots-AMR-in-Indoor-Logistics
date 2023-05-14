# Dynamic-Geofence-for-Autonomous-Transport-Robots-AGV-in-Indoor-Logistics
Developed a novel approach based on computational geometry to create dynamic geofences for AGVs.

New concepts and technologies, ranging from manufacturing to intralogistics and
transportation, are required to kickstart the intelligent factory. Mobile robots in industry,
autonomous vehicles in transportation and logistics, IIoT, and augmented reality are
already being explored. All of this, however, necessitates that today's networks soon hit
their limitations. Industrial 5G's exceptional dependability and reduced latency times, as
well as its full IIoT connection, open the way for trend-setting industrial applications.
One of the most important application is identification and eradication of possible
dangers, as well as the documenting of evidence for safety cases, are critical to system
safety. This is usually done during the design and development phase of the system.
During the operating phase of automated systems, however, there is a need to cope with
unknowns and uncertainties. This project focuses on virtual borders surrounding
geographic zones (i.e., geofences) that may be used as an active countermeasure for
dynamic risk management in automated transportation and production environments.
In this paper, a proposal is made for a communication framework capable of connecting
to the existing geofencing system to further add dynamic geofence functionalities. To
implement this, a novel approach based on computational geometrics is built. The
experiments determine how factors such as (Automated Guided Vehicles) AGV speeds,
tag transmission, software and AGV capabilities affect the geofence around it. This
research describes how this approach could be used to create a safety case for the AGV
operation

## Objective 
The goal of this project is to create and construct a system that allows dynamic
protection zones to be formed using geofences or spatial points. Static geofences can
already be defined using an existing system. The system in this thesis will interface
with an existing system using MQTT in order to acquire spatial points that construct
static geofences. The updated system will be able to alter these geographical
locations, add additional geofences, and enlarge or shrink geofence based on the
activity of the AGV. A user interface with appropriate functionality is created for these
operations.

## Geofence

A geofence is a virtual perimeter for a real-world geographic area. A geo-fence could
be dynamically generated or match a predefined set of boundaries. The use of a
geofence is called geofencing, and one example of use involves a location-aware
device of a location-based service (LBS) user entering or exiting a geo-fence. This
activity could trigger an alert to the device's user as well as messaging to the geo-fence
operator.The geofences can serve as a countermeasure that could either eliminate the encountered
hazards or reduce the risk of a mishap to an acceptable level. Geofencing is a
virtual boundary (shape and dimension) defined for each zone (e.g., loading, unloading
and transportation zones etc.) [5]. Within the geofencing zone, the mobile robots are
constantly monitored. Geometric shapes can be created in site zones in order to
establish virtual borders around geographic zones (i.e. geofences).

## System Architecture 

![image](https://github.com/SowjanyaKrishna/Dynamic-Geofence-for-Autonomous-Transport-Robots-AGV-in-Indoor-Logistics/assets/128833366/4d8bcbd3-af32-4f0e-b374-d9173f7a3fe1)


In above Figure, the implemented architecture can be seen with all modules defined. The
backend module is implemented in Flask python framework. All the communication
towards the remaining modules is initiated through this module. The database used is
SQLite as a backend database. The client side (User interface) is implemented on
Vuejs. The user input from the frontend is communicated to the SQLite database using
the library SQLAchemy which enables Object-Relational Mapping (ORM). ORM is
used for data conversion between two incompatible applications. This practically
means that the operations done on SQLite data base can be initiated from flask using
Python queries. This speeds up the process of converting SQL queries into python.
NAiSE GUI rendered from NAiSE server which provides as 3D map of the ARENA with real-time movements of the AGV’s, Tags and with a feature to draw polygon shaped
geofences. The AGV’s (Rexroth active shuttle) communicate to the NAiSE server, an
MQTT broker is implemented as communication protocol to enable bidirectional
communication.
