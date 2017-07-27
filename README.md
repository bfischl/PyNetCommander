# PyNetCommander
Execute scheduled tasks on many computers, regardless of Operating System.
Flexibly create your own task libraries.

The purpose of this program is to simulate user interaction in a dynamic forensics testing environment.
v0.01 Basic Tasks

* openfile
* exec_cmd
* download_file
* visit_site

## Master
Maintains a roster of minions and their individual tasks. Maintains the results of
past tasks.

## Minion
Each minion must first register with the master and register its capabilities.
The master replies with initial configurations including poll delay.