from OpenGL.GL import *
import pygame
import glm


# An object in 3D space, with a mesh, position, orientation (yaw/pitch/roll),
# and scale.
class Object3D:
    def __init__(
        self,
        mesh,
        position: glm.vec3 = glm.vec3(0.0, 0.0, 0.0),
        orientation: glm.vec3 = glm.vec3(0.0, 0.0, 0.0),
        scale: glm.vec3 = glm.vec3(1.0, 1.0, 1.0),
        center: glm.vec3 = glm.vec3(0, 0, 0),
        material: glm.vec4 = None,
    ):
        self.mesh = mesh
        self.position = position
        self.orientation = orientation
        self.scale = scale
        self.center = center
        self._refresh_model_matrix()
        self.children: list[Object3D] = []

        # Sets a value if not just sets a default value
        # (ambient, diffuse, specular, shininess)
        self.material = material or glm.vec4(1.0, 1.0, 1.0, 32.0)
        self.ambient_coe = self.material[0]
        self.diffuse_coe = self.material[1]
        self.specular_coe = self.material[2]
        self.shine = self.material[3]

        # animation
        self.velocity = glm.vec3(0, 0, 0)
        self.acceleration = glm.vec3(0, -9.8, 0)

        # Spotlight
        self.cutOff = 0
        # self.spotDir = glm.vec3(0, -1, 0)

        self.tex = None

    def move(self, offset: glm.vec3):
        """
        Moves the object along the given vector.
        """
        self.position = self.position + offset
        self._refresh_model_matrix()

    def rotate(self, rot: glm.vec3):
        """
        Adds the given yaw,pitch,roll values to the object's current orientation.
        """
        self.orientation = self.orientation + rot
        self._refresh_model_matrix()

    def grow(self, sc: glm.vec3):
        """
        Multiplies the object's current scale by the given x,y,z scale values.
        """
        self.scale = self.scale * sc
        self._refresh_model_matrix()

    def center_point(self, center: glm.vec3):
        self.center = center
        self._refresh_model_matrix()

    def get_position(self):
        return self.position

    def set_absolute_position(self, position: glm.vec3):
        self.position = position
        self._refresh_model_matrix()

    def set_absolute_orientation(self, orientation: glm.vec3):
        self.orientation = orientation
        self._refresh_model_matrix()

    def set_absolute_scale(self, scale: glm.vec3):
        self.scale = scale
        self._refresh_model_matrix()

    def get_model_matrix(self):
        """
        Retrieve the object's current Model transformation matrix.
        """
        return self.model_matrix

    def set_material(self, material: glm.vec4):
        self.material = material
        self.ambient_coe = self.material[0]
        self.diffuse_coe = self.material[1]
        self.specular_coe = self.material[2]
        self.shine = self.material[3]

    def change_tex(self, new_tex):
        new_tex = pygame.image.load(new_tex)
        new_tex = self.mesh.get_texture(new_tex)
        self.mesh.texture = new_tex

    # def set_spotlight(self, cutOff=12, spotDir=glm.vec3(0, -1, 0)):
    #     self.cutOff = cutOff
    #     self.spotDir = spotDir
    def set_spotlight(self, cutOff=12):
        self.cutOff = cutOff

    def get_bounding_box(self):
        width, height, depth = self.scale
        min_x = self.position[0] - width / 2
        max_x = self.position[0] + width / 2

        min_y = self.position[1] - height / 2
        max_y = self.position[1] + height / 2

        min_z = self.position[2] - depth / 2
        max_z = self.position[2] + depth / 2

        bounding_box = {
            "min_x": min_x,
            "max_x": max_x,
            "min_y": min_y,
            "max_y": max_y,
            "min_z": min_z,
            "max_z": max_z,
        }

        return bounding_box

    def impact_bounce(self, object2, bounce_speed=1.5):
        bounce_dir = glm.normalize(self.position - object2.position)
        self.velocity = bounce_dir * bounce_speed

    def graivty(self, delta_time):
        self.velocity += self.acceleration * delta_time

    def update(self, delta_time):
        self.position += self.velocity * delta_time
        self._refresh_model_matrix()

    def _is_vaid_x_overlap(self, object2):
        obj1_bounding_box = self.get_bounding_box()
        obj2_bounding_box = object2.get_bounding_box()

        max_x1 = obj1_bounding_box["max_x"]
        min_x1 = obj1_bounding_box["min_x"]

        max_x2 = obj2_bounding_box["max_x"]
        min_x2 = obj2_bounding_box["min_x"]

        if max_x1 >= min_x2 and min_x1 <= max_x2:
            return True
        else:
            return False

    def _is_vaid_y_overlap(self, object2):
        obj1_bounding_box = self.get_bounding_box()
        obj2_bounding_box = object2.get_bounding_box()

        max_y1 = obj1_bounding_box["max_y"]
        min_y1 = obj1_bounding_box["min_y"]

        max_y2 = obj2_bounding_box["max_y"]
        min_y2 = obj2_bounding_box["min_y"]

        if max_y1 >= min_y2 and min_y1 <= max_y2:
            return True
        else:
            return False

    def _is_vaid_z_overlap(self, object2):
        obj1_bounding_box = self.get_bounding_box()
        obj2_bounding_box = object2.get_bounding_box()

        max_z1 = obj1_bounding_box["max_z"]
        min_z1 = obj1_bounding_box["min_z"]

        max_z2 = obj2_bounding_box["max_z"]
        min_z2 = obj2_bounding_box["min_z"]

        if max_z1 >= min_z2 and min_z1 <= max_z2:
            return True
        else:
            return False

    def check_collision(self, object2):
        """
        Checks if the object is colliding with another object -> intersection of bounding boxes
        lets check for x,y,z for overlapping -> collision if all 3
        if max_x1 >= min_x2 and min_x1 <= max_x2
        """

        if (
            self._is_vaid_x_overlap(object2)
            and self._is_vaid_y_overlap(object2)
            and self._is_vaid_z_overlap(object2)
        ):
            return True
        else:
            return False

    def _refresh_model_matrix(self):
        m = glm.translate(glm.mat4(1), self.position)
        m = glm.translate(m, self.center * self.scale)
        m = glm.scale(m, self.scale)
        m = glm.rotate(m, self.orientation[2], glm.vec3(0, 0, 1))
        m = glm.rotate(m, self.orientation[0], glm.vec3(1, 0, 0))
        m = glm.rotate(m, self.orientation[1], glm.vec3(0, 1, 0))
        m = glm.translate(m, -self.center)

        self.model_matrix = m

    def add_child(self, child: "Object3D"):
        self.children.append(child)
        if child.material is not None:
            self.material = child.material
            self.ambient_coe = child.ambient_coe
            self.diffuse_coe = child.diffuse_coe
            self.specular_coe = child.specular_coe
            self.shine = child.shine

    def draw(self, renderer):
        self.draw_recursive(glm.mat4(1), renderer)

    def draw_recursive(self, parent_matrix, renderer):
        combined = parent_matrix * self.model_matrix
        renderer.set_uniform("model", glm.value_ptr(combined), glm.mat4)
        renderer.start_program()
        if self.mesh is not None:
            self.mesh.draw()

        for c in self.children:
            c.draw_recursive(combined, renderer)

    # def draw(self):
    #     self.mesh.draw()
