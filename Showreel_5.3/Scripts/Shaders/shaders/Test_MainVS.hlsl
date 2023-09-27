float4 main(float2 uv : TEXCOORD0) : SV_TARGET
{
    float2 grid = float2(24, 8);
    float2 tex = frac(uv * grid);
    float2 dim = float2(0.8, 0.8);
    
    if (tex.x >= -dim.x && tex.x <= dim.x && tex.y >= -dim.y && tex.y <= dim.y)
    {
        return float4(1.0, 1.0, 1.0, 1.0); // Return white color (1, 1, 1, 1)
    }
    else
    {
        return float4(0.0, 0.0, 0.0, 1.0); // Return black color (0, 0, 0, 1)
    }
}
