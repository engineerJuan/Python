import tkinter as tk
from tkinter import messagebox
import calendar

def mostrar_calendario():
    for widget in frame_dias.winfo_children():
        widget.destroy()

    try:
        año = int(entry_año.get())
        mes = int(entry_mes.get())
        dia_destacado = entry_dia.get()
        dia_destacado = int(dia_destacado) if dia_destacado else None

        if not (1 <= mes <= 12):
            raise ValueError("Mes inválido. Debe estar entre 1 y 12.")

        cal = calendar.Calendar(firstweekday=0) 
        semanas = cal.monthdayscalendar(año, mes)

        dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for idx, nombre_dia in enumerate(dias_semana):
            tk.Label(frame_dias, text=nombre_dia, font=('Arial', 10, 'bold')).grid(row=0, column=idx, padx=5, pady=5)

        for fila, semana in enumerate(semanas, start=1):
            for col, dia in enumerate(semana):
                if dia == 0:
                
                    label = tk.Label(frame_dias, text="", width=4, height=2)
                else:
                    if dia_destacado and dia == dia_destacado:
                        label = tk.Label(
                            frame_dias, text=str(dia), bg="lightblue", fg="black", width=4, height=2,
                            font=('Arial', 10, 'bold')
                        )
                    else:
                        label = tk.Label(frame_dias, text=str(dia), width=4, height=2)
                label.grid(row=fila, column=col, padx=2, pady=2)

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

ventana = tk.Tk()
ventana.title("Calendario Visual Interactivo")

tk.Label(ventana, text="Año:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_año = tk.Entry(ventana)
entry_año.grid(row=0, column=1, padx=5)

tk.Label(ventana, text="Mes (1-12):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_mes = tk.Entry(ventana)
entry_mes.grid(row=1, column=1, padx=5)

tk.Label(ventana, text="Día a destacar (opcional):").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_dia = tk.Entry(ventana)
entry_dia.grid(row=2, column=1, padx=5)

btn_mostrar = tk.Button(ventana, text="Mostrar Calendario", command=mostrar_calendario)
btn_mostrar.grid(row=3, column=0, columnspan=2, pady=10)

frame_dias = tk.Frame(ventana)
frame_dias.grid(row=4, column=0, columnspan=2, pady=10)

ventana.mainloop()