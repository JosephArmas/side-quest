#version 330
in vec3 Normal;
in vec2 TexCoord;
in vec3 FragPos;

// This is the proper way to set the color of the fragment, NOT using gl_FragColor.
layout (location = 0) out vec4 FragColor;

uniform sampler2D ourTexture;
// Lighting parameters for ambient light, and a single point light w/ no attenuation.
uniform vec3 ambientColor;
uniform vec3 pointPosition;
uniform vec3 pointColor;

// Pass in the camera
uniform vec3 viewPos;

// coefficients for the material
uniform float ambientCoe;
uniform float diffuseCoe;
uniform float specularCoe;
uniform float shine;


void main() {
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(pointPosition - FragPos);  
    float cosineLight = max(dot(norm, lightDir), 0.0);

    // Compute the ambient and diffuse components.
    // vec3 ambient = ambientColor;
    // vec3 diffuse = cosineLight * pointColor;

    vec3 ambient = ambientCoe * ambientColor;
    vec3 diffuse = diffuseCoe * cosineLight * pointColor;

    // Compute the specular component.
    vec3 reflect_vector = reflect(-lightDir, norm);
    float cosine = dot(reflect_vector, normalize(viewPos - FragPos));
    // float spec_factor = pow(max(cosine, 0.0), 32.0);
    float spec_factor = pow(max(cosine, 0.0), shine);

    // vec3 specular = spec_factor * pointColor;
    vec3 specular = specularCoe * spec_factor * pointColor;


    // Assemble the final fragment color.
    FragColor = vec4(diffuse + ambient + specular, 1.0) * texture(ourTexture, TexCoord);
}