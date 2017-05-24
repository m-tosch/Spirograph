from spirograph import Spirograph

def main():

    # create a new Spirograph with R = 200
    my_spirograph = Spirograph(200)

    # draw a curve
    my_spirograph.setSmallCircle(35)
    my_spirograph.setPen(0.65, 'purple')
    my_spirograph.draw()

    # clear screen
    my_spirograph.clear()

    # draw another curve
    my_spirograph.setSmallCircle(150)
    my_spirograph.setPen(0.55, 'red')
    my_spirograph.draw()

    # exit when user clicks inside the window
    my_spirograph.turtle.getscreen().exitonclick()


if __name__ == '__main__':
    main()