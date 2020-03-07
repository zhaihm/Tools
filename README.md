# Tools
Some useful tools for system management.

### rmfile
**Options**

* `-r` file to remove
* `-d` remove matched directory
* `-t` specify a time to compare time
* `-l` remove modified later than specified time, default ealier

**Usage**

* `rmfile.py -r [filename]`
* `rmfile.py -r [filename] -d`
* `rmfile.py -t [time] -l`
* `rmfile.py -r [filename] -t [time]`