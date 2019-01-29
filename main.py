import glfw
from OpenGL.GL import *



def draw():
    pass


def main():
    # initialize GLFW
    if not glfw.init():
        print("GLFW could not initialize")
        return

    # create a window and test if it works
    window = glfw.create_window(800, 600, "simple Graphics implementation", None, None)
    if not window:
        print("Window could not initialize")
        glfw.terminate()
        return

    # create GL-Context and bind to the recently created window
    glfw.make_context_current(window)

    # Main Loop
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        draw()

        glfw.swap_buffers(window)

    # terminate GLFW at the end
    glfw.terminate()


if __name__ == "__main__":
    main()
