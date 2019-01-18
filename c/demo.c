#include <OpenGL/gl.h>
#include <GLFW/glfw3.h>

int main(){
    GLFWwindow* window; 
    glfwInit();
    window = glfwCreateWindow(320, 240, "Demo", NULL, NULL);
    glfwMakeContextCurrent(window);
    glClearColor(0.1, 0.2, 0.3, 1.0);

    /* Loop until the user closes the window */
    while (!glfwWindowShouldClose(window))
    {
        
        glClear(GL_COLOR_BUFFER_BIT);

        // refresh display, double buffered
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    return 0;
}

