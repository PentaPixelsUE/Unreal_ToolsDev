int div = 10;
float3 colA= float3(1.0,0.0,0.0);
float3 colB= float3(0.0,0.0,1.0);


return lerp(colB,colA,step(((ceil(tex*div))/div)-sin(t),0.5));
