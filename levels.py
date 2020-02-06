import pymunk


def create_moving_platforms(number, width, height):

    if number == 1:
        values = []
        # 1. moving platform
        pa = [(width * 0.942, height * 0.25), (width * 0.869, height * 0.5),
              (width * 0.942, height * 0.725), (width * 0.43478, height * 0.725),
              (width * 0.942, height * 0.725)]


        #Moving_Platform(speed=2, path=pa, x=self.width * 0.942, y=self.height * 0.25,
        #                x1=-self.width * 0.04, y1=0, x2=self.width * 0.04, y2=0, size=5, space=self.space)

        values.append([2, pa, width * 0.942, height * 0.25, -width * 0.04, 0, width * 0.04, 0, 5] )

        # 2.platform
        pa = [(500, 300), (200, 300)]
        #Moving_Platform(speed=2, path=pa, x=500, y=300, x1=-25, y1=0, x2=25, y2=0, size=5, space=self.space)
        values.append([2, pa, 500,300, -25,0,25,0,5])

        # add more platforms
        # ...

        return values
    if number == 2:
        print("making platforms for level 2")
        values = []
        pa = [(width * 0.942, height * 0.25), (width * 0.869, height * 0.5),
              (width * 0.942, height * 0.725), (width * 0.43478, height * 0.725),
              (width * 0.942, height * 0.725)]

        # Moving_Platform(speed=2, path=pa, x=self.width * 0.942, y=self.height * 0.25,
        #                x1=-self.width * 0.04, y1=0, x2=self.width * 0.04, y2=0, size=5, space=self.space)

        values.append([2, pa, width * 0.942, height * 0.25, -width * 0.04, 0, width * 0.04, 0, 5])

        # ...
        return values


def create_walls(number, space, width, height):
    # Pymunk has y coordinates from low to high (upwards)
    # Pygame has y coordinates from high to low (downwards)
    if number == 1:

        # box walls
        static = [
            pymunk.Segment(space.static_body, (width * 0.01449, height * 0.125), (width * 0.43478, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.43478, height * 0.125), (width * 0.47101, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.47101, height * 0.125), (width * 0.5072, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.5072, height * 0.125), (width * 0.543478, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.543478, height * 0.125), (width * 0.9855, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.9855, height * 0.125), (width * 0.9855, height * 0.925), 3)
            , pymunk.Segment(space.static_body, (width * 0.9855, height * 0.925), (width * 0.01449, height * 0.925), 3)
            , pymunk.Segment(space.static_body, (width * 0.01449, height * 0.925), (width * 0.01449, height * 0.125), 3)
            ]

        # paint some walls with colors
        static[1].color = (255, 0, 0)  # pygame.color.THECOLORS['red']
        static[2].color = (0, 255, 0)  # pygame.color.THECOLORS['green']
        static[3].color = (255, 0, 0)  # pygame.color.THECOLORS['red']

        # rounded shape
        rounded = [
            pymunk.Segment(space.static_body, (width * 0.7246, height * 0.125), (width * 0.753623, height * 0.15), 3)
            , pymunk.Segment(space.static_body, (width * 0.753623, height * 0.15), (width * 0.7826, height * 0.2), 3)
            , pymunk.Segment(space.static_body, (width * 0.7826, height * 0.2), (width * 0.7971, height * 0.25), 3)
            , pymunk.Segment(space.static_body, (width * 0.7971, height * 0.25), (width * 0.7971, height * 0.375), 3)
            ]

        # static platforms
        platforms = [pymunk.Segment(space.static_body, (170, height * 0.125), (270, height * 0.375), 3)
                     # , pymunk.Segment(space.static_body, (270, 100), (300, 100), 5)
            , pymunk.Segment(space.static_body, (width * 0.5797, height * 0.375), (width * 0.65217, height * 0.375), 3)
            , pymunk.Segment(space.static_body, (width * 0.5797, height * 0.5), (width * 0.65217, height * 0.5), 3)
            , pymunk.Segment(space.static_body, (width * 0.31884, height * 0.5), (width * 0.43478, height * 0.5), 3)
            , pymunk.Segment(space.static_body, (width * 0.07246, height * 0.625), (width * 0.289855, height * 0.625),
                             3)
            , pymunk.Segment(space.static_body, (width * 0.01449, height * 0.925), (width * 0.07246, height * 0.625), 3)
                     ]

        # -- set friction and group for elements ---             ]
        for s in static + platforms + rounded:
            s.friction = 1.
            s.group = 1
        space.add(static, platforms + rounded)

        # goal platform
        static.append(pymunk.Segment(space.static_body, (width - width * 0.14492, height * 0.925 - height * 0.175),
                                     (width - width * 0.07246, height * 0.925 - height * 0.175), 4))
        static[-1].color = (255, 255, 255)
        static[-1].friction = 1.
        static[-1].goup = 9
        static[-1].collision_type = 9
        space.add(static[-1])

        # pass through platform
        passthrough = pymunk.Segment(space.static_body, (width * 0.391, height * 0.25),
                                     (width * 0.463, height * 0.25), 5)
        passthrough.color = (0,255,255) #pygame.color.THECOLORS["yellow"]
        passthrough.friction = 1.
        passthrough.collision_type = 2
        passthrough.filter = pymunk.ShapeFilter(categories=0b1000)
        space.add(passthrough)

        # ------------------
        return space

    if number == 2:

        # box walls
        static = [
            pymunk.Segment(space.static_body, (width * 0.01449, height * 0.125), (width * 0.43478, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.43478, height * 0.125), (width * 0.47101, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.47101, height * 0.125), (width * 0.5072, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.5072, height * 0.125), (width * 0.543478, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.543478, height * 0.125), (width * 0.9855, height * 0.125), 3)
            , pymunk.Segment(space.static_body, (width * 0.9855, height * 0.125), (width * 0.9855, height * 0.925), 3)
            , pymunk.Segment(space.static_body, (width * 0.9855, height * 0.925), (width * 0.01449, height * 0.925), 3)
            , pymunk.Segment(space.static_body, (width * 0.01449, height * 0.925), (width * 0.01449, height * 0.125), 3)
            ]

        # paint some walls with colors
        static[1].color = (255, 0, 0)  # pygame.color.THECOLORS['red']
        static[2].color = (0, 255, 0)  # pygame.color.THECOLORS['green']
        static[3].color = (255, 0, 0)  # pygame.color.THECOLORS['red']

        # rounded shape
        rounded = [
            pymunk.Segment(space.static_body, (width * 0.7246, height * 0.125), (width * 0.753623, height * 0.15), 3)
            , pymunk.Segment(space.static_body, (width * 0.753623, height * 0.15), (width * 0.7826, height * 0.2), 3)
            , pymunk.Segment(space.static_body, (width * 0.7826, height * 0.2), (width * 0.7971, height * 0.25), 3)
            , pymunk.Segment(space.static_body, (width * 0.7971, height * 0.25), (width * 0.7971, height * 0.375), 3)
            ]

        # static platforms
        platforms = [pymunk.Segment(space.static_body, (170, height * 0.125), (270, height * 0.375), 3)
                     # , pymunk.Segment(space.static_body, (270, 100), (300, 100), 5)
            , pymunk.Segment(space.static_body, (width * 0.5797, height * 0.375), (width * 0.65217, height * 0.375), 3)
            , pymunk.Segment(space.static_body, (width * 0.5797, height * 0.5), (width * 0.65217, height * 0.5), 3)
            , pymunk.Segment(space.static_body, (width * 0.31884, height * 0.5), (width * 0.43478, height * 0.5), 3)
            , pymunk.Segment(space.static_body, (width * 0.07246, height * 0.625), (width * 0.289855, height * 0.625),
                             3)
            , pymunk.Segment(space.static_body, (width * 0.01449, height * 0.925), (width * 0.07246, height * 0.625), 3)
                     ]

        # -- set friction and group for elements ---             ]
        for s in static + platforms + rounded:
            s.friction = 1.
            s.group = 1
        space.add(static, platforms + rounded)

        # goal platform
        static.append(pymunk.Segment(space.static_body, (width - width * 0.14492, height * 0.925 - height * 0.175),
                                     (width - width * 0.07246, height * 0.925 - height * 0.175), 4))
        static[-1].color = (255, 255, 255)
        static[-1].friction = 1.
        static[-1].goup = 9
        static[-1].collision_type = 9
        space.add(static[-1])

        # pass-through platform(s)

        # pass through platform
        passthrough = pymunk.Segment(space.static_body, (width * 0.191, height * 0.25),
                                     (width * 0.363, height * 0.25), 10)
        passthrough.color = (255, 0, 255)  # pygame.color.THECOLORS["yellow"]
        passthrough.friction = 1.
        passthrough.collision_type = 2
        passthrough.filter = pymunk.ShapeFilter(categories=0b1000)
        space.add(passthrough)
        return space


if __name__ == "__main__":
    print("please start game.py")
