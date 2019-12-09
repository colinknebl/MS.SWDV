class Shape2D:
    def area(self):
        raise NotImplementedError('`area` method not implemented!')


class Square(Shape2D):

    def __init__(self, *args, **kwargs):
        super(Shape2D, self).__init__(*args, **kwargs)

    def area(self):
        print('area method is implemented!')


def main():
    square = Square()
    square.area()

main()