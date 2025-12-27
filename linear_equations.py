from manim import *

class LinearEquations(Scene):
    def construct(self):
        # Title
        title = Text("Ecuaciones Lineales", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Definition
        definition = Text(
            "Una ecuación de primer grado con una variable",
            font_size=32,
            color=WHITE
        )
        definition.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(definition))
        self.wait(2)

        # General form
        self.play(FadeOut(definition))
        general_form = MathTex(
            "ax + b = 0",
            font_size=60,
            color=YELLOW
        )
        general_form.move_to(ORIGIN)
        self.play(Write(general_form))
        self.wait(2)

        # Solution formula
        self.play(general_form.animate.shift(UP * 1.5))

        solution_text = Text("Solución:", font_size=36, color=GREEN)
        solution_text.next_to(general_form, DOWN, buff=0.8)

        solution_formula = MathTex(
            "x = -\\frac{b}{a}",
            font_size=60,
            color=GREEN
        )
        solution_formula.next_to(solution_text, DOWN, buff=0.5)

        self.play(Write(solution_text))
        self.play(Write(solution_formula))
        self.wait(2)

        # Clear screen for example
        self.play(
            FadeOut(general_form),
            FadeOut(solution_text),
            FadeOut(solution_formula)
        )

        # Example
        example_title = Text("Ejemplo:", font_size=40, color=ORANGE)
        example_title.to_edge(UP, buff=1.5)
        self.play(Write(example_title))

        # Original equation
        equation = MathTex(
            "2x + 6 = 0",
            font_size=60,
            color=WHITE
        )
        equation.move_to(ORIGIN)
        self.play(Write(equation))
        self.wait(2)

        # Step 1: Subtract 6 from both sides
        step1_text = Text("Paso 1: Restamos 6 de ambos lados", font_size=28, color=BLUE)
        step1_text.to_edge(DOWN, buff=1)
        self.play(Write(step1_text))

        equation_step1 = MathTex(
            "2x + 6 - 6 = 0 - 6",
            font_size=60,
            color=WHITE
        )
        equation_step1.move_to(ORIGIN)
        self.play(Transform(equation, equation_step1))
        self.wait(2)

        # Step 2: Simplify
        self.play(FadeOut(step1_text))
        step2_text = Text("Paso 2: Simplificamos", font_size=28, color=BLUE)
        step2_text.to_edge(DOWN, buff=1)
        self.play(Write(step2_text))

        equation_step2 = MathTex(
            "2x = -6",
            font_size=60,
            color=WHITE
        )
        equation_step2.move_to(ORIGIN)
        self.play(Transform(equation, equation_step2))
        self.wait(2)

        # Step 3: Divide by 2
        self.play(FadeOut(step2_text))
        step3_text = Text("Paso 3: Dividimos entre 2", font_size=28, color=BLUE)
        step3_text.to_edge(DOWN, buff=1)
        self.play(Write(step3_text))

        equation_step3 = MathTex(
            "\\frac{2x}{2} = \\frac{-6}{2}",
            font_size=60,
            color=WHITE
        )
        equation_step3.move_to(ORIGIN)
        self.play(Transform(equation, equation_step3))
        self.wait(2)

        # Final solution
        self.play(FadeOut(step3_text))
        solution_final_text = Text("¡Solución!", font_size=36, color=GREEN)
        solution_final_text.to_edge(DOWN, buff=1)
        self.play(Write(solution_final_text))

        equation_final = MathTex(
            "x = -3",
            font_size=80,
            color=GREEN
        )
        equation_final.move_to(ORIGIN)
        self.play(Transform(equation, equation_final))

        # Add a box around the solution
        box = SurroundingRectangle(equation_final, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(2)

        # Verification
        self.play(
            FadeOut(equation),
            FadeOut(box),
            FadeOut(solution_final_text),
            FadeOut(example_title)
        )

        verify_title = Text("Verificación:", font_size=40, color=PURPLE)
        verify_title.to_edge(UP, buff=1.5)
        self.play(Write(verify_title))

        verify_eq = MathTex(
            "2(-3) + 6 = 0",
            font_size=60,
            color=WHITE
        )
        verify_eq.move_to(ORIGIN + UP * 0.5)
        self.play(Write(verify_eq))
        self.wait(1)

        verify_calc = MathTex(
            "-6 + 6 = 0",
            font_size=60,
            color=WHITE
        )
        verify_calc.next_to(verify_eq, DOWN, buff=0.5)
        self.play(Write(verify_calc))
        self.wait(1)

        verify_final = MathTex(
            "0 = 0 \\quad \\checkmark",
            font_size=60,
            color=GREEN
        )
        verify_final.next_to(verify_calc, DOWN, buff=0.5)
        self.play(Write(verify_final))
        self.wait(2)

        # End
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        end_text = Text("¡Ecuaciones Lineales!", font_size=60, color=BLUE)
        self.play(Write(end_text))
        self.wait(2)
