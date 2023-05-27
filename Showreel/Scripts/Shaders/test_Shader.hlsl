// Vertex input structure
struct VertexInput
{
    float3 position : POSITION;
    float3 normal : NORMAL;
};

// Vertex output structure
struct VertexOutput
{
    float4 position : SV_POSITION;
    float3 normal : NORMAL;
};

// Constant buffer for transformation matrix
cbuffer TransformBuffer : register(b0)
{
    float4x4 worldViewProjectionMatrix;
}

// Vertex shader entry point
VertexOutput SimpleVertexShader(VertexInput input)
{
    VertexOutput output;

    // Transform the vertex position
    output.position = mul(float4(input.position, 1.0f), worldViewProjectionMatrix);

    // Pass through the normal
    output.normal = input.normal;

    return output;
}
