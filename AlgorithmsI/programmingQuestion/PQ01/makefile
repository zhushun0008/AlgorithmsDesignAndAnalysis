all	:	countInversion
countInversion:	countInversion.o 
	cc -o countInversion countInversion.o 
countInversion.o: countInversion.c 
	cc -c countInversion.c
.PHONY : clean
clean :
	rm *.o
