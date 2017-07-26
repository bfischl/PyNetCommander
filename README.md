# PyNetCommander
Execute scheduled tasks on many computers, regardless of Operating System.
Flexibly create your own task libraries.

v0.01 Basic Tasks

* ip
* cmd


## Master
Maintains a roster of minions and their individual tasks. Maintains the results of
past tasks.

## Minion
Each minion must first register with the master and register its capabilities.
The master replies with initial configurations including poll delay.