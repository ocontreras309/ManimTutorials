#################################################
# Source code for derivatives animation
# Final animation:
# https://www.youtube.com/watch?v=KMRK3soMV54
#################################################
#
# LICENSE:
# Copyright 2020 Oscar Contreras Carrasco
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
# and associated documentation files (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#################################################


from manimlib.imports import *


class DerivativeDefinition(GraphScene):
    graph_elements = {}

    def construct(self):
        self.setup_axes()
        self.axes.set_color(BLACK)

        self.graph_elements = {}
        self.__animate_intro()
        self.__show_intuition()
        self.__animate_graph_creation()
        self.__animate_line_coordinates()
        self.__move_graph_to_left()
        self.__show_slope_equation()
        self.__show_distances()
        self.__show_slope_definition()
        self.__bring_slope_equation_to_front()
        self.__setup_curve_equation()
        self.__draw_line_on_curve()
        self.__animate_candidate_slope()
        self.__transform_slope_equation_into_limit()
        self.__solve_for_derivative_of_x_squared()
        self.__show_other_derivatives()
        self.__show_innovacademy_ad()

    def __animate_intro(self):
        first_line = TexMobject("f'(x)")
        first_line.scale_in_place(2)
        first_line.set_y(1.5)

        second_line = TextMobject('Definición de Derivada')
        second_line.set_y(0.5)

        third_line = TextMobject('Por Oscar Contreras Carrasco')
        third_line.set_y(-1.5)

        fourth_line = ImageMobject('../MathCourses/resources/innovacademy_logo.png')
        fourth_line.scale_in_place(0.7)
        fourth_line.set_y(-2.5)

        self.play(FadeIn(first_line), FadeIn(second_line))
        self.wait(1)

        self.play(FadeIn(third_line), FadeIn(fourth_line))
        self.wait(5)

        self.play(FadeOut(first_line), FadeOut(second_line), FadeOut(third_line), FadeOut(fourth_line))
        self.wait(1)

    def __show_intuition(self):
        deriv1 = TextMobject('Derivada:', ' ', 'Pendiente de la tangente a la curva')
        deriv1.set_color_by_tex('Derivada:', RED)
        deriv1.set_x(-0.1)
        deriv1.set_y(2.5)

        deriv2 = TextMobject('evaluada en un punto dado.')
        deriv2.set_x(0.2)
        deriv2.set_y(2.0)

        pi_character = PiCreature(mode='plain')
        pi_character.set_y(-2)
        pi_character.set_x(-10)

        pi_character_bubble = ThoughtBubble()
        pi_character_bubble.scale_in_place(0.4)
        pi_character_bubble.set_x(-1.5)
        pi_character_bubble.set_y(0.5)

        bubble_text = TextMobject("???")
        bubble_text.set_x(-1.5)
        bubble_text.set_y(0.8)
        bubble_text.scale_in_place(1.5)

        self.play(FadeIn(deriv1), FadeIn(deriv2))
        self.wait(14)

        self.play(ApplyMethod(pi_character.shift, RIGHT * 6))
        self.play(Blink(pi_character), FadeIn(pi_character_bubble, run_time=0.5), FadeIn(bubble_text, run_time=0.5))
        self.wait(2)
        self.play(Blink(pi_character))
        self.play(Blink(pi_character))
        self.play(FadeOut(pi_character_bubble, run_time=0.5),
                  FadeOut(bubble_text, run_time=0.5))
        self.play(Blink(pi_character))
        self.wait(7)

        self.play(FadeOut(deriv1), FadeOut(deriv2), FadeOut(pi_character))
        self.wait(1)

    def __animate_graph_creation(self):
        animations = []

        x_axis = Arrow(np.array([-4, -2, 0]), np.array([4, -2, 0]))
        y_axis = Arrow(np.array([0, -4.0, 0]), np.array([0, 3, 0]))
        x_label = TexMobject("x")
        y_label = TexMobject("y")

        self.graph_elements['x_axis'] = x_axis
        self.graph_elements['y_axis'] = y_axis
        self.graph_elements['x_label'] = x_label
        self.graph_elements['y_label'] = y_label

        for i, x in enumerate(range(-3, 4)):
            vertical_line = Line(np.array([x, -4, 0]), np.array([x, 4, 0]), color=DARK_GREY)
            self.graph_elements[f'vertical_line{i}'] = vertical_line
            animations.append(FadeIn(vertical_line))

        for i, y in enumerate(range(-4, 4)):
            horizontal_line = Line(np.array([-4, y, 0]), np.array([4, y, 0]), color=DARK_GREY)
            self.graph_elements[f'horizontal_line{i}'] = horizontal_line
            animations.append(FadeIn(horizontal_line))

        animations.append(ShowCreation(x_axis))
        animations.append(ShowCreation(y_axis))
        animations.append(FadeIn(x_label))
        animations.append(FadeIn(y_label))

        x_label.set_x(4.0)
        x_label.set_y(-2.0)
        y_label.set_x(0.0)
        y_label.set_y(3.0)

        line = Line(np.array([-1.0, -4.0, 0]), np.array([2.5, 3, 0]), color=RED)
        line_equation = TexMobject("y", "=f(x)", "=", "m", "x", "+", "b")
        line_equation.set_x(-0.4)
        line_equation.set_y(1.5)

        self.graph_elements['line_equation'] = line_equation
        self.graph_elements['line'] = line

        self.play(*animations)
        self.wait(2)
        self.play(ShowCreation(line))
        self.wait(8)
        self.play(FadeIn(line_equation, run_time=0.5))
        self.wait(3)
        self.play(ApplyMethod(line_equation.set_color_by_tex, "m", BLUE, run_time=0.5))
        self.wait(5)

    def __animate_line_coordinates(self):
        point1 = Dot(np.array([1, 0, 0]))
        point2 = Dot(np.array([2, 2, 0]))

        coord1 = TextMobject("(1,2)")
        coord1.set_x(0.5)
        coord1.set_y(0.1)

        coord2 = TextMobject("(2,4)")
        coord2.set_x(1.5)
        coord2.set_y(2.3)

        vertices = [np.array([1, 0, 0]), np.array([2, 0, 0]), np.array([2, 2, 0])]
        slope_triangle = Polygon(*vertices, color=BLUE, fill_color=BLUE, fill_opacity=0.5)

        self.graph_elements['coord1'] = coord1
        self.graph_elements['coord2'] = coord2
        self.graph_elements['slope_triangle'] = slope_triangle

        horizontal_curly_brace = Brace(slope_triangle, DOWN)
        vertical_curly_brace = Brace(slope_triangle, RIGHT)

        deltax = TexMobject("\\Delta x")
        deltay = TexMobject("\\Delta y")

        deltax.set_x(1.5)
        deltax.set_y(-0.7)

        deltay.set_x(3.0)
        deltay.set_y(1)

        self.graph_elements['horizontal_curly_brace'] = horizontal_curly_brace
        self.graph_elements['vertical_curly_brace'] = vertical_curly_brace
        self.graph_elements['coord1'] = coord1
        self.graph_elements['coord2'] = coord2
        self.graph_elements['deltax'] = deltax
        self.graph_elements['deltay'] = deltay
        self.graph_elements['point1'] = point1
        self.graph_elements['point2'] = point2

        self.play(FadeIn(coord1), FadeIn(coord2), FadeIn(point1), FadeIn(point2))
        self.wait(3)

        self.play(FadeIn(slope_triangle))
        self.wait(3)

        self.play(FadeIn(horizontal_curly_brace), FadeIn(vertical_curly_brace),
                  FadeIn(deltax), FadeIn(deltay))
        self.wait(3)

    def __move_graph_to_left(self):
        self.play(*[ApplyMethod(element.shift, 4 * LEFT) for element in self.graph_elements.values()])
        self.wait(0.3)

    def __show_slope_equation(self):
        slope_equation = TexMobject('m={', '\\Delta y', '\\over', '\\Delta x', '}')
        slope_equation.set_x(2.5)
        slope_equation.set_y(2.5)
        slope_equation.set_color_by_tex('\\Delta y', YELLOW)
        slope_equation.set_color_by_tex('\\Delta x', RED)
        slope_equation.set_color_by_tex('m=', BLUE)

        deltay_equals2 = TextMobject('=2')
        deltax_equals1 = TextMobject('=1')

        deltay_equals2.set_x(-0.3)
        deltay_equals2.set_y(1)

        deltax_equals1.set_x(-1.7)
        deltax_equals1.set_y(-0.7)

        vertical_slope_line = Line(np.array([-2, 0, 0]), np.array([-2, 2, 0]), color=YELLOW)
        horizontal_slope_line = Line(np.array([-3, 0, 0]), np.array([-2, 0, 0]), color=RED)

        self.graph_elements['vertical_slope_line'] = vertical_slope_line
        self.graph_elements['horizontal_slope_line'] = horizontal_slope_line
        self.graph_elements['slope_equation'] = slope_equation

        self.play(FadeIn(slope_equation),
                  FadeIn(vertical_slope_line),
                  FadeIn(horizontal_slope_line),
                  ApplyMethod(self.graph_elements['deltay'].set_color, YELLOW),
                  ApplyMethod(self.graph_elements['deltax'].set_color, RED),
                  ApplyMethod(self.graph_elements['vertical_curly_brace'].set_color, YELLOW),
                  ApplyMethod(self.graph_elements['horizontal_curly_brace'].set_color, RED))

        self.wait(4)

        self.play(FadeIn(deltay_equals2, run_time=2))
        self.wait(1)

        self.play(FadeIn(deltax_equals1, run_time=2))
        self.wait(8)

        slope_calculation = TexMobject("m=\\frac 2 1=2")
        slope_calculation.set_x(2.7)
        slope_calculation.set_y(0.7)

        self.graph_elements['slope_calculation'] = slope_calculation

        self.play(FadeIn(slope_calculation))

        self.wait(10)
        self.play(FadeOut(deltay_equals2, run_time=2), FadeOut(deltax_equals1, run_time=2))
        self.wait(2)

    def __show_distances(self):
        self.play(FadeOut(self.graph_elements['coord1']), FadeOut(self.graph_elements['coord2']),
                  FadeOut(self.graph_elements['line_equation']))

        vertical_dashed_line1 = DashedLine(np.array([-3, -2, 0]), np.array([-3, 0, 0]))
        vertical_dashed_line2 = DashedLine(np.array([-2, -2, 0]), np.array([-2, 0, 0]))
        horizontal_dashed_line1 = DashedLine(np.array([-4, 0, 0]), np.array([-3, 0, 0]))
        horizontal_dashed_line2 = DashedLine(np.array([-4, 2, 0]), np.array([-2, 2, 0]))
        horizontal_dashed_line3 = DashedLine(np.array([-4, -2, 0]), np.array([-2, -2, 0]))
        horizontal_dashed_line3_brace = Brace(horizontal_dashed_line3, DOWN)
        horizontal_dashed_line3_label = TexMobject('x+\\Delta x')
        horizontal_dashed_line3_label.set_x(-3)
        horizontal_dashed_line3_label.set_y(-2.7)

        vertical_fx_deltax = DashedLine(np.array([-4, -2, 0]), np.array([-4, 2, 0]))
        vertical_fx_deltax_brace = Brace(vertical_fx_deltax, LEFT)
        vertical_fx_deltax_label = TexMobject('f(x+\\Delta x)')
        vertical_fx_deltax_label.set_x(-5.8)

        vertical_dashed_line2_brace = Brace(vertical_dashed_line2, RIGHT)
        vertical_dashed_line2_label = TexMobject('f(x)')
        vertical_dashed_line2_label.set_x(-1.0)
        vertical_dashed_line2_label.set_y(-1)
        
        horizontal_fx = DashedLine(np.array([-4, 0, 0]), np.array([-3, 0, 0]))
        horizontal_fx_brace = Brace(horizontal_fx, DOWN)
        horizontal_fx_label = TexMobject('x')
        horizontal_fx_label.set_x(-3.5)
        horizontal_fx_label.set_y(-0.7)

        self.graph_elements['vertical_dashed_line1'] = vertical_dashed_line1
        self.graph_elements['vertical_dashed_line2'] = vertical_dashed_line2
        self.graph_elements['horizontal_dashed_line1'] = horizontal_dashed_line1
        self.graph_elements['horizontal_dashed_line2'] = horizontal_dashed_line2
        self.graph_elements['horizontal_dashed_line3'] = horizontal_dashed_line3
        self.graph_elements['vertical_fx_deltax'] = vertical_fx_deltax
        self.graph_elements['vertical_fx_deltax_brace'] = vertical_fx_deltax_brace
        self.graph_elements['vertical_fx_deltax_label'] = vertical_fx_deltax_label
        self.graph_elements['vertical_dashed_line2_brace'] = vertical_dashed_line2_brace
        self.graph_elements['vertical_dashed_line2_label'] = vertical_dashed_line2_label
        self.graph_elements['horizontal_fx'] = horizontal_fx
        self.graph_elements['horizontal_fx_brace'] = horizontal_fx_brace
        self.graph_elements['horizontal_fx_label'] = horizontal_fx_label
        self.graph_elements['horizontal_dashed_line3_brace'] = horizontal_dashed_line3_brace
        self.graph_elements['horizontal_dashed_line3_label'] = horizontal_dashed_line3_label

        self.play(FadeIn(vertical_dashed_line1, run_time=0.5), FadeIn(vertical_dashed_line2, run_time=0.5),
                  FadeIn(horizontal_fx_brace, run_time=0.5), FadeIn(horizontal_fx_label, run_time=0.5),
                  FadeIn(horizontal_dashed_line3_brace, run_time=0.5),
                  FadeIn(horizontal_dashed_line3_label, run_time=0.5))

        self.wait(8)

        self.play(FadeIn(horizontal_dashed_line1, run_time=0.5), FadeIn(horizontal_dashed_line2, run_time=0.5),
                  FadeIn(vertical_fx_deltax_brace, run_time=0.5), FadeIn(vertical_fx_deltax_label, run_time=0.5),
                  FadeIn(vertical_dashed_line2_brace, run_time=0.5), FadeIn(vertical_dashed_line2_label, run_time=0.5))

        self.wait(16)

    def __show_slope_definition(self):
        delta_y_eq = TexMobject('\\Delta y', '=f(x+\\Delta x)', '-f(x)')
        delta_y_eq.set_x(3.5)
        delta_y_eq.set_y(-1.0)
        delta_y_eq.set_color_by_tex('\\Delta y', YELLOW)
        delta_y_eq.set_color_by_tex('=f(x+\\Delta x)', BLACK)
        delta_y_eq.set_color_by_tex('-f(x)', BLACK)

        arrow_deltay_replacement = Arrow(np.array([1.2, -1, 0]), np.array([3, 2.9, 0]))

        new_slope_equation = TexMobject('m={', '{f(x+\\Delta x)-f(x)}', '\\over', '\\Delta x', '}')
        new_slope_equation.set_x(3.5)
        new_slope_equation.set_y(-2.5)

        equation_box = Rectangle(width=5.3, height=1.5, color=RED)
        equation_box.set_x(3.5)
        equation_box.set_y(-2.5)

        circle_deltax = Ellipse(width=1.2, height=1.2, color=YELLOW)
        circle_deltax.set_x(-1)
        circle_deltax.set_y(1)

        circle_fx_deltax = Ellipse(width=2.5, height=1.2, color=GREEN)
        circle_fx_deltax.set_x(-5.8)

        circle_fx = Ellipse(width=1.2, height=1.2, color=BLUE)
        circle_fx.set_x(-1)
        circle_fx.set_y(-1)

        self.graph_elements['delta_y_eq'] = delta_y_eq
        self.graph_elements['new_slope_equation'] = new_slope_equation
        self.graph_elements['equation_box'] = equation_box
        self.graph_elements['circle_deltax'] = circle_deltax
        self.graph_elements['circle_fx_deltax'] = circle_fx_deltax
        self.graph_elements['circle_fx'] = circle_fx

        self.play(ShowCreation(circle_deltax))
        self.play(FadeIn(delta_y_eq, run_time=0.1))
        self.wait(4)

        self.play(ShowCreation(circle_fx_deltax))
        self.play(ApplyMethod(self.graph_elements['vertical_fx_deltax_brace'].set_color, GREEN, run_time=0.1),
                  ApplyMethod(self.graph_elements['vertical_fx_deltax_label'].set_color, GREEN, run_time=0.1),
                  ApplyMethod(delta_y_eq.set_color_by_tex, '=f(x+\\Delta x)', GREEN, run_time=0.1))
        self.wait(1)

        self.play(ShowCreation(circle_fx))
        self.play(ApplyMethod(self.graph_elements['vertical_dashed_line2_brace'].set_color, BLUE, run_time=0.1),
                  ApplyMethod(self.graph_elements['vertical_dashed_line2_label'].set_color, BLUE, run_time=0.1),
                  ApplyMethod(delta_y_eq.set_color_by_tex, '-f(x)', BLUE, run_time=0.1))

        self.wait(3)

        self.play(ShowCreation(arrow_deltay_replacement))
        self.wait(2)

        self.play(FadeIn(new_slope_equation), FadeOut(arrow_deltay_replacement))
        self.play(ShowCreation(equation_box))

    def __bring_slope_equation_to_front(self):
        equation_text = TextMobject('Ecuación de la pendiente')
        equation_text.set_y(1.5)

        elements_kept = ['new_slope_equation', 'equation_box']
        elements_removed = [key for key in self.graph_elements.keys()
                            if key not in (elements_kept + ['line_equation', 'coord1', 'coord2'])]

        fadeout_group = AnimationGroup(*[FadeOut(self.graph_elements[key]) for key in elements_removed])
        self.play(fadeout_group)
        self.play(*[ApplyMethod(self.graph_elements[element].shift, np.array([-3.5, 2.5, 0]))
                    for element in elements_kept])
        self.play(FadeIn(equation_text))
        self.wait(1)

        self.graph_elements['equation_text'] = equation_text

    def __setup_curve_equation(self):
        recovered_assets = []

        for i in range(7):
            recovered_assets.append(f'vertical_line{i}')

        for i in range(8):
            recovered_assets.append(f'horizontal_line{i}')

        recovered_assets += ['x_axis', 'y_axis', 'x_label', 'y_label']

        graph = self.get_graph(lambda x: (x - 1) ** 2 / 2 + 3, color=GREEN, x_min=-5, x_max=4)

        self.graph_elements['graph'] = graph

        self.play(FadeOut(self.graph_elements['equation_box']), FadeOut(self.graph_elements['equation_text']))
        self.play(ApplyMethod(self.graph_elements['new_slope_equation'].shift, np.array([4, 2, 0])))
        self.wait(0.3)

        self.play(*[FadeIn(self.graph_elements[key]) for key in recovered_assets])
        self.wait(1)

        self.play(ShowCreation(graph))
        self.wait(1)

    def __draw_line_on_curve(self):
        initial_alpha = 0.2
        max_alpha = 1.0
        stationary_alpha = 0.794

        tang_line = TangentLine(self.graph_elements['graph'], initial_alpha)
        tang_line.set_length(4)
        tangent_dot = Dot(tang_line.get_center())
        self.last_alpha = initial_alpha

        self.play(FadeIn(tang_line), FadeIn(tangent_dot))

        def rotate_tangent_line(line):
            R = self.x_axis.point_to_number(tangent_dot.get_center())
            line.set_angle(self.angle_of_tangent(R, self.graph_elements['graph']))
            line.move_to(tangent_dot)

        def animate_line(current_alpha):
            self.play(MoveAlongPath(tangent_dot, self.graph_elements['graph'],
                                    rate_func=lambda t: interpolate(self.last_alpha, current_alpha, smooth(t))),
                      UpdateFromFunc(tang_line, rotate_tangent_line), run_time=3)
            self.last_alpha = current_alpha

        animate_line(max_alpha)
        self.wait(2)

        animate_line(stationary_alpha)
        self.wait(2)

        line_on_curve = Line(np.array([-4, -1, 0]), np.array([-0.6, 1.58, 0]), color=RED)
        slope_triangle_curve = Polygon(np.array([-3.72, -0.78, 0]), np.array([-0.8, 1.4, 0]),
                                       np.array([-0.8, -0.78, 0]))
        slope_triangle_curve.set_color(BLUE)
        slope_triangle_curve.set_opacity(0.5)

        curve_deltax_brace = Brace(slope_triangle_curve, DOWN)
        curve_deltay_brace = Brace(slope_triangle_curve, RIGHT)

        curve_deltax = TexMobject('\\Delta x')
        curve_deltay = TexMobject('\\Delta y')

        curve_deltax.set_x(-2.2)
        curve_deltax.set_y(-1.5)

        curve_deltay.set_x(0.1)
        curve_deltay.set_y(0.3)

        self.graph_elements['tang_line'] = tang_line
        self.graph_elements['tangent_dot'] = tangent_dot
        self.graph_elements['line_on_curve'] = line_on_curve
        self.graph_elements['slope_triangle_curve'] = slope_triangle_curve
        self.graph_elements['curve_deltax_brace'] = curve_deltax_brace
        self.graph_elements['curve_deltay_brace'] = curve_deltay_brace
        self.graph_elements['curve_deltax'] = curve_deltax
        self.graph_elements['curve_deltay'] = curve_deltay

        self.play(ShowCreation(line_on_curve))
        self.play(FadeIn(slope_triangle_curve), FadeIn(curve_deltax_brace), FadeIn(curve_deltay_brace),
                  FadeIn(curve_deltax), FadeIn(curve_deltay))
        self.wait(9)

    def __animate_candidate_slope(self):
        self.play(FadeOut(self.graph_elements['line_on_curve']),
                  FadeOut(self.graph_elements['slope_triangle_curve']),
                  FadeOut(self.graph_elements['curve_deltax_brace']),
                  FadeOut(self.graph_elements['curve_deltay_brace']),
                  FadeOut(self.graph_elements['curve_deltax']),
                  FadeOut(self.graph_elements['curve_deltay']))
        self.wait(1)

        line_shifts = [
            0.5 * DOWN, 0.28 * DOWN
        ]

        triangles = [
            Polygon(np.array([-3.12, -0.85, 0]), np.array([-1.4, 0.48, 0]),
                    np.array([-1.4, -0.85, 0])),
            Polygon(np.array([-2.55, -0.7, 0]), np.array([-2, -0.7, 0]),
                    np.array([-2, -0.3, 0])),
        ]

        deltax_coords = [
            (-2.2, -1.5),
            (-2.3, -1)
        ]

        deltay_coords = [
            (-0.52, -0.28),
            (-1.58, -0.48)
        ]

        for i in range(len(line_shifts)):
            line_on_curve = self.graph_elements['line_on_curve']
            line_on_curve.shift(line_shifts[i])

            triangle = triangles[i]
            triangle.set_color(BLUE)
            triangle.set_opacity(0.5)

            curve_deltax = TexMobject('\\Delta x')
            curve_deltay = TexMobject('\\Delta y')

            curve_deltax.set_x(deltax_coords[i][0])
            curve_deltax.set_y(deltax_coords[i][1])

            curve_deltay.set_x(deltay_coords[i][0])
            curve_deltay.set_y(deltay_coords[i][1])

            self.graph_elements['curve_deltax'] = curve_deltax
            self.graph_elements['curve_deltay'] = curve_deltay

            if i == 0:
                horizontal_triangle_brace = Brace(triangle, DOWN)
                vertical_triangle_brace = Brace(triangle, RIGHT)

                self.graph_elements['curve_deltax_brace'] = horizontal_triangle_brace
                self.graph_elements['curve_deltay_brace'] = vertical_triangle_brace

                self.play(FadeIn(line_on_curve), FadeIn(triangle),
                          FadeIn(horizontal_triangle_brace), FadeIn(vertical_triangle_brace),
                          FadeIn(curve_deltax), FadeIn(curve_deltay))
                self.wait(3)
            else:
                self.play(FadeIn(line_on_curve), FadeIn(triangle),
                          FadeIn(curve_deltax), FadeIn(curve_deltay))
                self.wait(13)

            self.graph_elements['line_on_curve'] = line_on_curve
            self.graph_elements['slope_triangle_curve'] = triangle

            if i == 0:
                self.play(FadeOut(self.graph_elements['line_on_curve']),
                          FadeOut(triangle),
                          FadeOut(self.graph_elements['curve_deltax_brace']),
                          FadeOut(self.graph_elements['curve_deltay_brace']),
                          FadeOut(self.graph_elements['curve_deltax']),
                          FadeOut(self.graph_elements['curve_deltay']))

        deltax_trend = TexMobject('\\Delta x\\rightarrow 0')
        deltay_trend = TexMobject('\\Delta y\\rightarrow 0')

        self.graph_elements['deltax_trend'] = deltax_trend
        self.graph_elements['deltay_trend'] = deltay_trend

        deltax_trend.set_x(3)
        deltax_trend.set_y(0)

        deltay_trend.set_x(3)
        deltay_trend.set_y(-1)

        deltax_arrow = Arrow(np.array([2.7, 0.1, 0]), np.array([2, 2, 0]))

        self.graph_elements['deltax_arrow'] = deltax_arrow

        self.play(FadeIn(deltax_trend), FadeIn(deltay_trend))
        self.wait(4)

        self.play(ShowCreation(deltax_arrow))
        self.wait(3)

    def __transform_slope_equation_into_limit(self):
        animation_keys = ['line_on_curve', 'tang_line', 'tangent_dot', 'slope_triangle_curve',
                          'curve_deltax', 'curve_deltay', 'graph', 'deltax_arrow',
                          'deltax_trend', 'deltay_trend', 'x_axis', 'y_axis', 'x_label', 'y_label']
        animation_list = []

        for key in animation_keys:
            animation_list.append(FadeOut(self.graph_elements[key]))

        animation_list += [FadeOut(self.graph_elements[key]) for key
                           in self.graph_elements.keys() if key.startswith('horizontal_line')]
        animation_list += [FadeOut(self.graph_elements[key]) for key
                           in self.graph_elements.keys() if key.startswith('vertical_line')]

        self.play(*animation_list)

        self.play(ApplyMethod(self.graph_elements['new_slope_equation'].shift, np.array([-4, -2, 0])))
        self.wait(0.3)

        self.play(ApplyMethod(self.graph_elements['new_slope_equation'].set_color_by_tex, 'm=', BLACK))
        self.play(ApplyMethod(self.graph_elements['new_slope_equation'].shift, RIGHT * 1.4))

        derivative_as_limit = TexMobject("m=f'(x)=\\lim_{\\Delta x\\rightarrow 0}")
        derivative_as_limit.set_x(-2.0)
        derivative_as_limit.set_y(-0.1)

        equation_box = Rectangle(width=8.3, height=2, color=RED)
        equation_text = TextMobject('Definición de la derivada')
        equation_text.set_y(2)

        self.play(FadeIn(derivative_as_limit))
        self.wait(5)
        self.play(ShowCreation(equation_box))
        self.play(FadeIn(equation_text))

        self.graph_elements['equation_box'] = equation_box
        self.graph_elements['derivative_as_limit'] = derivative_as_limit
        self.graph_elements['equation_text'] = equation_text

        self.wait(5)

    def __solve_for_derivative_of_x_squared(self):
        fadeout_keys = ['equation_box', 'derivative_as_limit', 'equation_text', 'new_slope_equation']
        self.play(*[FadeOut(self.graph_elements[key]) for key in fadeout_keys])

        fx = TexMobject("f(x)=x^2\\qquad f'(x)=?")
        fx.set_y(3)

        self.play(FadeIn(fx))
        self.wait(6)

        fx_step1 = TexMobject("f'(x)=\\lim_{\\Delta x\\rightarrow 0}\\frac{f(x+\\Delta x)-f(x)}{\\Delta x}")
        fx_step1.set_x(-3)
        fx_step1.set_y(1.5)

        fx_step1_squares = TexMobject("=\\lim_{\\Delta x\\rightarrow 0}\\frac{(x+\\Delta x)^2-x^2}{\\Delta x}")
        fx_step1_squares.set_x(3.5)
        fx_step1_squares.set_y(1.5)

        fx_step1_ind = TexMobject("\\frac 0 0", color=RED)
        fx_step1_ind.set_x(4.7)
        fx_step1_ind.set_y(3)

        fx_step1_ind_arrow = Arrow(np.array([3.5, 2, 0]), np.array([4.7, 3, 0]))

        self.play(FadeIn(fx_step1))
        self.wait(2)

        self.play(FadeIn(fx_step1_squares))
        self.wait(10)

        self.play(ShowCreation(fx_step1_ind_arrow))
        self.play(FadeIn(fx_step1_ind))
        self.wait(9)

        self.play(FadeOut(fx_step1_ind_arrow), FadeOut(fx_step1_ind))
        self.wait(2)

        fx_step2 = TexMobject("f'(x)=\\lim_{\\Delta x\\rightarrow 0}\\frac{(x+\\Delta x+x)(x+\\Delta x-x)}{\\Delta x}")
        self.play(FadeIn(fx_step2))
        self.wait(8)

        fx_step3 = TexMobject("f'(x)=\\lim_{\\Delta x\\rightarrow 0}\\frac{(2x+\\Delta x)\\Delta x}{\\Delta x}")
        fx_step3.set_y(-1.5)
        self.play(FadeIn(fx_step3))
        self.wait(5)

        fx_step3_mark1 = Line(np.array([2.2, -1.4, 0]), np.array([3.1, -1.1, 0]), color=RED)
        fx_step3_mark2 = Line(np.array([1.1, -2.0, 0]), np.array([2.0, -1.7, 0]), color=RED)

        self.play(ShowCreation(fx_step3_mark1, run_time=0.5))
        self.play(ShowCreation(fx_step3_mark2, run_time=0.5))
        self.wait(6)

        fx_step4 = TexMobject("f'(x)=\\lim_{\\Delta x\\rightarrow 0}(2x+\\Delta x)=2x")
        fx_step4.set_y(-3)
        self.play(FadeIn(fx_step4))
        self.wait(6)

        self.play(FadeOut(fx), FadeOut(fx_step1), FadeOut(fx_step1_squares), FadeOut(fx_step2), FadeOut(fx_step3),
                  FadeOut(fx_step3_mark1), FadeOut(fx_step3_mark2), FadeOut(fx_step4))
        self.wait(2)

    def __show_other_derivatives(self):
        fx_xn = TexMobject("f(x)=x^n\\qquad f'(x)=?")
        fx_xn.set_x(-0.1)
        fx_xn.set_y(3)

        fx_lnx = TexMobject("f(x)=\\ln x\\qquad f'(x)=?")
        fx_lnx.set_x(-0.1)
        fx_lnx.set_y(1)

        fx_tanx = TexMobject("f(x)=\\tan x\\qquad f'(x)=?")
        fx_tanx.set_x(-0.1)
        fx_tanx.set_y(-1)

        fx_ex = TexMobject("f(x)=e^x\\qquad f'(x)=?")
        fx_ex.set_x(-0.1)
        fx_ex.set_y(-3)

        self.play(FadeIn(fx_xn), FadeIn(fx_lnx), FadeIn(fx_tanx), FadeIn(fx_ex))
        self.wait(9)
        self.play(FadeOut(fx_xn), FadeOut(fx_lnx), FadeOut(fx_tanx), FadeOut(fx_ex))

        self.wait(1)

    def __show_innovacademy_ad(self):
        innovacademy_logo = ImageMobject('../MathCourses/resources/innovacademy_logo.png')
        innovacademy_logo.set_y(0.5)
        innovacademy_logo.scale_in_place(0.01)

        self.play(ScaleInPlace(innovacademy_logo, scale_factor=100))
        ad_text = TextMobject("¡Inscríbete a nuestros cursos!")
        ad_text.set_y(-1.5)

        ad_link = TextMobject("www.innovacademy.com")
        ad_link.set_y(-2)

        self.play(FadeIn(ad_text), FadeIn(ad_link))

        self.wait(15)

        self.play(FadeOut(innovacademy_logo), FadeOut(ad_text), FadeOut(ad_link))
        self.wait(1)
