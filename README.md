This repo contains all random things I'm doing, some are usefull some aren't
This README also contain several oneliners used time to time

#### Summary
- [Dictannabinol.py](#dictannabinol)
- [Functions\_automatic\_Integration\_roxygen\_doc](#roxygen)
- [robotguide2urscript](#robotguide2urscript)
- [DMS2DD](#dms2dd)
- [Oneliners](#oneliners)


### Scripts
##### Dictannabinol.py<a name="dictannabinol"></a>
Python object reminder, long time no object in python
Python dict-like class that forgets things. I need to rename this...
This script is based on [https://github.com/gitpan/Tie-Hash-Cannabinol](https://github.com/gitpan/Tie-Hash-Cannabinol)

---
##### Functions\_automatic\_Integration\_roxygen\_doc<a name="roxygen"></a>
Python3; automatic generation for some part of roxygen documentation
See inside for more details

---
#### robotguide2urscript<a name="robotguide2urscript"></a>
Python3; convert robotguide waypoints files to URscript
Quickly done


---
#### DMS2DD<a name="dms2dd"></a>
Python3; transform GPS Degrees Minutes Seconds locations into Decimal Degrees

---

### Oneliners <a name="oneliners"></a>
**Concat files without their 1st line**
```bash
find . -name "*.txt" | xargs -n 1 tail -n +2 > outfile
```

**Extract all columns but the one matching regex**
```awk
awk 'NR==1{for(i=1;i<=NF;i++)if(!($i~/REGEX_HERE:_[kv][0-9]+$/)){a[i]=1;m=i}}{for(i=1;i<=NF;i++)if(a[i])printf "%s%s",$i,(i==m?RS:FS)}' FILE.tsv |column -t
```

**Create N files of size S**
```bash
# Create 20 000 files of size = 1MB; change bs to change size
for i in $(seq 1 20000); do touch $i; dd if=/dev/urandom of=$i bs=1024 count=1024 >/dev/null 2>&1; done
```

**Python, create a test email server that prints mail in terminal instead of sending them**
```bash
# Mail is sent to localhost on port 8025 in this example
python -m smtpd -n -c DebuggingServer localhost:8025
```

**Extract only even/odd lines from a file**
```bash
# even
sed -n '0~2p' file.csv > output.csv
# odd
sed -n '1~2p' file.csv > output.csv
```

**Count number of reads in fasta/fastq files**
```bash
# Fasta
grep '>' file.fasta | wc -l
# Fastq
awk '{lines++}END{print lines/4}' file.fastq
```

**Extract sequences from a fasta based on a list of IDs**
```bash
# Change the value in 'cut' to strip unneccessary characters before your id
cut -c 1- FILE_IDs.TXT | xargs -n 1 samtools faidx FILE.FASTA
```

**Extract specific regions from a fasta file (using bedtools)**
```bash
bedtools getfasta -fi file.fasta -bed file.bed -fo output.fasta -name

# See the bed file format here: https://felixfan.github.io/bedtools/
```

**Rename a tilda (or xterm compatible terminal programs) tab**
```bash
NAME="tab name here"
echo -e  "\e]2;$NAME\a  tab --> [$NAME]"
```

**Create multiple screens to run several commands in it**
```bash
#!/bin/bash
# Run this script with this command: screen -c "./SCRIPT_NAME" && pkill screen
# && pkill screen will just kill all the existing screens once you detach; on macos use pkill SCREEN instead

# split is going to split your window; the -v option is for vertical splitting and only available for screen > 4.01.0
# focus gonna change the focus to the newly created window
# using ;sh as the final bash command will allow you to keep the screen running. Otherwise it will terminate itself once the command is done running

screen -t "YOUR TITLE 1" bash -c "<your bash command>; sh"
split -v
focus
screen -t "YOUR TITLE 2" bash -c "<your bash command>; sh"
split -v
focus
screen -t "YOUR TITLE 3" bash -c "<your bash command>; sh"
split -v
focus
screen -t "YOUR TITLE 4" bash -c "<your bash command>; sh"
```
