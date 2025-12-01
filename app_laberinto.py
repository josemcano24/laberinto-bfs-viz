import streamlit as st
import pandas as pd
import time
from maze_solver import MAZE, START, END, solve_maze_bfs

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")

# Función para renderizar el laberinto
def render_maze(maze, path=None):
    if path is None:
        path = []
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🚀") # Inicio
            elif (r_idx, c_idx) == END:
                display_row.append("🏁") # Fin
            elif (r_idx, c_idx) in path:
                display_row.append("🔹") # Camino resuelto
            elif col == 1:
                display_row.append("⬛") # Muro
            else:
                display_row.append("⬜") # Camino libre
        display_maze.append("".join(display_row))
    
    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


# Sidebar para controles
st.sidebar.header("Opciones")
# Se deja solo BFS habilitado y el resto como 'no implementado'
algorithm = st.sidebar.selectbox("Selecciona el algoritmo", ["BFS", "DFS (no implementado)", "A* (no implementado)"])
solve_button = st.sidebar.button("Resolver Laberinto")

st.subheader("Laberinto Actual")
render_maze(MAZE)

if solve_button:
    if algorithm == "BFS":
        # Iniciar cronómetro
        start_time = time.time()
        
        path = solve_maze_bfs(MAZE, START, END)
        
        # Detener cronómetro
        end_time = time.time()
        execution_time = end_time - start_time

        if path:
            st.success(f"¡Camino encontrado con {algorithm}!")
            st.write(f"⏱️ **Tiempo de ejecución:** {execution_time:.6f} segundos")
            
            st.subheader("Solución")
            render_maze(MAZE, path)
        else:
            st.error("No se encontró un camino.")
    else:
        st.warning(f"El algoritmo {algorithm} aún no está implementado. Usa BFS.")