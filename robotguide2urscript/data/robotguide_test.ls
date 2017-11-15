/PROG  CONTOUR_ECROU
/ATTR
OWNER		= MNEDITOR;
COMMENT		= "SimPRO Auto-Gen";
PROG_SIZE	= 1498;
CREATE		= DATE 16-02-17  TIME 13:54:00;
MODIFIED	= DATE 16-02-17  TIME 14:05:54;
FILE_NAME	= ;
VERSION		= 0;
LINE_COUNT	= 26;
MEMORY_SIZE	= 1766;
PROTECT		= READ_WRITE;
TCD:  STACK_SIZE	= 0,
      TASK_PRIORITY	= 50,
      TIME_SLICE	= 0,
      BUSY_LAMP_OFF	= 0,
      ABORT_REQUEST	= 0,
      PAUSE_REQUEST	= 0;
DEFAULT_GROUP	= 1,*,*,*,*;
CONTROL_CODE	= 00000000 00000000;
/MN
   1:  !SimPRO Auto-Generated TPP ;
   2:  !boulon, contour ecrou ;
   3:   ;
   4:  UFRAME_NUM[GP1]=1 ;
   5:  UTOOL_NUM[GP1]=4 ;
   6:  !Feature Approach ;
   7:J P[1] 100% CNT100    ;
   8:   ;
   9:  !Segment1 ;
  10:  PR[1,3]=50    ;
  11:J P[2] 100% FINE    ;
  12:L P[3] 50mm/sec CNT100    ;
  13:L P[4] 50mm/sec CNT100    ;
  14:L P[5] 50mm/sec CNT100    ;
  15:L P[6] 50mm/sec CNT100    ;
  16:L P[7] 50mm/sec CNT100    ;
  17:L P[8] 50mm/sec CNT100    ;
  18:L P[9] 50mm/sec CNT100    ;
  19:L P[10] 50mm/sec CNT100    ;
  20:L P[11] 50mm/sec CNT100    ;
  21:L P[12] 50mm/sec CNT100    ;
  22:L P[13] 50mm/sec CNT100    ;
  23:L P[14] 50mm/sec CNT100    ;
  24:L P[15] 50mm/sec FINE    ;
  25:  !Feature Retreat ;
  26:L P[16] 2000mm/sec CNT100    ;
/POS
P[1]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   758.742  mm,	Y =  1211.896  mm,	Z =   338.375  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =   179.270 deg
};
P[2]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   758.078  mm,	Y =  1159.805  mm,	Z =    42.933  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =   179.270 deg
};
P[3]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   756.706  mm,	Y =  1052.119  mm,	Z =    42.933  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =   179.270 deg
};
P[4]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   711.247  mm,	Y =  1003.713  mm,	Z =    42.933  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =   134.270 deg
};
P[5]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   676.571  mm,	Y =   969.910  mm,	Z =    42.933  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =   134.270 deg
};
P[6]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   595.430  mm,	Y =   968.014  mm,	Z =    42.931  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =    89.270 deg
};
P[7]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   561.777  mm,	Y =   968.443  mm,	Z =    42.931  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =    89.270 deg
};
P[8]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   512.456  mm,	Y =  1014.838  mm,	Z =    42.931  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =    44.270 deg
};
P[9]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   479.566  mm,	Y =  1048.576  mm,	Z =    42.931  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =    44.270 deg
};
P[10]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   477.470  mm,	Y =  1113.736  mm,	Z =    42.929  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =     -.730 deg
};
P[11]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   478.100  mm,	Y =  1163.373  mm,	Z =    42.933  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =     -.730 deg
};
P[12]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   558.235  mm,	Y =  1245.582  mm,	Z =    42.933  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =   -45.730 deg
};
P[13]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   673.030  mm,	Y =  1247.048  mm,	Z =    42.933  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =   -90.730 deg
};
P[14]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   716.280  mm,	Y =  1206.877  mm,	Z =    42.933  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =  -135.730 deg
};
P[15]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   755.240  mm,	Y =  1166.913  mm,	Z =    42.931  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =  -135.730 deg
};
P[16]{
   GP1:
	UF : 1, UT : 4,		CONFIG : 'N U T, 0, 0, 0',
	X =   718.875  mm,	Y =  1204.216  mm,	Z =   338.373  mm,
	W =  -170.000 deg,	P =     0.000 deg,	R =  -135.730 deg
};
/END
