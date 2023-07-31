#!/usr/bin/python3

import open3d as o3d


class Renderer:
    def __init__(self, size):
        self.size = size
        self.init_window()
        self.init_scene()

    def init_window(self):
        self.app = o3d.visualization.gui.Application.instance
        self.app.initialize()
        self.main_viz = o3d.visualization.O3DVisualizer("Visualization", 1024, 1024)
        self.app.add_window(self.main_viz)
        
        self.main_viz.set_background([1, 1, 1, 1], None)
        center = self.size/2
        self.main_viz.setup_camera(60,
                                   [center, center, 0], # Center
                                   [center, center, self.size], # Camera position
                                   [0, 0, 1]) # Up

    def init_scene(self):
        self.size_x = self.size
        self.size_y = self.size
        self.size_z = 1

        # Define a default material
        default_mat = o3d.visualization.rendering.MaterialRecord()
        default_mat.shader = "defaultLit"
        default_mat.base_color = [0.5, 0.5, 0.5, 1.0]

        # Add grid lines to the scene
        line_points = []
        lines = []
        def add_line(start, end):
            line_points.append(start)
            line_points.append(end)
            point_start_idx = len(line_points)
            point_end_idx = point_start_idx + 1
            lines.append([point_start_idx, point_end_idx])
        for i in range(self.size_x + 1):
            for j in range(self.size_y + 1):
                for k in range(self.size_z + 1):
                    add_line([0, j, k], [self.size_x, j, k])
                    add_line([i, 0, k], [i, self.size_y, k])
                    add_line([i, j, 0], [i, j, self.size_z])
        colors = [[0, 0, 0] for i in range(len(lines))]
        line_set = o3d.geometry.LineSet(
            points=o3d.utility.Vector3dVector(line_points),
            lines=o3d.utility.Vector2iVector(lines),
        )
        line_set.colors = o3d.utility.Vector3dVector(colors)
        self.main_viz.add_geometry("lines", line_set, default_mat)

        # Add a coordinate frame to the scene
        mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(
            size=1.0, origin=[0, 0, 0])
        self.main_viz.add_geometry("coordinate_frame", mesh_frame, default_mat)

        # Initialize boxes
        def create_box():
            width = 1.0
            height = 1.0
            depth = 1.0
            box = o3d.geometry.TriangleMesh.create_box(
                width=width, height=height, depth=depth
            )
            box.compute_vertex_normals()
            box.translate((0.0, 0.0, 0.0))
            box.paint_uniform_color([0.2, 0.2, 0.2])
            return box
        def create_box_mat():
            mat = o3d.visualization.rendering.MaterialRecord()
            mat.shader = "defaultLit"
            mat.base_color = [0.0, 0.0, 0.0, 1.0]
            return mat
        self.boxes = [[[None for x in range(self.size_x)] for y in range(self.size_y)] for z in range(self.size_z)]
        self.materials = [[[None for x in range(self.size_x)] for y in range(self.size_y)] for z in range(self.size_z)]
        self.is_shown = [[[True for x in range(self.size_x)] for y in range(self.size_y)] for z in range(self.size_z)]
        for k in range(self.size_z):
            for j in range(self.size_y):
                for i in range(self.size_x):
                    # Copy template
                    box = create_box()
                    box.translate([i, j, k])
                    box_mat = create_box_mat()
                    # Keep a reference to the box and material
                    self.boxes[k][j][i] = box
                    self.materials[k][j][i] = box_mat
                    # Add the box to the scene
                    self.main_viz.add_geometry(f"box_{i}_{j}_{k}", box, box_mat)

    def render(self, state):
        for k in range(self.size_z):
            for j in range(self.size_y):
                for i in range(self.size_x):
                    show = state[k][j][i]
                    if show:
                        if not self.is_shown[k][j][i]:
                            self.is_shown[k][j][i] = True
                            self.main_viz.add_geometry(f"box_{i}_{j}_{k}", self.boxes[k][j][i], self.materials[k][j][i])
                    else:
                        if self.is_shown[k][j][i]:
                            self.is_shown[k][j][i] = False
                            self.main_viz.remove_geometry(f"box_{i}_{j}_{k}")
        
        # self.app = o3d.visualization.gui.Application.instance
        tick_return = self.app.run_one_tick()
        if tick_return:
            self.main_viz.post_redraw()



if __name__ == "__main__":
    renderer = Renderer(25)
    for i in range(100):
        renderer.render(None)
