# Detecting High Floating-Point Errors vis Ranking Analysis

## Setup
Install the [docker](https://www.docker.com/). Here are some guides for install [docker for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [docker for MacOS](https://docs.docker.com/docker-for-mac/install/)


Pull the docker image of RADE artifact and create, run the RADE container

```
$ docker pull star09/rade:apsec2022   
$ docker run -ti --name=rade -v PATH:/home/projects star09/rade:apsec2022   /bin/zsh 
```

Clone this repo to /home/projects:
```
$ git clone https://github.com/yixin-09/RADE.git
```

## Run for RADE and DEMC

Run the script under RADE to replicate experiments in paper:
```
./test.sh cpus repeats
```
where cpus and repeats are integers to set the number of cpu you want to use and the number of repeat for each methods, we set cpus and repeats as 20 and 100 in our paper, i.e.,

```
./test.sh 20 100
```

## Run for ATOM

Install ATOM according to [ATOM]{https://github.com/FP-Analysis/atomic-condition}

Copy "oracleMpmath.py" from RADE/src/oracleMpmath.py to replace atomic-condition/script to help save results of ATOM.

```
cp PATH/RADE/src/oracleMpmath.py    PATH/atomic-condition/script
```

Copy "atomic_test.py" from RADE/src/atomic_test.py to atomic-condition:

```
cp  PATH/RADE/src/atomic_test.py    PATH/atomic-condition
```
Run atomic_test.py under ATOM path

```
python atomic_test.py
```

Copy outs from ATOM to RADE
```
cp -r outs PATH/RADE/experiments/detecting_results/ATOM
```


## Results analysis

Run results_analysis.py script to analysis results:
```
python results_analysis.py
```
Main results (Table III and IV) will store in :
```
RADE/experiments/res_table.xls
```
Run 
```
python search_around_atomu.py
```
To get results for Table II:
```
RADE/experiments/atom_tab.xls
```

All results in our paper can be found under PATH/RADE/experiments/paperdate.



