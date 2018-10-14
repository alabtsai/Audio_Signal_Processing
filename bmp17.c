
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int  main(int argc ,  char **argv )
{ 

    FILE                *filebmp  ;
    FILE                *fout ;
    unsigned char     get[1000] ; 
    long int                        i,j  ;
    long int                       cur ;
    double    t, delta ;   
    int16_t  sample;

    filebmp=fopen(argv[1],"rb");
    fout=fopen("out.data","w");
//  N=117*121;
    
    printf("This is to extract the audio data of the WAV file of %s... by Su-Yung Tsai\n",argv[1]);

    for ( j=0; j < 11 ; j++ ){
      fread(get, 1,4,filebmp);
      for (i=0;i<4;i++) printf("%ld ",4*j+i);  
      printf("---");
      for ( i=0; i <4; i++ )
	{
         printf("%02x ",get[i]);
	    		      }
      if (j==1) {printf("RIFF chunk size=%d",  get[0]+get[1]*256+get[2]*65536+get[3]*1024*1024*16 );   }
      if (j==5) {printf("PCM=%d, Num of channel=%d",  get[0]+get[1]*256,  get[2]+get[3]*256 );   }
      if (j==6) {printf("sampling rate fs=%d,", get[0]+get[1]*256+get[2]*65536+get[3]*1024*1024*16 ); 
                delta=1.0/( get[0]+get[1]*256+get[2]*65536+get[3]*1024*1024*16 ) ;
                 printf(" Sampling time Ts=%10.7f",delta); }
      if (j==7) {printf("byte rate=%d", 
                                       get[0]+get[1]*256+get[2]*65536+get[3]*1024*1024*16 );   }
      if (j==8) {printf("bits per sample=%d",  get[2]+get[3]*256 );   }
      if (j==10) {printf("File size=%d",  get[0]+get[1]*256+get[2]*65536+get[3]*1024*1024*16 );   }
      printf("\n");
    }
      
     cur=ftell(filebmp )  ;
     printf("wav file current positon =%ld\n",cur  );
     printf("Starting reading data now ... exciting !!\n\n\n");
     t=0; int tt; double tm;
     for (i=0;i<10000000;i++) {
      tt=fread(get, 1,2,filebmp);  
      if (tt==2){
         sample=get[0]+get[1]*256 ; // readin 16 bits
         fprintf(fout,  "%17.10f %d\n", t,sample);    
         t=t+delta;}
      else {printf("total readin %ld data !! each data is two bytes !! \n",i ); 
            printf("cause read in tt= %d less than two bytes!!\n",tt ); 
            tm=delta*i; 
            printf("total record time is %ld x %10.7f  %7.3f second\n", i,delta,tm);
            exit(0) ; }

     }


     fclose(fout);
     fclose(filebmp);


}
/*** final ***/
