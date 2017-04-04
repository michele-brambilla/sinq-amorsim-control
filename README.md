# sinq-amorsim-control

Naive python UI to handle sinq-amorsim and kafka-to-nexus integration tests.

## Requirements

Python modules:

	* Tkinter
	* socket
	* kafka-python
	* re

## Usage

### Kafka-to-NeXus
	This frame sends commands to the kafka-to-nexus filewriter via a kafka topic.

	* insert the `command-broker` string in the form //[broker]:[port]/[topic]. Default values are

> broker: ess01.psi.ch
> port: 9092
> topic: kakfa-to-nexus.command
	
	* select the command file (JSON format)
	* submit the command from file
	* send the exit command using the `Stop` button
	
Note that multiple commands can be sent repeating the open and submit procedure.

### EL737 counterbox
	This frame starts and handles the sinq-amorsim simulation via the el737 counterbox.
	
	* insert the `host` and `port` where the counterbox is running
	* type the command to be set to the counterbox and Submit (or press enter)
	* the command hisotry is shown on the right hand side
	
The command sequence protocol starts with:

> rmt 1
> echo 2 [//<broker address>:<port>/topic]

Furthermore commands `rt` (rate) and `st` (stop) directly control the event generator.

## Authors
	
	* Michele Brambilla <michele.brambilla@psi.ch>

