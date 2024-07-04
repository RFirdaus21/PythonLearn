import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Fungsi untuk menggambar kubus
def draw_cube(color):
    glBegin(GL_LINES)

    # Sisi depan
    glColor3fv(color)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # Sisi belakang
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)

    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    # Sisi-sisi vertikal
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)

    glEnd()

def main():
    # Inisialisasi GLFW
    if not glfw.init():
        print("Gagal menginisialisasi GLFW")
        return

    # Buat GLFW window
    window = glfw.create_window(800, 600, "Hierarchical Modeling OpenGL", None, None)
    if not window:
        glfw.terminate()
        print("Gagal membuat jendela GLFW")
        return

    # Atur konteks OpenGL
    glfw.make_context_current(window)

    # Inisialisasi OpenGL
    glClearColor(0.0, 0.0, 0.0, 1.0) # Warna latar belakang (hitam)

    # Inisialisasi GLU
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800/600), 0.1, 50.0) # Set perspektif

    # Loop utama
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Mulai menggambar dengan matriks identitas
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Gunakan stack matriks
        glPushMatrix()

        # Atur matriks transformasi untuk kubus induk
        glTranslatef(0.0, 0.0, -5.0) # Pindahkan ke posisi yang sesuai

        # Gambar kubus induk dengan warna merah
        draw_cube((1.0, 0.0, 0.0))

        # Atur transformasi untuk objek anak
        glTranslatef(1.5, 0.0, 0.0) # Pindahkan ke posisi yang sesuai

        # Simpan matriks transformasi saat ini ke dalam stack (untuk objek anak)
        child_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPushMatrix()

        # Atur matriks transformasi global dengan matriks transformasi dari stack
        glMultMatrixf(child_matrix)

        # Gambar kubus objek anak dengan warna hijau
        draw_cube((0.0, 1.0, 0.0))

        # Pop matriks transformasi dari stack (objek anak)
        glPopMatrix()

        # Pop matriks transformasi dari stack (kubus induk)
        glPopMatrix()

        # Tampilkan hasil render
        glfw.swap_buffers(window)

        # Periksa dan proses event
        glfw.poll_events()

    # Hentikan GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
