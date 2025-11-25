from manim import *

# -----------------------------------------------------
# Scene 1: The Geometric Vector
# -----------------------------------------------------
class GeometricVectorScene(Scene):
    def construct(self):
        
        geom_title = Tex("Geometric Vector").to_edge(UP) # Adds a title

        # Creates the coordinate system
        axes = NumberPlane(
            x_range=[-3, 3, 1],  #Specifies x-axis range
            y_range=[-3, 3, 1],  # y-axis range
            x_length=7,          # Visual width of the plane
            y_length=7,          # Visual height of the plane
            axis_config={"color": WHITE}, #sets basis to white
            background_line_style={ #alters background (color and stroke width)
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6}
        )

        # Create the vector
        vector = Vector([3, 2], color=WHITE, stroke_width=3.5) #Parameters are vector coords, color, and the thickeness of the arrow

        # Add a label for the vector
        vector_label = MathTex(r"\vec{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}") #Uses Latex to write the vectors column vector
        vector_label.next_to(vector.get_end(), RIGHT, buff=0.2)
        
        # Group all the diagram elements together
        geom_group = VGroup(axes, vector, vector_label)
        
        # Position the entire group under the title
        # This will automatically center it horizontally.
        geom_group.next_to(geom_title, DOWN, buff=0.5)

        # --- Animation ---
        self.play(Write(geom_title))
        self.play(Create(axes))
        self.play(
            GrowArrow(vector),
            Write(vector_label)
        )
        self.wait(2)
        # --- Uncreate Animation ---
        # Fades the animation out
        self.play(
            Unwrite(geom_title),
            Unwrite(vector_label),
            Uncreate(geom_group) # Uncreates axes and vector
        )
        self.wait(1)

# -----------------------------------------------------
# Scene 2: The Numerical Vector
# -----------------------------------------------------
class NumericalVectorScene(Scene):
    def construct(self):
        # Add a title, centered at the top
        num_title = Tex("Numerical Vector").to_edge(UP)
        
        # Create the matrix (an ordered list of arbitrary numbers)
        numerical_vector = Matrix([
            [4],
            [-1],
            [2.5]
        ], h_buff=1.5)
        
        # Position the matrix directly under the title
        # This will automatically center it.
        #numerical_vector.next_to(num_title, DOWN, buff=0.5)

        # --- Animation ---
        self.play(Write(num_title))
        self.play(Create(numerical_vector))
        self.wait(2)

        # --- Uncreate Animation ---
        self.play(
            Unwrite(num_title),
            Uncreate(numerical_vector)
        )
        self.wait(1)

# -----------------------------------------------------
# Scene 3: Examples of Vector on Coordinate Plane
# -----------------------------------------------------

class PlotVectors(Scene):
        def construct(self):
            axes = NumberPlane(
                  axis_config={"color": WHITE}, #sets basis to white
            background_line_style={ #alters background (color and stroke width)
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6}
        )
            #Define and label da vectors
            vector_1 = Vector([1,2], stroke_width=3.5)
            vector_2 = Vector([-5,-2], stroke_width=3.5)
            vector_3 = Vector([4,0], stroke_width=3.5)
            label_1 = vector_1.coordinate_label()
            label_2 = vector_2.coordinate_label()
            label_3 = vector_3.coordinate_label()

            #animate them jawnsons
            self.play(Create(axes))
            self.play(
            GrowArrow(vector_1),
            Write(label_1)
            )
            self.wait(.5)
            self.play(
            GrowArrow(vector_2),
            Write(label_2)
            )
            self.wait(.5)
            self.play(
            GrowArrow(vector_3),
            Write(label_3)
            )
            self.wait(2)


class SuperpositionPrinciples(Scene):
    def construct(self):
        title = Tex("The Superposition Principles").to_edge(UP) # title
        scalar_title = Tex("Scalar Multiplication").next_to(title, DOWN, buff=1).shift(LEFT * 4)
        addition_title = Tex("Vector Addition").next_to(title, DOWN, buff = 1).shift(RIGHT * 4)
        scalar_eq = MathTex(
            r"c \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} c v_1 \\ c v_2 \end{bmatrix}" #describes scalar multiplication
        ).next_to(scalar_title, DOWN, buff=.5)
        addition_eq = MathTex(
        r"\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} + \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} v_1 + w_1 \\ v_2 + w_2 \end{bmatrix}" #describes vector addition 
        ).next_to(addition_title, DOWN, buff=0.5)

# --- Animation ---
        self.play(Write(title))
        self.play(Write(scalar_title))
        self.play(Write(addition_title))
        self.wait(1)
        self.play(Write(scalar_eq))
        self.play(Write(addition_eq))
        self.wait(5) #leave animations on screen
        
        # --- Uncreate Animation ---
        self.play(Unwrite(title), Unwrite(scalar_eq), Unwrite(scalar_title), Unwrite(addition_eq), Unwrite(addition_title))
        self.wait(1)