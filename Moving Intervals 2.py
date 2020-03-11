  int m,n,k,a[10000],in[10000],i,j,key,r,r1,max,x,c=-1,y=0,s,u,o,value,min;
  scanf("%d %d %d",&m,&n,&k);
m,n,k=input().split(" ")
m=int(m)
n=int(n)
k=int(k)
a = []
inter = []
for i in range(0,2n,2):

for(i=0;i<2*n;i=i+2)

    scanf("%d %d",(a+i), (a+i+1));
    key=*(a+i);
    r=*(a+i+1);
    j=i-2;
    while(j>=0 && a[j]>key)
    {
      a[j+2]=a[j];
      a[j+3]=a[j+1];
      j=j-2;
    }
    a[j+2]=key;
    a[j+3]=r;
  }
  //printf("\n");
  /*for(i=0;i<2*n;i++)
  {
    printf("%d  ",*(a+i));
  }*/
  j=1;
  for(i=0;i<=n;i++)
  {
    if(i==0)
    {
      in[i]=a[i]-1;
    }
    else if(i==n)
    {
      in[i]=m-a[2*n-1];
    }
    else
    {
      x=a[j+1]-a[j];
      if(x<=0)
      {
	    in[i]=-(a[j]-a[j+1]+1);
      }
      else
      {
	    in[i]=x-1;
      }
      j=j+2;
    }
  }
  max=in[0];
  for(i=0;i<=n;i++)
  {
    if(in[i]>max)
    {
      max=in[i];
    }
    if(in[i]<0 && in[i+1]<0)
    {
      if(c==-1)
      {
	    c=1;
	    value=a[2*(i+1)]-a[2*i-1];
	    r=a[2*i+1]-a[2*i]+1;
      }
      else
      {
	c=c+1;
      }
    }
    if(in[i]<0)
    {
      y=y+1;
      if(y==1)
      {
	    u=i;//a[2*(i+1)]-a[2*(i+1)-1]-1;
	    r1=a[2*i-1]-a[2*(i-1)]+1;
	    key=a[2*i+1]-a[2*i]+1;
        if(a[2*i+1]<=a[2*i-1])
	    {
	      o=a[2*i+1]-a[2*i]+1;
	    }
	    else
	    {
	      o=a[2*i-1]-a[2*i]+1;
	    }
	    if(r1<key)
	    {
	      min=r1;
	    }
	    else
	    {
	      min=key;
	    }
      }
    }
  }
  //printf("\n  %d  %d",c,y);
  if(k==0)
  {
    if(y==0)
    {
      printf("Good\n");
    }
    else
    {
      printf("Bad\n");
    }
  }
  if(k==1)
  {
    if(c>1)
    {
      printf("Bad\n");
    }
    else if(c==1)
    {
      if(y>2)
      {
	    printf("Bad\n");
      }
      else if((value<=0)|| (r>max))
      {
	    printf("Bad\n");
      }
      else
      {
	    printf("Good\n");
      }
    }
    else
    {
      if(y==1)
      {
	    if((in[u-1]>=o) || (in[u+1]>=o) || min<=max)
	    {
	      printf("Good\n");
	    }
        else
        {
          printf("Bad\n");
        }
	  }
	  else
	  {
	    printf("Bad\n");
	  }
    }
  }
}