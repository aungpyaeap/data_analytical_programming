DATA FLIGHTINFO;

  INFILE '/home/aungpyaemcc0/DAP_codes/FLIGHTINFO.DAT';

  /*INPUT Col1 $ Col2 Col3 Col4 Col5 Col6 Col7;*/
  
  INPUT 
  	@1 Flight 2.
	@4 Date mmddyy6.
	@10 Time time5.
	@15 Origin $3.
	@18 Dest $3.
	@21 Miles comma5.
	@26 Mail 4.
	@30 Freight 3.
	@34 Boarded 3.
	@37 Transfer 3.
	@40 Nonrev 3.
	@43 Deplane 3.
	@46 Capacity 3.;

 /*input    flight 1-3
           	@4 date mmddyy6.
			@10 time time5.
			orig $ 15-17
			dest $ 18-20
			@21 miles comma5.
			mail 26-29
			freight 30-33
			boarded 34-36
			transfer 37-39
			nonrev 40-42
			deplane 43-45
			capacity 46-48;*/

RUN;

* Print the data to make sure the file was read correctly;

PROC PRINT DATA = FLIGHTINFO;
  TITLE 'Filght Info Data';
  FORMAT Date mmddyy10.;
  FORMAT Time time5.;
RUN;

DATA MARCH15 ;
	SET FLIGHTINFO;
	FORMAT Date mmddyy10.;
	FORMAT Time time5.;
	IF (Date ^= '15mar1990'd) THEN DELETE;
RUN;

DATA LONDON ;
	SET FLIGHTINFO;
	FORMAT Date mmddyy10.;
  	FORMAT Time time5.;
	IF (Dest ^= 'LON') THEN DELETE;
RUN;

DATA LONGHAUL  ;
	SET FLIGHTINFO;
	FORMAT Date mmddyy10.;
  	FORMAT Time time5.;
	IF (Miles < 1000) THEN DELETE;
RUN;
