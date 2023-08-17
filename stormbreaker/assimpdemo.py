import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Mesh3D_normals import *

# from Object3D_animated import *
from Object3D import *
from OpenGL.GL import shaders

# from Object3D import *
import os
import assimp_py

from RenderProgram import *
import time
import math


def load_obj(filename) -> Object3D:
    with open(filename) as f:
        return Object3D(Mesh3D.load_obj(f))


def mesh_to_object3d(mesh, scene, filename, texture_path):
    material = scene.materials[mesh.material_index]

    if texture_path is None:
        if mesh.material_index > 0 and len(material["TEXTURES"]) == 0:
            material = scene.materials[0]

        if mesh.material_index < 0 or len(material["TEXTURES"]) == 0:
            raise Exception(
                "You must provide a texture_path because the OBJ file has no .mtl file, or there is no texture set in the .mtl file"
            )

        # Load the texture information from the obj file's material file.
        textures = material["TEXTURES"][1]
        objpath = os.path.dirname(filename)

        # mac / linux
        texture_path = os.path.join(objpath, textures[0]).replace("\\", "/")

        # win
        # texture_path = os.path.join(objpath, textures[0])

    obj = Object3D(Mesh3D.load_assimp_mesh(mesh, pygame.image.load(texture_path)))

    return obj


def assimp_load_object(
    filename, texture_path=None, assimp_options=assimp_py.Process_Triangulate
) -> Object3D:
    scene = assimp_py.ImportFile(filename, assimp_options)

    if len(scene.meshes) == 1:
        return mesh_to_object3d(scene.meshes[0], scene, filename, texture_path)

    root = Object3D(None)
    for mesh in scene.meshes:
        obj = mesh_to_object3d(mesh, scene, filename, texture_path)
        root.add_child(obj)
    return root


def apply_change_tex(obj, texture_path):
    obj.change_tex(texture_path)


def load_shader_source(filename):
    with open(filename) as f:
        return f.read()


def get_program(vertex_source_filename, fragment_source_filename):
    vertex_shader = shaders.compileShader(
        load_shader_source(vertex_source_filename), GL_VERTEX_SHADER
    )
    fragment_shader = shaders.compileShader(
        load_shader_source(fragment_source_filename), GL_FRAGMENT_SHADER
    )
    return shaders.compileProgram(vertex_shader, fragment_shader)


def controller(obj: object, keys_down):
    if pygame.K_UP in keys_down:
        obj.rotate(glm.vec3(-0.001, 0, 0))
    elif pygame.K_DOWN in keys_down:
        obj.rotate(glm.vec3(0.001, 0, 0))
    if pygame.K_RIGHT in keys_down:
        obj.rotate(glm.vec3(0, 0.001, 0))
    elif pygame.K_LEFT in keys_down:
        obj.rotate(glm.vec3(0, -0.001, 0))


def light_controller(obj: object, keys_down, light_pos):
    if pygame.K_a in keys_down:
        light.move(glm.vec3(-0.0001, 0, 0))
        renderer.set_uniform("pointPosition", light.position, glm.vec3)
        # print(light_pos)
    elif pygame.K_d in keys_down:
        light.move(glm.vec3(0.0001, 0, 0))
        renderer.set_uniform("pointPosition", light.position, glm.vec3)
        # print(light_pos)
    elif pygame.K_w in keys_down:
        light.move(glm.vec3(0, 0.0001, 0))
        renderer.set_uniform("pointPosition", light.position, glm.vec3)
        # print(light_pos)
    elif pygame.K_s in keys_down:
        light.move(glm.vec3(0, -0.0001, 0))
        renderer.set_uniform("pointPosition", light.position, glm.vec3)
        # print(light_pos)


def light_controller_mac(obj: object, keys_down):
    if pygame.K_a in keys_down:
        light.move(glm.vec3(-0.01, 0, 0))
        renderer.set_uniform("pointPosition", light.position, glm.vec3)
    elif pygame.K_d in keys_down:
        light.move(glm.vec3(0.01, 0, 0))
        renderer.set_uniform("pointPosition", light.position, glm.vec3)
    elif pygame.K_w in keys_down:
        light.move(glm.vec3(0, 0.01, 0))
        renderer.set_uniform("pointPosition", light.position, glm.vec3)
    elif pygame.K_s in keys_down:
        light.move(glm.vec3(0, -0.01, 0))
        renderer.set_uniform("pointPosition", light.position, glm.vec3)


def update_light_pos(light, renderer):
    ambient_color = glm.vec3(1, 1, 1)
    ambient_intensity = 0.1
    renderer.set_uniform("ambientColor", ambient_color * ambient_intensity, glm.vec3)
    renderer.set_uniform("pointPosition", light.position, glm.vec3)
    renderer.set_uniform("pointColor", glm.vec3(1, 1, 1), glm.vec3)
    renderer.set_uniform("viewPos", glm.vec3(0, 0, 0), glm.vec3)


if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 800

    pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK,
        pygame.GL_CONTEXT_PROFILE_CORE,
    )
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
    # For Mac people.
    # pygame.display.gl_set_attribute(GL_CONTEXT_MAJOR_VERSION, 3)
    # pygame.display.gl_set_attribute(GL_CONTEXT_MINOR_VERSION, 3)
    # pygame.display.gl_set_attribute(GL_CONTEXT_FORWARD_COMPATIBLE_FLAG, True)
    # pygame.display.gl_set_attribute(GL_CONTEXT_PROFILE_COMPATIBILITY, GL_CONTEXT_PROFILE_CORE)

    screen = pygame.display.set_mode(
        (screen_width, screen_height),
        DOUBLEBUF | OPENGL,
    )

    print(glGetString(GL_VERSION))

    pygame.display.set_caption("OpenGL in Python")

    # earth = load_textured_obj("models/bunny_textured.obj")
    earth = assimp_load_object("models/earth.obj", "models/earth_6k.png")
    earth.set_material(glm.vec4(1, 1, 1, 32))
    earth.move(glm.vec3(1, 0, -5))
    # earth.move(glm.vec3(0.3, -0.5, -3))
    earth.grow(glm.vec3(1, 1, 1))

    # boat = assimp_load_object("models/boat/boat.fbx")
    # boat = assimp_load_object(
    #     "models/backpack/backpack.obj",
    #     None,
    #     assimp_py.Process_Triangulate | assimp_py.Process_FlipUVs,
    # )
    # boat.move(glm.vec3(-1, 0, -5))
    # boat.grow(glm.vec3(0.5, 0.5, 0.5))
    # boat.rotate(glm.vec3(math.pi / 4, math.pi / 2, math.pi / 2))
    # boat.set_material(glm.vec4(1, 1, 0.3, 1))

    # Tester code
    # test = assimp_load_object(
    #     "models/Tree1/Tree1.obj", "models/Tree1/BarkDecidious0143_5_S.jpg"
    # )
    # test.set_material(glm.vec4(1, 1, 1, 32))
    # test.move(glm.vec3(0, 0, -1))
    # test.grow(glm.vec3(3, 3, 3))

    # test
    test = assimp_load_object(
        "models/stormbreaker/StormBreaker_axHead.obj",
        "models/stormbreaker/chromev1.jpeg",
    )
    test.move(glm.vec3(0, 0, -1))
    test.grow(glm.vec3(0.01, 0.01, 0.01))
    test.set_material(glm.vec4(1, 1, 1, 32))
    # test.set_spotlight(0.5)

    # ground
    ground = assimp_load_object(
        "models/ground/cube.obj",
        "models/textures/plain_cement.jpeg"
        # "models/ground/cube.obj",
        # "models/textures/shattered_cement.jpeg",
    )
    # ground.grow(glm.vec3(10, 0.01, 6.8))
    ground.grow(glm.vec3(10, 0.01, 10))
    ground.move(glm.vec3(0, -1.5, -5))
    ground.set_material(glm.vec4(1, 1, 0.5, 30))
    ground.set_spotlight(0.9)

    back_drop = assimp_load_object("models/cube.obj", "models/textures/night-sky.jpg")
    back_drop.grow(glm.vec3(7, 6, 0.1))
    back_drop.move(glm.vec3(0, 0, -9))
    back_drop.set_material(glm.vec4(1, 1, 0.5, 30))
    # back_drop.set_spotlight(0.1)

    # sky
    sky = assimp_load_object("models/cube.obj", "models/textures/blue-sky.jpg")
    sky.grow(glm.vec3(30, 30, 0.1))
    sky.move(glm.vec3(0, 0, -50))
    sky.set_material(glm.vec4(1, 1, 0.5, 20))
    sky.set_spotlight(0)

    rock = assimp_load_object(
        # "models/rock/Rock_001.obj",
        # "models/rock/Rock_001_SPECULAR.png"
        "models/rock/Rock_001.obj",
        "models/textures/rocky.jpeg",
    )
    rock.grow(glm.vec3(0.005, 0.005, 0.005))
    rock.move(glm.vec3(-1.5, -1.5, -2.9))
    rock.set_material(glm.vec4(1, 1, 1, 50))
    # rock.set_spotlight(0.1)

    # test 2
    kaws = assimp_load_object(
        "models/Kaws_Clown/Kaws_Clown.obj",
        "models/Kaws_Clown/Kaws_Clean_Color.png",
        # "models/textures/wall.jpg",
        # "models/textures/chromev1.jpeg",
    )
    # kaws.center_point(glm.vec3(-0.03, 0.07, 0))
    # kaws.move(glm.vec3(-1.4, -1.37, -7))
    kaws.move(glm.vec3(-2.1, -0.09, -7))
    kaws.grow(glm.vec3(0.008, 0.008, 0.008))
    kaws.set_material(glm.vec4(1, 1, 1, 32))

    # kaws 2
    kaws2 = assimp_load_object("models/Kaws_Protector/KAWSProtector.obj")
    # kaws2.move(glm.vec3(1.4, -1.37, -7))
    kaws2.move(glm.vec3(1.2, 0.008, -7))
    kaws2.grow(glm.vec3(0.06, 0.06, 0.06))

    # ax head
    ax_head = assimp_load_object(
        "models/stormbreaker/StormBreaker_axHead.obj",
        "models/stormbreaker/chromev1.jpeg",
    )
    ax_head.set_material(glm.vec4(1, 1, 80, 100))

    # ax handle
    ax_handle = assimp_load_object(
        "models/stormbreaker/StormBreaker_Handle.obj",
        "models/stormbreaker/bark.jpeg",
    )

    ax_handle.set_material(glm.vec4(1, 1, 0, 10))

    axe = Object3D(None)
    axe.add_child(ax_head)
    axe.add_child(ax_handle)

    # axe.grow(glm.vec3(0.01, 0.01, 0.02))
    axe.grow(glm.vec3(0.007, 0.007, 0.007))

    # axe.rotate(glm.vec3(0, 4.7, 0))  # axe upright
    # axe.rotate(glm.vec3(0, 3, 0))  # axe face right
    # axe.rotate(glm.vec3(0.9, 4.7, 0))  # axe upright
    # print(axe.orientation.x)

    # axe.move(glm.vec3(0, 0, -2))
    # axe.move(glm.vec3(-1, 0, -2))  # simulate collision

    axe.rotate(glm.vec3(-3, 0, 0))  # upside down

    # axe.rotate(glm.vec3(-3, 0.7, 0))  # titled & upsidedown -> dropping hammer

    axe.move(glm.vec3(0, -0.84, -2))  # hover position
    # axe.move(glm.vec3(0, -1, -2))  # on ground

    axe.set_spotlight(60)

    # helmet
    helmet = assimp_load_object(
        "models/ironman_helmet/obj/helmet.obj",
        "models/textures/chromev2.jpeg",
    )
    # helmet.grow(glm.vec3(0.020, 0.020, 0.020))
    # helmet.grow(glm.vec3(0.019, 0.015, 0.015))
    # helmet.move(glm.vec3(1, 0, -2))
    # helmet.set_material(glm.vec4(1, 1, 1, 50))
    helmet.grow(glm.vec3(0, 0, 0))
    helmet.move(glm.vec3(0, 0, 0))
    # helmet.set_material(glm.vec4(1, 1, 1, 50))
    # helmet.set_spotlight(10)

    # sky object
    skybox = assimp_load_object("models/cube.obj", "models/textures/night-sky.jpg")
    skybox.grow(glm.vec3(20, 20, 20))
    skybox.move(glm.vec3(0, 0, 0))
    skybox.set_material(glm.vec4(5, 1, 1, 50))

    # light
    light = Object3D(None)
    # light.position = glm.vec3(0, 0, 1)
    # light.position = glm.vec3(0, 0, 0)
    light.position = glm.vec3(0, 2, 0)

    # ufo = assimp_load_object("models/ufo/ufo_1.obj", "models/textures/chromev1.jpeg")
    ufo = assimp_load_object("models/ufo/Low_poly_UFO.obj")
    ufo.grow(glm.vec3(0.008, 0.008, 0.008))
    ufo.rotate(glm.vec3(0.4, 0, 0))
    # ufo.move(glm.vec3(1.3, 0, -2))
    ufo.move(glm.vec3(1.3, 0.9, -2))

    # bridge
    bridge = assimp_load_object("models/bridge/Old_stone_bridgeOBJ.obj")
    bridge.grow(glm.vec3(0.12, 0.12, 0.12))
    bridge.move(glm.vec3(-0.5, -0.62, -3))

    # Load the vertex and fragment shaders for this program.
    shader_lighting = get_program(
        "shaders/normal_perspective.vert", "shaders/specular_light.frag"
    )
    shader_nolighting = get_program(
        "shaders/normal_perspective.vert", "shaders/texture_mapped.frag"
    )

    # spotlight
    shader_spotlight = get_program(
        "shaders/normal_perspective.vert", "shaders/spot_light.frag"
    )

    renderer = RenderProgram()

    # Define the scene.
    camera_position = glm.vec3(0, 0, 3)
    # camera_position = glm.vec3(0, 0, 0)
    # camera_position = glm.vec3(0, -0.05, -10)

    # fixed point
    # fixed_point = glm.vec3(0, 0, 0)

    # z distance
    # z_distance = 3

    # perfered angle
    # rotation_angle = 0.0

    camera = glm.lookAt(camera_position, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))
    perspective = glm.perspective(
        math.radians(30), screen_width / screen_height, 0.1, 100
    )

    ambient_color = glm.vec3(1, 1, 1)
    ambient_intensity = 0.1
    renderer.set_uniform("ambientColor", ambient_color * ambient_intensity, glm.vec3)
    renderer.set_uniform("pointPosition", light.position, glm.vec3)
    renderer.set_uniform("pointColor", glm.vec3(1, 1, 1), glm.vec3)
    renderer.set_uniform("viewPos", glm.vec3(0, 0, 0), glm.vec3)

    # Loop
    done = False
    frames = 0
    start = time.perf_counter()
    throw = False
    hover = True

    lower = -0.9
    upper = -0.78

    direction = 1

    simulation_running = False

    delta_time = 0.001

    # Only draw wireframes.
    glEnable(GL_DEPTH_TEST)
    keys_down = set()
    spin = False
    collision = False
    simulation_running = False

    hover = True
    ground_impact = False
    simulation_ground = False

    ufo_flying = True
    ufo_timer = 0
    ufo_standby = False

    shattered = "models/textures/shattered_cement.jpeg"
    not_shattered = "models/textures/plain_cement.jpeg"

    is_light_y = True

    current_shader = shader_lighting

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                keys_down.add(event.dict["key"])
                if pygame.K_2 in keys_down:
                    if current_shader == shader_lighting:
                        print("light: spotlight")
                        current_shader = shader_spotlight
                    else:
                        print("light: specular")
                        current_shader = shader_lighting
                if pygame.K_1 in keys_down:
                    is_light_y = not is_light_y
                    if is_light_y:
                        print("light pos: above")
                        light.set_absolute_position(glm.vec3(0, 2, 0))
                    else:
                        print("light pos: -z")
                        light.set_absolute_position(glm.vec3(0, 0, 0))
                    update_light_pos(light, renderer)
            elif event.type == pygame.KEYUP:
                keys_down.remove(event.dict["key"])

        # controller(ground, keys_down)
        controller(axe, keys_down)
        # print(axe.position)
        # print(axe.orientation)
        light_position = light.get_position()
        light_controller(light, keys_down, light_position)

        """
        if pygame.K_UP in keys_down:
            earth.rotate(glm.vec3(-0.001, 0, 0))
        elif pygame.K_DOWN in keys_down:
            earth.rotate(glm.vec3(0.001, 0, 0))
        if pygame.K_RIGHT in keys_down:
            earth.rotate(glm.vec3(0, 0.001, 0))
        elif pygame.K_LEFT in keys_down:
            earth.rotate(glm.vec3(0, -0.001, 0))

        if pygame.K_a in keys_down:
            light.move(glm.vec3(-0.003, 0, 0))
            renderer.set_uniform("pointPosition", light.position, glm.vec3)
        elif pygame.K_d in keys_down:
            light.move(glm.vec3(0.003, 0, 0))
            renderer.set_uniform("pointPosition", light.position, glm.vec3)
        elif pygame.K_w in keys_down:
            light.move(glm.vec3(0, 0, -0.003))
            renderer.set_uniform("pointPosition", light.position, glm.vec3)
        elif pygame.K_s in keys_down:
            light.move(glm.vec3(0, 0, 0.003))
            renderer.set_uniform("pointPosition", light.position, glm.vec3)

        """

        # camera

        if pygame.K_n in keys_down:  # forward
            camera_position.z -= 0.0001
            # print(camera_position)
        if pygame.K_m in keys_down:  # backward
            camera_position.z += 0.0001
            # print(camera_position)
        if pygame.K_l in keys_down:  # left
            camera_position.x -= 0.0001
            # print(camera_position)
        if pygame.K_h in keys_down:  # right
            camera_position.x += 0.0001
            # print(camera_position)
        if pygame.K_k in keys_down:  # down
            camera_position.y -= 0.0001
            # print(camera_position)
        if pygame.K_j in keys_down:  # up
            camera_position.y += 0.0001
            # print(camera_position)

        camera = glm.lookAt(camera_position, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))

        # lower -1.19
        # upper -0.78
        # print(axe_y)

        ufo_timer += 1
        if ufo_flying:
            ufo.move(glm.vec3(-0.003, 0, 0))
            if ufo_timer >= 2000:
                # if ufo_timer >= 20000:
                ufo_flying = False
                ufo_timer = 0
        else:
            if ufo_timer >= 2000:
                # if ufo_timer >= 20000:
                ufo.set_absolute_position(glm.vec3(1.9, 0.9, -2))
            # if ufo_timer >= 20000:
            if ufo_timer >= 2000:
                ufo_flying = True
                ufo_timer = 0

        if pygame.K_z in keys_down:
            hover = False
            throw = False
            simulation_running = False
            if not simulation_ground:
                axe.set_absolute_position(glm.vec3(0, 0.8, -2))
                axe.set_absolute_orientation(
                    glm.vec3(-3, 0.7, 0)
                )  # titled & upsidedown -> dropping hammer
            simulation_ground = True

        if simulation_ground:
            axe.move(glm.vec3(0, -0.005, 0))
            if axe.get_position().y <= -1:
                print("hit ground")
                axe.move(glm.vec3(0, 0, 0))
                simulation_ground = False
                ground_impact = True

        if ground_impact:
            new_tex = "models/textures/shattered_cement.jpeg"
            apply_change_tex(ground, new_tex)

        if pygame.K_y in keys_down:
            hover = False
            if not simulation_running:
                axe.set_absolute_position(glm.vec3(-1, 0, -2))
                axe.set_absolute_orientation(glm.vec3(0, 3, 0))
                helmet.set_absolute_scale(glm.vec3(0.019, 0.015, 0.015))
                helmet.set_absolute_position(glm.vec3(1, 0, -2))
            #     renderer.render(perspective, camera, [helmet])
            simulation_running = True

        if simulation_running:
            axe.move(glm.vec3(+0.0001, 0, 0))  # slow
            helmet.move(glm.vec3(-0.0001, 0, 0))  # slow

            axe.move(glm.vec3(+0.001, 0, 0))  # fast
            helmet.move(glm.vec3(-0.001, 0, 0))  # fast

            if helmet.check_collision(axe):
                print("collision detected")
                axe.impact_bounce(helmet)
                helmet.impact_bounce(
                    axe, 4
                )  # larger it is, the more bounce on that object -> helmet has more bounce
                collision = True

            if collision:
                for obj in [axe, helmet]:
                    obj.graivty(delta_time)
                    obj.update(delta_time)

        if hover:
            axe_position = axe.get_position()
            axe_y = axe_position.y
            if direction == 1 and axe_y < upper:
                axe.move(glm.vec3(0, 0.00006, 0))
            elif direction == -1 and axe_y > lower:
                axe.move(glm.vec3(0, -0.00006, 0))

            if axe_y >= upper:
                direction = -1
            elif axe_y <= lower:
                direction = 1

        if pygame.K_t in keys_down:
            hover = False
            prep_throw = True
            if not throw:
                axe.set_absolute_orientation(glm.vec3(0, 4.7, 0))
            throw = True

        if throw:
            # axe.move(glm.vec3(0, 0, -0.001))  # slow
            axe.move(glm.vec3(0, 0, -0.01))  # fast
            # axe.move(glm.vec3(0, 0, -0.1))  # super fast

        if pygame.K_ESCAPE in keys_down:
            throw = False

        if pygame.K_SPACE in keys_down:
            ground_impact = False  # comment out if you want to see the ground impact
            apply_change_tex(
                ground, not_shattered
            )  # comment out if you want to see the ground impact

            axe.set_absolute_position(glm.vec3(0, -0.84, -2))
            axe.set_absolute_orientation(glm.vec3(-3, 0, 0))

            helmet.set_absolute_position(glm.vec3(0, 0, 0))
            helmet.set_absolute_scale(glm.vec3(0, 0, 0))

            throw = False
            simulation_running = False
            hover = True

        # update_light_pos(light, renderer)

        # axe.rotate(glm.vec3(0, 0.001, 0))

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # renderer.use_program(shader_lighting)
        # renderer.use_program(shader_spotlight)
        renderer.use_program(current_shader)
        # renderer.render(perspective, camera, [earth, boat])
        # renderer.render(perspective, camera, [earth])
        # renderer.render(perspective, camera, [boat])

        # renderer.render(perspective, camera, [ground, back_drop])
        # renderer.render(perspective, camera, [ground])
        # renderer.render(perspective, camera, [back_drop])
        # renderer.render(perspective, camera, [skybox])
        # renderer.render(perspective, camera, [helmet])
        # renderer.render(perspective, camera, [t1])

        # renderer.render(perspective, camera, [kaws])
        # renderer.render(perspective, camera, [kaws2])

        # renderer.render(perspective, camera, [ax_head])
        # renderer.render(perspective, camera, [ax_handle])
        # renderer.render(perspective, camera, [test, ground])
        # renderer.render(perspective, camera, [axe])
        # renderer.render(perspective, camera, [sky])

        renderer.render(perspective, camera, [ufo])

        # renderer.render(perspective, camera, [rock])
        # renderer.render(perspective, camera, [bridge])

        # working
        renderer.render(
            perspective, camera, [axe, helmet, ground, kaws, kaws2, rock, bridge, sky]
        )

        pygame.display.flip()
        end = time.perf_counter()
        frames += 1
        print(f"FPS: {frames / (end - start)}", end="\r")

    pygame.quit()
