from manimlib.imports import *
from sympy.solvers import solve
from sympy.plotting import plot
from sympy import Symbol
class graphx(GraphScene):
    CONFIG={
        "x_axis_label":"$x$",
        "y_axis_label":"$y$",
        "x_min":-7,
        "x_max":7,
        "y_min":-7,
        "y_max":7,
        "x_labeled_nums":range(-6,7),
        "y_labeled_nums":range(-6,7),
        "axes_color":GREEN,
        }
    def get_graph_inv(
        self, func,
        color=None,
        y_min=None,
        y_max=None,
        **kwargs
    ):
        if color is None:
            color = next(self.default_graph_colors_cycle)
        if y_min is None:
            y_min = self.y_min
        if y_max is None:
            y_max = self.y_max

        def parameterized_function(alpha):
            y = interpolate(y_min, y_max, alpha)
            x = func(y)
            if not np.isfinite(x):
                x = self.x_max
            return self.coords_to_point(x, y)

        graph = ParametricFunction(
            parameterized_function,
            color=color,
            **kwargs
        )
        graph.underlying_function = func
        return graph



    def show(self,eq):
        self.setup_axes(animate=True)
        if 'y' in eq:
            y=Symbol('y')
            t=solve(eq,y)
            q=float(t[0])
            def func(x):
                return q
            graph=self.get_graph(func,x_min=-6,x_max=6)
        
        elif 'x' in eq:
            x=Symbol('x')
            t=solve(eq,x)
            q=float(t[0])
            def func(y):
                return q
            graph=self.get_graph_inv(func,y_min=-6,y_max=6)
        

        graph_lab=self.get_graph_label(graph,label=eq+"=0")
        graph.set_color(ORANGE)
        self.play(ShowCreation(graph),Write(graph_lab))
        self.wait(5)
    
    def construct(self):
         eq="2*y-4"
         self.show(eq)
