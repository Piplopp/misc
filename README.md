This repo contains all random things I'm doing, some are usefull some aren't
This README also contain several oneliners used time to time

# Scripts
## Dictannabinol.py
Python object reminder, long time no object in python
Python dict-like class that forgets things. I need to rename this...
This script is based on [https://github.com/gitpan/Tie-Hash-Cannabinol](https://github.com/gitpan/Tie-Hash-Cannabinol)

## Functions\_automatic\_Integration\_roxygen\_doc
Python3; automatic generation for some part of roxygen documentation
See inside for more details

# Oneliners
===
**Concat files without their 1st line**
```bash
find . -name "*.txt" | xargs -n 1 tail -n +2 > outfile
```
