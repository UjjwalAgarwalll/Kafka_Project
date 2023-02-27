import tkinter as tk
import kafka_producer

#Creating the window

window = tk.Tk()
window.title("Find the mth Prime Number from N")


#Creating input fields and labels

n_label = tk.Label(window, text="Enter the value of n:")
n_label.grid(row=0, column=0, padx=5, pady=5)
n_entry = tk.Entry(window)
n_entry.grid(row=0, column=1, padx=5, pady=5)

m_label = tk.Label(window, text="Enter the value of m:")
m_label.grid(row=1, column=0, padx=5, pady=5)
m_entry = tk.Entry(window)
m_entry.grid(row=1, column=1, padx=5, pady=5)


#Sending the data to kafka producer

def send_message():
    n = int(n_entry.get())
    m = int(m_entry.get())
    input_data = f"{n},{m}"
    kafka_producer.sender(input_data)


run_button = tk.Button(window, text="Find the mth Prime Number", command=send_message)
run_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


window.mainloop()