from manim import *
import numpy as np

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
        geom_group = VGroup(axes, vector)
        
        # Position the entire group under the title
        geom_group.next_to(geom_title, DOWN, buff=0.5)

        # --- Animation ---
        self.play(Write(geom_title))
        self.play(Create(axes))
        self.play(
            GrowArrow(vector),
            Write(vector_label)
        )
        self.wait(2)
        self.wait(1.5)
        self.play(
            Rotate(vector, 3*PI/4, about_point=ORIGIN) #rotates the vector 3pi/4 radians about the origin
        )
        self.wait(1)
        self.wait(2)
        # Fades the animation out
        self.play(
            Unwrite(geom_title),
            Unwrite(vector_label),
            Uncreate(geom_group) # Uncreates axes and vector
        )
        self.wait(1)



class VectorTransformations(Scene):
    def construct(self):
        # create coordinate plane
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        self.add(plane)

        title = Text("Geometric Vectors", font_size=40).to_edge(UP)
        self.play(Write(title))
        
        #  create the Initial Vector
        # Vector v = [3, 1]
        v_coords = [3, 1, 0]
        vec = Arrow(ORIGIN, v_coords, color=YELLOW, buff=0)
        
        self.play(GrowArrow(vec)) #growarrow is a function that animates a vector appearing from a point (origin default) extending from tail to tip 
        
        self.wait(4) 

        # Scalar Multiplication
        #scale_text = Text("Scaling: Multiply length, keep direction", font_size=24, color=GREEN).to_corner(UL)
        scaled_coords = [4, 1.33, 0] # 1.33 * [3, 1]
        vec_scaled = Arrow(ORIGIN, scaled_coords, color=GREEN, buff=0)
        
        #self.play(FadeIn(scale_text))
        self.play(
            Transform(vec, vec_scaled), #transform is a built in function. it replaces one mobject with another in a visually appealing manner
            run_time=2
        )
        
        self.wait(4)

        # Rotation
        #rotate_text = Text("Rotation: Change direction, keep length", font_size=24, color=RED).next_to(scale_text, DOWN, aligned_edge=LEFT)
        
        #self.play(FadeIn(rotate_text))
        
        # Rotate animation ONLY (separated from color change to prevent conflict)
        self.play(
            Rotate(vec, angle=3*PI/4, about_point=ORIGIN), #rotates 3pi/4 radians around the center of the screen
            run_time=2.5
        )
        
        # Change color to red after rotation completes
        self.play(vec.animate.set_color(RED), run_time=0.5)
        
        self.wait(4)
        
        self.play(FadeOut(Group(*self.mobjects)))



class NumericalVectorScene(Scene):
    def construct(self):
        num_title = Tex("Numerical Vectors").to_edge(UP)
        
        # Create the matrices
        #each number in brackets is associated with a vector coordinate
        numerical_vector = Matrix([
            [4],
            [-1],
            [2.5]
        ], h_buff=1.5)

        numerical_vector_2 = Matrix([
            [3],
            [7],
            [4]
        ], h_buff=1.5)

        numerical_vector_3 = Matrix([
            [3.7],
            [0],
            [3.2]
        ], h_buff=1.5)
        
 
        numerical_vector_2.next_to(numerical_vector, LEFT, buff=0.5) #the next_to function allows you to position an Mobject relative to another Mobject
        numerical_vector_3.next_to(numerical_vector, RIGHT, buff=0.5) #buff is the buffer, how far do you want the Mobject to be from the anchor object

        # --- Animation ---
        self.play(Write(num_title))
        self.play(Create(numerical_vector))
        self.wait(1)
        self.play(Create(numerical_vector_2))
        self.play(Create(numerical_vector_3))
        self.wait(2)

        # fade out
        self.play(
            Unwrite(num_title),
            Uncreate(numerical_vector_3)
        )
        self.play(Uncreate(numerical_vector_2))
        self.play(Uncreate(numerical_vector))
        self.wait(1)



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
        #This portion utilizes mathtex to write on the screen in a nice font
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
        
        # fade out
        self.play(Unwrite(title), Unwrite(scalar_eq), Unwrite(scalar_title), Unwrite(addition_eq), Unwrite(addition_title))
        self.wait(1)



class VectorScalingAndSpace(Scene):
    def construct(self):
        # Setup Plane
        plane = NumberPlane(
            background_line_style={#all of these parameters control the aesthetics of the plane
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        self.play(Create(plane), run_time=2) #run time is in seconds, essentially how long do you want the animation to take 
        
        # Animate first vector v
        v_coords = [2, 1, 0]
        v_vector = Vector(v_coords, color=YELLOW)
        v_label = MathTex(r"\vec{v}").next_to(v_vector.get_end(), RIGHT + UP)
        
        self.play(GrowArrow(v_vector), Write(v_label))
        self.wait(1)

        # Demonstrate Scalar Multiplication 
        scale_factor = 2   # Scale by 2
        scaled_v = Vector([x * scale_factor for x in v_coords], color=YELLOW) #new sclaed vector
        scale_label = MathTex(r"2 \cdot \vec{v}").next_to(scaled_v.get_end(), RIGHT + UP)
        
        self.play(
            Transform(v_vector, scaled_v),
            Transform(v_label, scale_label) #transform function fades from one mobject to the next
        )
        self.wait(1)

        # Scale by -1.5 (showing direction change)
        scale_factor_neg = -1.5
        neg_v = Vector([x * scale_factor_neg for x in v_coords], color=RED)
        neg_label = MathTex(r"-1.5 \cdot \vec{v}").next_to(neg_v.get_end(), LEFT + DOWN) #text next to vector
        
        self.play(
            Transform(v_vector, neg_v),
            Transform(v_label, neg_label)
        )
        self.wait(1) #hold the scene for a second

        # Show the Span of a Single Vector 
        # Explain that all scalings of v create a line
        span_line = Line(start=np.array(v_coords)*-10, end=np.array(v_coords)*10, color=YELLOW_A) #i use numpy to easily scale the coordinates of my vector, giving the illusion of a line spanning the screen
        span_text = Text("Span of one vector is a line", font_size=24).to_corner(UL)
        
        self.play(Create(span_line), Write(span_text))
        self.play(FadeOut(v_vector), FadeOut(v_label)) # Hide the specific instance
        self.wait(2)
        
        # Transition to Linear Combination (Building 2D Space)
        # Reset scene elements for Part 2
        self.play(
            FadeOut(span_line), 
            FadeOut(span_text)
        )
        
        # Define two basis vectors (linearly independent)
        v1 = Vector([2, 1, 0], color=GREEN) # original v
        v2 = Vector([-1, 2, 0], color=BLUE) # new vector w
        
        #labels
        v1_label = MathTex(r"\vec{v}").next_to(v1.get_end(), RIGHT) #get end returns the position of the vectors head
        v2_label = MathTex(r"\vec{w}").next_to(v2.get_end(), LEFT)
        
        self.play(GrowArrow(v1), Write(v1_label))
        self.play(GrowArrow(v2), Write(v2_label))
        
        # Show a linear combination: a*v + b*w
        a = 2
        b = 1
        
        # animate/visualize the components
        comp1 = Vector([2 * a, 1 * a, 0], color=GREEN_A).set_opacity(0.6)
        comp2 = Vector([-1 * b, 2 * b, 0], color=BLUE_A).set_opacity(0.6).shift(comp1.get_end())
        
        combo_vector = Vector(comp1.get_end() + comp2.get_end() - comp1.get_end(), color=PURPLE)
        combo_label = MathTex(r"2\vec{v} + 1\vec{w}").next_to(combo_vector.get_end(), UP)

        self.play(TransformFromCopy(v1, comp1))
        self.play(TransformFromCopy(v2, comp2))
        self.play(GrowArrow(combo_vector), Write(combo_label))
        self.wait(1)
        
        # explainnn the planeeee
        # Highlight that ANY point on the plane can be reached this way
        final_text = Text("Linear combinations of independent vectors\ncreate a 2D Vector Space (Plane)", font_size=30).to_edge(UP)
        plane_highlight = plane.copy().set_color(PURPLE).set_opacity(0.2)
        
        self.play(
            FadeOut(comp1), FadeOut(comp2), FadeOut(combo_vector), FadeOut(combo_label),
            FadeOut(v1), FadeOut(v2), FadeOut(v1_label), FadeOut(v2_label),
            FadeIn(plane_highlight),
            Write(final_text)
        )
        self.wait(2)



class DefineBasis(Scene):
    def construct(self):
        # create coord plane MObject
        plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        self.play(Create(plane), run_time=2)

        # Define Basis Vectors
        i_hat = Vector([1, 0, 0], color=GREEN)
        j_hat = Vector([0, 1, 0], color=RED)
        
        label_i = MathTex(r"\hat{i}").next_to(i_hat.get_end(), DOWN + RIGHT, buff=0.1)
        label_j = MathTex(r"\hat{j}").next_to(j_hat.get_end(), LEFT + UP, buff=0.1)
        
        self.play(GrowArrow(i_hat), Write(label_i))
        self.play(GrowArrow(j_hat), Write(label_j))

        # Title 
        def_text = Tex(r"The Unit Vectors $\hat{i}$ and $\hat{j}$ form the Basis").to_edge(UP)
        self.play(Write(def_text))
        self.wait(1)

        #constructing a vector with coordinates
        # show that vector v = [3, 2] is built from 3*i and 2*j
        x_val = 3
        y_val = 2
        v_values = [x_val, y_val, 0]
        
        v = Vector(v_values, color=YELLOW)
        v_label = MathTex(r"\vec{v} = 3\hat{i} + 2\hat{j}").next_to(v.get_end(), RIGHT)
        
        # Visualizing the "walk" (Linear Combination components)
        # Component along X (scaled i_hat)
        comp_i = Line(ORIGIN, RIGHT * x_val, color=GREEN, stroke_width=5).set_opacity(0.6)
        comp_i_arrow = Arrow(ORIGIN, RIGHT * x_val, color=GREEN, buff=0).set_opacity(0.6)
        
        # Component along Y (scaled j_hat, shifted)
        comp_j = Line(RIGHT * x_val, RIGHT * x_val + UP * y_val, color=RED, stroke_width=5).set_opacity(0.6)
        comp_j_arrow = Arrow(RIGHT * x_val, RIGHT * x_val + UP * y_val, color=RED, buff=0).set_opacity(0.6)

        # Animate the components being added
        self.play(Create(comp_i_arrow))
        self.play(Create(comp_j_arrow))
        
        # this shows the resulting vector
        self.play(GrowArrow(v), Write(v_label))
        self.wait(1)

        # explain that this works for any vector in the space
        final_text = Tex(r"Every vector in the plane is a linear combination of $\hat{i}$ and $\hat{j}$").to_edge(DOWN)
        self.play(Write(final_text))
        
        # fade animations
        self.play(
            FadeOut(comp_i_arrow), 
            FadeOut(comp_j_arrow),
            FadeOut(v),
            FadeOut(v_label)
        )
        self.wait(2)



class DotProduct(Scene):
    def construct(self):
        # creating the coord plane
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        self.add(plane)
        
        # dot product
        
        title_dot = Text("Dot Product", font_size=40).to_edge(UP)
        self.play(Write(title_dot))
        self.wait(1.5)
        self.play(FadeOut(title_dot))

        # Define vectors for Dot Product 
        # v along x-axis to make the projection (shadow) easy to see
        v_coords = [3, 0, 0]
        w_coords = [2, 2, 0] 
        
        arrow_v = Arrow(ORIGIN, v_coords, color=RED, buff=0)
        label_v = MathTex(r"\vec{v} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}", color=RED).next_to(arrow_v, DOWN)
        
        arrow_w = Arrow(ORIGIN, w_coords, color=BLUE, buff=0)
        label_w = MathTex(r"\vec{w} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}", color=BLUE).next_to(arrow_w, UP)
        
        self.play(GrowArrow(arrow_v), Write(label_v))
        self.play(GrowArrow(arrow_w), Write(label_w))
        self.wait(1)
        
        # Express the algebraic formula for dot products w/ LaTex
        calc_text = MathTex(
            r"\vec{v} \cdot \vec{w} = (v_x)(w_x) + (v_y)(w_y)",
            font_size=32
        ).to_corner(UL)
        
        # Plugging in numbers from the chosen example vectors
        calc_example = MathTex(
            r"= (3)(2) + (0)(2) = 6",
            font_size=32
        ).next_to(calc_text, DOWN, aligned_edge=LEFT)
        
        self.play(Write(calc_text))
        self.play(Write(calc_example))
        self.wait(1)
        
        # Geometric Interpretation (Projection)
        # Draw a dashed line dropping from w to v to show the "shadow"
        proj_point = [2, 0, 0]
        dashed_line = DashedLine(start=w_coords, end=proj_point, color=YELLOW) #dashed line Mobject
        
        # The "Shadow" vector (Projection)
        shadow_arrow = Arrow(ORIGIN, proj_point, color=YELLOW, buff=0, stroke_width=6)
        label_shadow = Text("Shadow (Length 2)", font_size=20, color=YELLOW).next_to(shadow_arrow, UP, buff=0.1)
        
        self.play(Create(dashed_line))
        self.play(GrowArrow(shadow_arrow), FadeIn(label_shadow))
        
        # Explanation Text
        geo_text = Text("Dot Product = (Length of Base) * (Length of Shadow)", font_size=24, color=YELLOW)
        geo_text.next_to(calc_example, DOWN, buff=0.5, aligned_edge=LEFT)
        
        geo_math = MathTex(r"3 \times 2 = 6", font_size=32, color=YELLOW)
        geo_math.next_to(geo_text, DOWN, aligned_edge=LEFT)
        
        self.play(Write(geo_text))
        self.play(Write(geo_math))
        
        self.wait(3)
        
        # Clear specific elements but keep plane and formula for continuity
        self.play(
            FadeOut(arrow_v), FadeOut(label_v),
            FadeOut(arrow_w), FadeOut(label_w),
            FadeOut(dashed_line), FadeOut(shadow_arrow), FadeOut(label_shadow),
            FadeOut(calc_example), FadeOut(geo_text), FadeOut(geo_math)
        )

        """
        Commented out because I did not use this part of the scene

        #title_ortho = Text("Orthogonal Dot Product", font_size=40, color=GREEN).to_edge(UP)
        #self.play(FadeOut(title_ortho))
        
        # New Vectors: Perpendicular
        v_ortho_coords = [3, 0, 0]
        w_ortho_coords = [0, 2, 0] # Straight up
        
        arrow_v_ortho = Arrow(ORIGIN, v_ortho_coords, color=RED, buff=0)
        label_v_ortho = MathTex(r"\vec{v} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}", color=RED).next_to(arrow_v_ortho, DOWN)
        
        arrow_w_ortho = Arrow(ORIGIN, w_ortho_coords, color=GREEN, buff=0)
        label_w_ortho = MathTex(r"\vec{w} = \begin{bmatrix} 0 \\ 2 \end{bmatrix}", color=GREEN).next_to(arrow_w_ortho, LEFT)
        
        self.play(GrowArrow(arrow_v_ortho), Write(label_v_ortho))
        self.play(GrowArrow(arrow_w_ortho), Write(label_w_ortho))
        
        # Right angle symbol
        right_angle = Square(side_length=0.4, color=WHITE).move_to([0.2, 0.2, 0])
        self.play(Create(right_angle))
        
        # Calculate Dot Product
        calc_ortho = MathTex(
            r"= (3)(0) + (0)(2) = 0",
            font_size=32
        ).next_to(calc_text, DOWN, aligned_edge=LEFT)
        
        self.play(Write(calc_ortho))
        self.wait(1)
        
        # Explain Shadow
        ortho_text = Text("The Shadow has length 0!", font_size=24, color=YELLOW)
        ortho_text.next_to(calc_ortho, DOWN, buff=0.5, aligned_edge=LEFT)
        
        # Visualize "dropping" the shadow
        # A dashed line going straight down the y-axis to the origin
        dashed_drop = DashedLine(start=w_ortho_coords, end=ORIGIN, color=YELLOW)
        
        self.play(Create(dashed_drop))
        self.play(Write(ortho_text))
        
        final_conclusion = Text("Dot Product = 0 implies 90° Angle", font_size=30, color=GREEN)
        final_conclusion.next_to(ortho_text, DOWN, buff=0.5)
        
        self.play(Write(final_conclusion))
        
        self.wait(4)
        self.play(FadeOut(Group(*self.mobjects)))
        """



class WorkIntegral(Scene):
    def construct(self):
        title = Text("Work as a Dot Product", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Prints the vector form of the work integral
        # W = integral F dot dr
        equation_vector = MathTex(#each element of the equation vector can be referenced as an array element
            r"W",                              # 0
            r"=",                              # 1
            r"\int",                           # 2
            r"\vec{F}",                        # 3
            r"\cdot",                          # 4
            r"d\vec{r}"                        # 5
        ).scale(1.5)

        self.play(Write(equation_vector))
        self.wait(2)

        # 3. The Scalar/Cosine Form
        # W = integral |F| |dr| cos(theta)
        equation_expanded = MathTex(
            r"W",                                      # 0
            r"=",                                      # 1
            r"\int",                                   # 2
            r"|\vec{F}|",                              # 3
            r"|d\vec{r}|",                             # 4
            r"\cos(\theta)"                            # 5
        ).scale(1.5)

        # Color the cosine part to highlight the angle dependence
        equation_expanded[5].set_color(YELLOW) #changing the cosine theta elements color w/ index 5

        self.play(
            TransformMatchingTex(equation_vector, equation_expanded),
            run_time=2
        )
        
        #  Explanation text
        explanation = Text(
            "Dot Product = Magnitudes × Cosine of angle", 
            font_size=24, 
            color=GREY
        ).next_to(equation_expanded, DOWN, buff=0.5)

        self.play(FadeIn(explanation))
        self.wait(2)
        
        # Clear scene
        self.play(FadeOut(Group(*self.mobjects)))

        # --- PHYSICS DEMO ---

        # create floor and box Mobjects
        floor = Line(start=[-6, -2, 0], end=[6, -2, 0], color=WHITE)
        box = Square(side_length=1.5, color=BLUE, fill_opacity=0.5).move_to([-4, -1.25, 0]) #choosing specific coordinates for box
        box_label = Text("Mass", font_size=20).move_to(box.get_center()) #places label in the center of the box
        
        self.play(Create(floor), FadeIn(box), Write(box_label))
        
        #  This function allows me to run the push simulation multiple times
        # the arguments are the angle at which the box is pushed, how far i want it to move, and the text that is displayed next to the angle and vector
        def run_push_scenario(angle_degrees, label_text, move_distance):
            angle_rad = angle_degrees * DEGREES
            
            # Create Force Vector
            # Start at center of box, point in direction of force
            # I draw the arrow pointing TO the box center to simulate pushing, 

            
            # Calculate start point relative to box based on angle
            force_len = 2.0
            # A vector pointing towards the box center from the left/top
            start_offset = [
                -force_len * np.cos(angle_rad), 
                force_len * np.sin(angle_rad), 
                0
            ]
            
            # Arrow ends at box center
            arrow_end = box.get_center()
            arrow_start = arrow_end + start_offset
            
            force_arrow = Arrow(start=arrow_start, end=arrow_end, color=RED, buff=0)
            force_label = MathTex(r"\vec{F}", color=RED).next_to(force_arrow.get_start(), UP)
            
            # Angle arc
            # Showing cosine component of angle (relative to horizontal)
            ref_line = DashedLine(start=arrow_start, end=arrow_start + [1, 0, 0], color=GREY)
            if angle_degrees > 0:
                angle_arc = Angle(ref_line, force_arrow, radius=0.5, other_angle=True)
                angle_tex = MathTex(f"{angle_degrees}^\circ", font_size=24).next_to(angle_arc, RIGHT)
            else:
                angle_arc = VGroup() # Empty
                angle_tex = VGroup()

            # Math display
            cos_val = np.cos(angle_rad)
            math_text = MathTex(
                r"W \propto \cos(" + str(angle_degrees) + r"^\circ) \approx " + f"{cos_val:.2f}",
                font_size=36, color=YELLOW
            ).to_edge(UP)

            # animate the intial conditions
            self.play(
                GrowArrow(force_arrow), 
                Write(force_label), 
                Write(math_text),
                Create(angle_arc),
                Write(angle_tex)
            )
            self.wait(1)

            # 2. Animate Movement
            if move_distance > 0.1:
                self.play(
                    box.animate.shift(RIGHT * move_distance),
                    box_label.animate.shift(RIGHT * move_distance),
                    force_arrow.animate.shift(RIGHT * move_distance),
                    force_label.animate.shift(RIGHT * move_distance),
                    # Fade out angle markers during move to avoid clutter
                    FadeOut(angle_arc), FadeOut(angle_tex),
                    rate_func=linear, #this parameter just means the speed the box moves is invariant  
                    run_time=2
                )
            else:
                # Shake effect for no movement
                self.play(Wiggle(box))
            
            self.wait(1)
            
            # 3. Reset for next scene
            self.play(
                FadeOut(force_arrow), FadeOut(force_label), 
                FadeOut(math_text), FadeOut(angle_arc), FadeOut(angle_tex),
                box.animate.move_to([-4, -1.25, 0]),
                box_label.animate.move_to([-4, -1.25, 0])
            )

        # SCENARIO 1: 0 Degrees (Efficient Push)
        run_push_scenario(0, "Parallel", 6)

        # SCENARIO 2: 45 Degrees (Inefficient Push)
        # Moves less distance in same time (simulating less acceleration)
        run_push_scenario(45, "Diagonal", 3.5)

        # SCENARIO 3: 90 Degrees (Pushing Down)
        # No movement
        run_push_scenario(90, "Perpendicular", 0)

        self.play(FadeOut(Group(*self.mobjects)))



class CrossProductMagic(ThreeDScene): #ThreeDScene has different functions and Mobjects than a normal manim Scene
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            z_length=6 # Adjusted for visual balance
        )
        
        # Title (Fixed in 2D overlay)
        title = Text("The Cross Product", font_size=40)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # --- DEFINING VECTORS ---
        
        # I chose vectors in the x-y plane so that it can be visually clear when I take the cross product in 3d
        # v = [2, 0, 0] (Red)
        # w = [1, 2, 0] (Blue)
        v_coords = [2, 0, 0]
        w_coords = [1, 2, 0]
        
        # Result of cross product: (2*2 - 0*1) = 4 in Z direction
        # cross = [0, 0, 4] (Green)
        cross_coords = [0, 0, 4]

        arrow_v = Arrow3D(start=ORIGIN, end=v_coords, color=RED)
        arrow_w = Arrow3D(start=ORIGIN, end=w_coords, color=BLUE)
        
        self.add(axes)
        
        # Move camera to a nice angle to see 3D structure
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Use Create instead of GrowArrow for 3D objects to avoid scale_tips error
        #This one took me forever to figure out lol....
        self.play(Create(arrow_v), Create(arrow_w))
        
        # Labeling vectors in 3D
        label_v = Text("v", color=RED).move_to([2.2, 0, 0])
        label_w = Text("w", color=BLUE).move_to([1, 2.2, 0])
        
        # Rotate labels to face camera
        self.add_fixed_orientation_mobjects(label_v)
        self.add_fixed_orientation_mobjects(label_w)
        self.play(FadeIn(label_v), FadeIn(label_w))
        self.wait(1)

        # --- Determinant/Parallelogram Animation ---
        
        explanation_1 = Text("Magnitude = Area of Parallelogram", font_size=24, color=YELLOW)
        explanation_1.to_corner(DL)
        self.add_fixed_in_frame_mobjects(explanation_1)
        self.play(Write(explanation_1))

        # Draw the parallelogram
        # Points: Origin -> v -> (v+w) -> w -> Origin
        parallelogram = Polygon(#Mobject that is drawn using vector component indices as reference points
            ORIGIN, 
            v_coords, 
            [v_coords[0] + w_coords[0], v_coords[1] + w_coords[1], 0], #I found that using the v and w coords is a convenient way to define my shapes size
            w_coords,
            fill_color=YELLOW, 
            fill_opacity=0.3, 
            stroke_opacity=0
        )
        
        self.play(FadeIn(parallelogram))
        self.wait(1)

        # 3D cross product/creating orthogonal vector
        
        explanation_2 = Text("Direction = Perpendicular (Right Hand Rule)", font_size=24, color=GREEN)
        explanation_2.next_to(explanation_1, UP, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(explanation_2)
        self.play(Write(explanation_2))

        # Show the cross product vector
        arrow_cross = Arrow3D(start=ORIGIN, end=cross_coords, color=GREEN)
        label_cross = Text("v x w", color=GREEN).move_to([0, 0, 4.2])
        self.add_fixed_orientation_mobjects(label_cross)

        # Use Create instead of GrowArrow :):):):):)
        self.play(Create(arrow_cross))
        self.play(Write(label_cross))
        
        # Rotate camera to emphasize the 90 degree angle
        self.begin_ambient_camera_rotation(rate=0.2) # Slow rotation
        self.wait(2)
        
        # Calculation overlay
        calc_box = Rectangle(height=2, width=5, fill_color=BLACK, fill_opacity=0.8, stroke_color=WHITE)
        calc_box.to_corner(UR)
        #chat, is that slang?
        calc_text = MathTex(
            r"\vec{v} &= \langle 2, 0, 0 \rangle \\",
            r"\vec{w} &= \langle 1, 2, 0 \rangle \\",
            r"|\vec{v} \times \vec{w}| &= (2)(2) - (0)(1) \\",
            r"&= 4",
            font_size=30
        ).move_to(calc_box.get_center())
        
        self.add_fixed_in_frame_mobjects(calc_box)
        self.add_fixed_in_frame_mobjects(calc_text)
        
        self.play(FadeIn(calc_box), Write(calc_text))
        self.wait(3)
        
        # Stop rotation and fade out
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(Group(*self.mobjects)))



class QuantumWave(Scene):
    def construct(self):
        # Title and Equations
        title = Text("Linear Algebra in Quantum Mechanics", font_size=36).to_edge(UP, buff=0.5)
        
        # Time-Dependent Schrodinger Equation
        tdse = MathTex(
            r"i\hbar \frac{\partial}{\partial t}\psi = \hat{H}\psi",
            font_size=40, color=BLUE
        ).next_to(title, DOWN)
        
        # Energy Eigenvalue Equation (Time-Independent)
        tise = MathTex(
            r"\hat{H}\psi = E\psi",
            font_size=40, color=GREEN
        ).next_to(tdse, DOWN)
        
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(tdse))
        self.play(Write(tise))
        self.wait(1)
        
        # Move equations to the corner to make space for the graph
        self.play(
            FadeOut(title),
            tdse.animate.to_corner(UL).scale(0.8),
        )
        self.play(tise.animate.next_to(tdse, DOWN, aligned_edge=LEFT).scale(0.8))
        
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": True, "color": GREY},
        ).shift(DOWN * 0.5)
        
        labels = axes.get_axis_labels(x_label="x", y_label=r"\psi(x)")
        
        self.play(Create(axes), Write(labels))
        
        # Animate Wave Packet
        # We visualize a "Wave Packet" which represents a localized particle
        # Formula: Gaussian envelope * Cosine carrier
        # psi(x,t) = exp(-1.5*(x-t)^2) * cos(5*(x-t))
        
        # ValueTracker controls the 'time' parameter (position of the packet)
        t_tracker = ValueTracker(-4)
        
        # always_redraw ensures the plot updates every frame based on t_tracker
        wave_packet = always_redraw(lambda: axes.plot(
            lambda x: np.exp(-1.5 * (x - t_tracker.get_value())**2) * np.cos(5 * (x - t_tracker.get_value())),
            color=YELLOW,
            x_range=[-6, 6] # Limit drawing range to axis size
        ))
        
        self.play(Create(wave_packet))
        
        # Animate the movement from left (t=-4) to right (t=4)
        self.play(
            t_tracker.animate.set_value(4),
            run_time=6,
            rate_func=linear #parameter for translational/rotational animations. Linear means it doesnt change w. time
        )
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))



class Outro(Scene):
    def construct(self):
        #if you cant figure out what this does then you havent been reading my other comments
        thanks_text = Text("Thanks for watching", font_size=50)
        self.play(Write(thanks_text))
        self.wait(3)
        Unwrite(thanks_text)    



class SneakPeek(ThreeDScene):
    def construct(self):
        # Create fixed title/matrix
        # fixed_in_frame keeps 2D objects in place when I change the camera angle to make the 3D camera move or looks at 3D objects.

        # Title
        title = Text("Sneak Peek", font_size=50, color=YELLOW).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        
        # 3D rotation Matrix Equation
        # represent a rotation around the Z-axis
        # R_z(theta) * v
        matrix_eq = MathTex(
            r"\begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}",
            r"\begin{bmatrix} x \\ y \\ z \end{bmatrix}",
            font_size=36
        )
        
        # Position it on the left side of the screen
        matrix_eq.to_edge(LEFT, buff=1)
        self.add_fixed_in_frame_mobjects(matrix_eq)
        
        # Add a label
        label = Text("Rotation Matrix", font_size=24, color=BLUE).next_to(matrix_eq, UP)
        self.add_fixed_in_frame_mobjects(label)
        
        # doin da 3D stuff
        
        # This shifts the 3D axes to the right so they don't overlap the matrix
        # Note to self: In ThreeDScene, shifting objects works better than shifting camera sometimes
        axes_origin = [3, -1, 0]
        
        axes = ThreeDAxes(
            x_length=5, y_length=5, z_length=4,
            axis_config={"include_tip": True}
        ).move_to(axes_origin)
        
        # Create a vector inside this coordinate system
        # Vector v = [2, 1, 1] relative to the axes origin
        vec_coords = [axes_origin[0] + 2, axes_origin[1] + 1, axes_origin[2] + 1]
        vector = Arrow3D(
            start=axes_origin, 
            end=vec_coords, 
            color=RED
        )
        
        # Group them so we can rotate the "Coordinate System" (Axes + Vector together)
        system = VGroup(axes, vector)
        
        self.add(axes, vector)
        
        # Animation
        # Set camera angle to see 3D depth
        self.move_camera(phi=60 * DEGREES, theta=-30 * DEGREES)
        self.play(Write(title), Write(matrix_eq), Write(label), Create(axes), Create(vector))
        
        # Rotate the coordinate system (around the Z-axis of the local system)
        # rotating about the axes_origin
        self.play(
            Rotate(
                system, 
                angle=2 * PI,           # Full 360 spin
                axis=OUT,               # Z-axis
                about_point=axes_origin # Spin around its own center, not global origin
            ),
            run_time=10,
            rate_func=linear #this just means that the speed of the spinning animation does not vary with time
        )