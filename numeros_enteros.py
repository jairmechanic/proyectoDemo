from manim import *

class NumerosEnteros(Scene):
    def construct(self):
        # Título principal
        titulo = Text("Los Números Enteros", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        # PROBLEMA 1
        self.problema_1()
        self.wait(1)

        # SOLUCIÓN 1
        self.solucion_1()
        self.wait(1)

        # PROBLEMA PEOR
        self.problema_peor()
        self.wait(1)

        # SOLUCIÓN DEFINITIVA
        self.solucion_definitiva()
        self.wait(2)

    def problema_1(self):
        """Presenta el primer problema: necesidad de contar"""
        seccion = Text("Problema 1", font_size=40, color=RED)
        seccion.to_edge(UP)
        self.play(Write(seccion))
        self.wait(0.5)

        # Contexto del problema
        problema_texto = Text(
            "María tiene 5 manzanas y Juan le da 3 más.\n¿Cuántas tiene ahora?",
            font_size=30
        )
        self.play(Write(problema_texto))
        self.wait(1.5)

        # Visualización con manzanas
        self.play(FadeOut(problema_texto))

        # Manzanas de María (5)
        manzanas_maria = VGroup(*[
            Circle(radius=0.3, color=RED, fill_opacity=0.7).shift(RIGHT * i * 0.7)
            for i in range(5)
        ]).shift(UP)

        label_maria = Text("María: 5", font_size=24).next_to(manzanas_maria, DOWN)

        self.play(
            LaggedStart(*[GrowFromCenter(m) for m in manzanas_maria], lag_ratio=0.2),
            Write(label_maria)
        )
        self.wait(1)

        # Manzanas de Juan (3)
        manzanas_juan = VGroup(*[
            Circle(radius=0.3, color=GREEN, fill_opacity=0.7).shift(RIGHT * i * 0.7)
            for i in range(3)
        ]).shift(DOWN)

        label_juan = Text("Juan da: 3", font_size=24).next_to(manzanas_juan, DOWN)

        self.play(
            LaggedStart(*[GrowFromCenter(m) for m in manzanas_juan], lag_ratio=0.2),
            Write(label_juan)
        )
        self.wait(1)

        # Operación matemática
        operacion = MathTex("5", "+", "3", "=", "8", font_size=48)
        operacion.shift(DOWN * 2)
        operacion[0].set_color(RED)
        operacion[2].set_color(GREEN)
        operacion[4].set_color(YELLOW)

        self.play(Write(operacion))
        self.wait(1)

        # Limpiar
        self.play(
            *[FadeOut(mob) for mob in [
                seccion, manzanas_maria, manzanas_juan,
                label_maria, label_juan, operacion
            ]]
        )

    def solucion_1(self):
        """Primera solución: números naturales"""
        seccion = Text("Solución 1", font_size=40, color=GREEN)
        seccion.to_edge(UP)
        self.play(Write(seccion))
        self.wait(0.5)

        # Explicación
        explicacion = Text(
            "Los números naturales nos permiten contar\ny sumar cantidades positivas",
            font_size=28
        )
        self.play(Write(explicacion))
        self.wait(1.5)
        self.play(FadeOut(explicacion))

        # Recta de números naturales
        naturales_titulo = Text("Números Naturales (ℕ)", font_size=32, color=BLUE)
        naturales_titulo.shift(UP * 2)
        self.play(Write(naturales_titulo))

        # Crear la recta numérica
        linea = Line(LEFT * 5, RIGHT * 3, color=WHITE)
        self.play(Create(linea))

        # Puntos y números
        puntos = VGroup()
        numeros = VGroup()

        for i in range(9):
            punto = Dot(linea.point_from_proportion(i/8), color=YELLOW)
            numero = MathTex(str(i), font_size=32).next_to(punto, DOWN)
            puntos.add(punto)
            numeros.add(numero)

        self.play(
            LaggedStart(*[GrowFromCenter(p) for p in puntos], lag_ratio=0.1),
            LaggedStart(*[Write(n) for n in numeros], lag_ratio=0.1)
        )

        # Ejemplos de operaciones que funcionan
        ejemplos = VGroup(
            MathTex("2 + 3 = 5", color=GREEN),
            MathTex("7 + 1 = 8", color=GREEN),
            MathTex("0 + 4 = 4", color=GREEN)
        ).arrange(DOWN, buff=0.3).shift(UP * 0.5 + RIGHT * 4)

        self.play(Write(ejemplos))
        self.wait(2)

        # Limpiar
        self.play(
            *[FadeOut(mob) for mob in [
                seccion, naturales_titulo, linea, puntos, numeros, ejemplos
            ]]
        )

    def problema_peor(self):
        """El problema que no se puede resolver con naturales"""
        seccion = Text("Problema Peor", font_size=40, color=RED, weight=BOLD)
        seccion.to_edge(UP)
        self.play(Write(seccion))
        self.wait(0.5)

        # Nuevo contexto
        problema_texto = Text(
            "Pedro tiene 3 euros y debe pagar 5 euros.\n¿Cuánto le falta?",
            font_size=30
        )
        self.play(Write(problema_texto))
        self.wait(2)
        self.play(FadeOut(problema_texto))

        # Intentar resolver con números naturales
        operacion = MathTex("3", "-", "5", "=", "?", font_size=60)
        operacion[0].set_color(BLUE)
        operacion[4].set_color(RED)
        self.play(Write(operacion))
        self.wait(1)

        # Marca de error
        cruz = VGroup(
            Line(UP + LEFT, DOWN + RIGHT, color=RED, stroke_width=8),
            Line(UP + RIGHT, DOWN + LEFT, color=RED, stroke_width=8)
        ).scale(0.5).next_to(operacion, RIGHT)

        self.play(Create(cruz))
        self.wait(0.5)

        # Mensaje de problema
        problema_msg = Text(
            "¡No existe en los números naturales!",
            font_size=32,
            color=RED,
            weight=BOLD
        ).shift(DOWN * 2)

        self.play(Write(problema_msg))
        self.wait(1)

        # Mostrar la recta incompleta
        self.play(
            FadeOut(operacion),
            FadeOut(cruz),
            FadeOut(problema_msg)
        )

        recta = NumberLine(
            x_range=[0, 8, 1],
            length=8,
            include_numbers=True,
            color=BLUE
        )

        pregunta = Text("¿Y los números menores que 0?", font_size=32, color=YELLOW)
        pregunta.shift(DOWN * 2)

        self.play(Create(recta))
        self.play(Write(pregunta))
        self.wait(2)

        # Limpiar
        self.play(
            *[FadeOut(mob) for mob in [seccion, recta, pregunta]]
        )

    def solucion_definitiva(self):
        """La solución: números enteros"""
        seccion = Text("Solución Definitiva", font_size=40, color=GOLD, weight=BOLD)
        seccion.to_edge(UP)
        self.play(Write(seccion))
        self.wait(0.5)

        # Introducción a los enteros
        intro = Text(
            "¡Los Números Enteros (ℤ)!",
            font_size=36,
            color=GOLD,
            weight=BOLD
        )
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))

        # Recta numérica completa con negativos
        recta = NumberLine(
            x_range=[-5, 5, 1],
            length=12,
            include_numbers=True,
            color=WHITE,
            font_size=28
        )

        self.play(Create(recta))

        # Destacar el cero
        cero = Circle(radius=0.2, color=YELLOW, stroke_width=4).move_to(recta.n2p(0))
        cero_label = Text("Cero", font_size=24, color=YELLOW).next_to(cero, DOWN, buff=0.5)

        self.play(Create(cero), Write(cero_label))
        self.wait(0.5)

        # Destacar positivos
        positivos_brace = Brace(Line(recta.n2p(0), recta.n2p(5)), UP, color=GREEN)
        positivos_label = Text("Positivos", font_size=24, color=GREEN).next_to(positivos_brace, UP)

        self.play(GrowFromCenter(positivos_brace), Write(positivos_label))
        self.wait(0.5)

        # Destacar negativos
        negativos_brace = Brace(Line(recta.n2p(-5), recta.n2p(0)), UP, color=RED)
        negativos_label = Text("Negativos", font_size=24, color=RED).next_to(negativos_brace, UP)

        self.play(GrowFromCenter(negativos_brace), Write(negativos_label))
        self.wait(1)

        # Resolver el problema anterior
        self.play(
            FadeOut(positivos_brace), FadeOut(positivos_label),
            FadeOut(negativos_brace), FadeOut(negativos_label),
            FadeOut(cero), FadeOut(cero_label)
        )

        solucion = MathTex("3", "-", "5", "=", "-2", font_size=50)
        solucion[0].set_color(BLUE)
        solucion[4].set_color(RED)
        solucion.shift(DOWN * 2)

        self.play(Write(solucion))

        # Animación en la recta
        punto_inicio = Dot(recta.n2p(3), color=BLUE, radius=0.15)
        punto_inicio_label = MathTex("3", color=BLUE, font_size=32).next_to(punto_inicio, UP)

        self.play(GrowFromCenter(punto_inicio), Write(punto_inicio_label))
        self.wait(0.5)

        # Flecha moviéndose hacia la izquierda
        flecha = Arrow(
            recta.n2p(3), recta.n2p(-2),
            buff=0,
            color=YELLOW,
            stroke_width=6
        )
        flecha_label = Text("-5", font_size=28, color=YELLOW).next_to(flecha, UP, buff=0.1)

        self.play(GrowArrow(flecha), Write(flecha_label))
        self.wait(0.5)

        # Punto final
        punto_final = Dot(recta.n2p(-2), color=RED, radius=0.15)
        punto_final_label = MathTex("-2", color=RED, font_size=32).next_to(punto_final, UP)

        self.play(
            GrowFromCenter(punto_final),
            Write(punto_final_label)
        )
        self.wait(1)

        # Checkmark de éxito
        check = VGroup(
            Line(ORIGIN, RIGHT * 0.3 + DOWN * 0.3, color=GREEN, stroke_width=8),
            Line(RIGHT * 0.3 + DOWN * 0.3, RIGHT * 0.8 + UP * 0.5, color=GREEN, stroke_width=8)
        ).next_to(solucion, RIGHT, buff=0.5)

        self.play(Create(check))
        self.wait(1)

        # Mensaje final
        self.play(
            *[FadeOut(mob) for mob in [
                punto_inicio, punto_inicio_label, flecha, flecha_label,
                punto_final, punto_final_label, solucion, check
            ]]
        )

        mensaje_final = VGroup(
            Text("Los Números Enteros incluyen:", font_size=32),
            MathTex(r"\mathbb{Z} = \{..., -3, -2, -1, 0, 1, 2, 3, ...\}", font_size=36, color=GOLD),
            Text("¡Ahora podemos restar cualquier número!", font_size=28, color=GREEN)
        ).arrange(DOWN, buff=0.5).shift(DOWN * 1.5)

        self.play(Write(mensaje_final))
        self.wait(2)

        # Fade out final
        self.play(
            *[FadeOut(mob) for mob in [seccion, recta, mensaje_final]]
        )
