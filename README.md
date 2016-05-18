This repo contains all random things I'm doing, some are usefull some aren't
This README also contain several oneliners used time to time

#### Summary
- [Dictannabinol.py](#dictannabinol)
- [Functions\_automatic\_Integration\_roxygen\_doc](#roxygen)
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

### Oneliners <a name="oneliners"></a>
**Concat files without their 1st line**
```bash
find . -name "*.txt" | xargs -n 1 tail -n +2 > outfile
```

Extract all columns but the one matching regex
`̀``awk
awk 'NR==1{for(i=1;i<=NF;i++)if($i~/_[kv][0-9]+$/){a[i]=1;m=i}}{for(i=1;i<=NF;i++){if(!a[i]){printf "%s%s",$i,(i>m?RS:FS)}}printf "\n"}' FILE.tsv
```
