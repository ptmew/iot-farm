# **Bally** DB Documentation

### PHP QUERY

```http
http://161.246.35.52/cie/pawee/sqltable/test.php?query=[MYSQL_QUERY]
```

###### example with MYSQL_QUERY

```http
http://161.246.35.52/cie/pawee/sqltable/test.php?query=select * from PLANT_STATUS
```



### Info

**user:** *pawee*

**pass:** *CIEkmitl2020$*

**database:** *cie_lab*

**table:** *PLANT STATUS, PLANT_SETTING, USET_SETTING*



### Database Schema

![Bally_DB_Pic](D:\UserData\gitclone\iot-farm\database\Bally_DB_Pic.JPG)

### MySQL Script

#### Create table Sample

```mysql
CREATE TABLE PLANT_STATUS
(
NAME VARCHAR(20) NOT NULL,
TIMESTAMP TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
HUMID FLOAT,
TEMP FLOAT,
PH FLOAT,
EC FLOAT,
O2 FLOAT,
CONSTRAINT Constraint_name PRIMARY KEY (NAME, TIMESTAMP)
);

CREATE TABLE PLANT_SETTING
(
PLANTNAME VARCHAR(20) NOT NULL,
HUMID FLOAT,
TEMP FLOAT,	
PH FLOAT,
EC FLOAT,
O2 FLOAT,
PRIMARY KEY(PLANTNAME)
);

CREATE TABLE USER_SETTING
(
NAME VARCHAR(20) NOT NULL,
PLANTNAME VARCHAR(20) NOT NULL,
PRIMARY KEY(NAME),
FOREIGN KEY (PLANTNAME) REFERENCES PLANT_SETTING(PLANTNAME)
);

```

#### Update data to the tables Sample

```mysql
INSERT INTO `PLANT_SETTING`
(
PLANTNAME,
HUMID,
TEMP,
PH,
EC
) VALUES 
(
"test",
25.00,
35.00,
7.00,
12.00
);

INSERT INTO `USER_SETTING`
(
NAME,
PLANTNAME
) VALUES 
(
"mew",
"test"
);

INSERT INTO `PLANT_STATUS`
(
NAME,
HUMID,
TEMP,
PH,
EC,
O2
) VALUES 
(
"mew",
12.00,
13.00,
14.00,
15.00,
16.00
);
```

