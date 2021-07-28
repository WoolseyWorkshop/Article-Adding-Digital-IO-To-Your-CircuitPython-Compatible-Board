EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr USLetter 11000 8500
encoding utf-8
Sheet 1 1
Title "Generic MCP23017 Interface Circuit"
Date "2021-07-08"
Rev "1.0"
Comp "Woolsey Workshop"
Comment1 "By John Woolsey"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Interface_Expansion:MCP23017_SP U1
U 1 1 60E74919
P 3550 2300
F 0 "U1" H 3550 3581 50  0000 C CNN
F 1 "MCP23017_SP" H 3550 3490 50  0000 C CNN
F 2 "Package_DIP:DIP-28_W7.62mm" H 3750 1300 50  0001 L CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20001952C.pdf" H 3750 1200 50  0001 L CNN
	1    3550 2300
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R2
U 1 1 60E773A4
P 4700 3350
F 0 "R2" H 4768 3396 50  0000 L CNN
F 1 "330" H 4768 3305 50  0000 L CNN
F 2 "" V 4740 3340 50  0001 C CNN
F 3 "~" H 4700 3350 50  0001 C CNN
	1    4700 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D2
U 1 1 60E7DC9C
P 4700 3700
F 0 "D2" V 4739 3582 50  0000 R CNN
F 1 "LED" V 4648 3582 50  0000 R CNN
F 2 "" H 4700 3700 50  0001 C CNN
F 3 "~" H 4700 3700 50  0001 C CNN
	1    4700 3700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4700 3500 4700 3550
$Comp
L Device:R_US R3
U 1 1 60E8017E
P 5050 3350
F 0 "R3" H 5118 3396 50  0000 L CNN
F 1 "330" H 5118 3305 50  0000 L CNN
F 2 "" V 5090 3340 50  0001 C CNN
F 3 "~" H 5050 3350 50  0001 C CNN
	1    5050 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D3
U 1 1 60E80184
P 5050 3700
F 0 "D3" V 5089 3582 50  0000 R CNN
F 1 "LED" V 4998 3582 50  0000 R CNN
F 2 "" H 5050 3700 50  0001 C CNN
F 3 "~" H 5050 3700 50  0001 C CNN
	1    5050 3700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5050 3500 5050 3550
$Comp
L Device:R_US R4
U 1 1 60E81683
P 5400 3350
F 0 "R4" H 5468 3396 50  0000 L CNN
F 1 "330" H 5468 3305 50  0000 L CNN
F 2 "" V 5440 3340 50  0001 C CNN
F 3 "~" H 5400 3350 50  0001 C CNN
	1    5400 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D4
U 1 1 60E81689
P 5400 3700
F 0 "D4" V 5439 3582 50  0000 R CNN
F 1 "LED" V 5348 3582 50  0000 R CNN
F 2 "" H 5400 3700 50  0001 C CNN
F 3 "~" H 5400 3700 50  0001 C CNN
	1    5400 3700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5400 3500 5400 3550
$Comp
L Device:R_US R5
U 1 1 60E82AC6
P 5750 3350
F 0 "R5" H 5818 3396 50  0000 L CNN
F 1 "330" H 5818 3305 50  0000 L CNN
F 2 "" V 5790 3340 50  0001 C CNN
F 3 "~" H 5750 3350 50  0001 C CNN
	1    5750 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D5
U 1 1 60E82ACC
P 5750 3700
F 0 "D5" V 5789 3582 50  0000 R CNN
F 1 "LED" V 5698 3582 50  0000 R CNN
F 2 "" H 5750 3700 50  0001 C CNN
F 3 "~" H 5750 3700 50  0001 C CNN
	1    5750 3700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5750 3500 5750 3550
$Comp
L Device:R_US R6
U 1 1 60E84206
P 6100 3350
F 0 "R6" H 6168 3396 50  0000 L CNN
F 1 "330" H 6168 3305 50  0000 L CNN
F 2 "" V 6140 3340 50  0001 C CNN
F 3 "~" H 6100 3350 50  0001 C CNN
	1    6100 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D6
U 1 1 60E8420C
P 6100 3700
F 0 "D6" V 6139 3582 50  0000 R CNN
F 1 "LED" V 6048 3582 50  0000 R CNN
F 2 "" H 6100 3700 50  0001 C CNN
F 3 "~" H 6100 3700 50  0001 C CNN
	1    6100 3700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6100 3500 6100 3550
$Comp
L Device:R_US R7
U 1 1 60E85775
P 6450 3350
F 0 "R7" H 6518 3396 50  0000 L CNN
F 1 "330" H 6518 3305 50  0000 L CNN
F 2 "" V 6490 3340 50  0001 C CNN
F 3 "~" H 6450 3350 50  0001 C CNN
	1    6450 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D7
U 1 1 60E8577B
P 6450 3700
F 0 "D7" V 6489 3582 50  0000 R CNN
F 1 "LED" V 6398 3582 50  0000 R CNN
F 2 "" H 6450 3700 50  0001 C CNN
F 3 "~" H 6450 3700 50  0001 C CNN
	1    6450 3700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6450 3500 6450 3550
$Comp
L Device:R_US R8
U 1 1 60E86904
P 6800 3350
F 0 "R8" H 6868 3396 50  0000 L CNN
F 1 "330" H 6868 3305 50  0000 L CNN
F 2 "" V 6840 3340 50  0001 C CNN
F 3 "~" H 6800 3350 50  0001 C CNN
	1    6800 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D8
U 1 1 60E8690A
P 6800 3700
F 0 "D8" V 6839 3582 50  0000 R CNN
F 1 "LED" V 6748 3582 50  0000 R CNN
F 2 "" H 6800 3700 50  0001 C CNN
F 3 "~" H 6800 3700 50  0001 C CNN
	1    6800 3700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6800 3500 6800 3550
$Comp
L Device:R_US R1
U 1 1 60E8C706
P 4350 3350
F 0 "R1" H 4418 3396 50  0000 L CNN
F 1 "330" H 4418 3305 50  0000 L CNN
F 2 "" V 4390 3340 50  0001 C CNN
F 3 "~" H 4350 3350 50  0001 C CNN
	1    4350 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D1
U 1 1 60E8C70C
P 4350 3700
F 0 "D1" V 4389 3582 50  0000 R CNN
F 1 "LED" V 4298 3582 50  0000 R CNN
F 2 "" H 4350 3700 50  0001 C CNN
F 3 "~" H 4350 3700 50  0001 C CNN
	1    4350 3700
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4350 3500 4350 3550
Wire Wire Line
	4350 3850 4350 3950
Wire Wire Line
	4350 3950 4700 3950
Wire Wire Line
	6800 3950 6800 3850
Wire Wire Line
	4700 3850 4700 3950
Connection ~ 4700 3950
Wire Wire Line
	4700 3950 5050 3950
Wire Wire Line
	5050 3850 5050 3950
Connection ~ 5050 3950
Wire Wire Line
	5050 3950 5400 3950
Wire Wire Line
	5400 3850 5400 3950
Connection ~ 5400 3950
Wire Wire Line
	5400 3950 5600 3950
Wire Wire Line
	5750 3850 5750 3950
Connection ~ 5750 3950
Wire Wire Line
	5750 3950 6100 3950
Wire Wire Line
	6100 3850 6100 3950
Connection ~ 6100 3950
Wire Wire Line
	6100 3950 6450 3950
Wire Wire Line
	6450 3850 6450 3950
Connection ~ 6450 3950
Wire Wire Line
	6450 3950 6800 3950
$Comp
L power:GND #PWR04
U 1 1 60E90E92
P 5600 4050
F 0 "#PWR04" H 5600 3800 50  0001 C CNN
F 1 "GND" H 5605 3877 50  0000 C CNN
F 2 "" H 5600 4050 50  0001 C CNN
F 3 "" H 5600 4050 50  0001 C CNN
	1    5600 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 3950 5600 4050
Connection ~ 5600 3950
Wire Wire Line
	5600 3950 5750 3950
Wire Wire Line
	4250 2400 4350 2400
Wire Wire Line
	4350 2400 4350 3200
Wire Wire Line
	4250 3100 6800 3100
Wire Wire Line
	6800 3100 6800 3200
Wire Wire Line
	4250 3000 6450 3000
Wire Wire Line
	6450 3000 6450 3200
Wire Wire Line
	4250 2900 6100 2900
Wire Wire Line
	6100 2900 6100 3200
Wire Wire Line
	4250 2800 5750 2800
Wire Wire Line
	5750 2800 5750 3200
Wire Wire Line
	4250 2700 5400 2700
Wire Wire Line
	5400 2700 5400 3200
Wire Wire Line
	4250 2600 5050 2600
Wire Wire Line
	5050 2600 5050 3200
Wire Wire Line
	4250 2500 4700 2500
Wire Wire Line
	4700 2500 4700 3200
$Comp
L Switch:SW_DIP_x08 SW1
U 1 1 60EA5997
P 4650 1900
F 0 "SW1" H 4650 2567 50  0000 C CNN
F 1 "SW_DIP_x08" H 4650 2476 50  0000 C CNN
F 2 "" H 4650 1900 50  0001 C CNN
F 3 "~" H 4650 1900 50  0001 C CNN
	1    4650 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 1500 5050 1500
Wire Wire Line
	5050 1500 5050 1600
Wire Wire Line
	5050 2200 4950 2200
Wire Wire Line
	4950 1600 5050 1600
Connection ~ 5050 1600
Wire Wire Line
	5050 1600 5050 1700
Wire Wire Line
	4950 1700 5050 1700
Connection ~ 5050 1700
Wire Wire Line
	5050 1700 5050 1800
Wire Wire Line
	4950 1800 5050 1800
Connection ~ 5050 1800
Wire Wire Line
	5050 1800 5050 1900
Wire Wire Line
	4950 1900 5050 1900
Connection ~ 5050 1900
Wire Wire Line
	5050 1900 5050 2000
Wire Wire Line
	4950 2000 5050 2000
Connection ~ 5050 2000
Wire Wire Line
	5050 2000 5050 2100
Wire Wire Line
	4950 2100 5050 2100
Connection ~ 5050 2100
Wire Wire Line
	5050 2100 5050 2200
$Comp
L power:GND #PWR03
U 1 1 60EADB9D
P 5050 2300
F 0 "#PWR03" H 5050 2050 50  0001 C CNN
F 1 "GND" H 5055 2127 50  0000 C CNN
F 2 "" H 5050 2300 50  0001 C CNN
F 3 "" H 5050 2300 50  0001 C CNN
	1    5050 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5050 2200 5050 2300
Connection ~ 5050 2200
Wire Wire Line
	4250 1500 4350 1500
Wire Wire Line
	4350 1600 4250 1600
Wire Wire Line
	4250 1700 4350 1700
Wire Wire Line
	4350 1800 4250 1800
Wire Wire Line
	4250 1900 4350 1900
Wire Wire Line
	4350 2000 4250 2000
Wire Wire Line
	4250 2100 4350 2100
Wire Wire Line
	4350 2200 4250 2200
Wire Wire Line
	2850 2900 2750 2900
Wire Wire Line
	2750 2900 2750 3000
Wire Wire Line
	2750 3100 2850 3100
Wire Wire Line
	2850 3000 2750 3000
Connection ~ 2750 3000
Wire Wire Line
	2750 3000 2750 3100
Wire Wire Line
	3550 1200 2750 1200
Wire Wire Line
	2750 1200 2750 2400
Wire Wire Line
	2750 2400 2850 2400
$Comp
L power:GND #PWR02
U 1 1 60EC8AA8
P 3550 3500
F 0 "#PWR02" H 3550 3250 50  0001 C CNN
F 1 "GND" H 3555 3327 50  0000 C CNN
F 2 "" H 3550 3500 50  0001 C CNN
F 3 "" H 3550 3500 50  0001 C CNN
	1    3550 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 3400 3550 3500
Wire Wire Line
	3550 3400 2750 3400
Wire Wire Line
	2750 3400 2750 3100
Connection ~ 3550 3400
Connection ~ 2750 3100
$Comp
L power:+3.3V #PWR01
U 1 1 60EDE539
P 2750 1100
F 0 "#PWR01" H 2750 950 50  0001 C CNN
F 1 "+3.3V" H 2765 1273 50  0000 C CNN
F 2 "" H 2750 1100 50  0001 C CNN
F 3 "" H 2750 1100 50  0001 C CNN
	1    2750 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 1100 2750 1200
Connection ~ 2750 1200
$Comp
L Device:C C1
U 1 1 60EE1869
P 2400 1850
F 0 "C1" H 2515 1896 50  0000 L CNN
F 1 "0.1u" H 2515 1805 50  0000 L CNN
F 2 "" H 2438 1700 50  0001 C CNN
F 3 "~" H 2400 1850 50  0001 C CNN
	1    2400 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 1200 2400 1200
Wire Wire Line
	2400 1200 2400 1700
Wire Wire Line
	2400 2000 2400 3400
Wire Wire Line
	2400 3400 2750 3400
Connection ~ 2750 3400
Text GLabel 1400 1700 0    50   BiDi ~ 0
I2C_SDA
Text GLabel 1400 1800 0    50   Input ~ 0
I2C_SCL
Text GLabel 1400 1900 0    50   Output ~ 0
D5
$Comp
L Device:R_US R9
U 1 1 60E815D5
P 1500 1450
F 0 "R9" H 1568 1496 50  0000 L CNN
F 1 "4.7k" H 1568 1405 50  0000 L CNN
F 2 "" V 1540 1440 50  0001 C CNN
F 3 "~" H 1500 1450 50  0001 C CNN
	1    1500 1450
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R10
U 1 1 60E82C32
P 1800 1450
F 0 "R10" H 1868 1496 50  0000 L CNN
F 1 "4.7k" H 1868 1405 50  0000 L CNN
F 2 "" V 1840 1440 50  0001 C CNN
F 3 "~" H 1800 1450 50  0001 C CNN
	1    1800 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2850 1600 2200 1600
Wire Wire Line
	2200 1600 2200 1800
Wire Wire Line
	2200 1800 1800 1800
Wire Wire Line
	2850 1500 2100 1500
Wire Wire Line
	2100 1500 2100 1700
Wire Wire Line
	2100 1700 1500 1700
Wire Wire Line
	1500 1600 1500 1700
Connection ~ 1500 1700
Wire Wire Line
	1500 1700 1400 1700
Wire Wire Line
	1800 1600 1800 1800
Connection ~ 1800 1800
Wire Wire Line
	1800 1800 1400 1800
Wire Wire Line
	2400 1200 1800 1200
Wire Wire Line
	1500 1200 1500 1300
Connection ~ 2400 1200
Wire Wire Line
	1800 1300 1800 1200
Connection ~ 1800 1200
Wire Wire Line
	1800 1200 1500 1200
Wire Wire Line
	2850 2100 2200 2100
Wire Wire Line
	2200 2100 2200 1900
Wire Wire Line
	2200 1900 1400 1900
$EndSCHEMATC