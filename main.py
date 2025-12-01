import customtkinter as ctk
from tkinter import ttk
import backend
import threading
import time

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class PortManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Windows Port Manager")
        self.geometry("900x600")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Top Control Panel
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.refresh_btn = ctk.CTkButton(self.top_frame, text="Refresh", command=self.refresh_data)
        self.refresh_btn.pack(side="left", padx=10)

        self.export_btn = ctk.CTkButton(self.top_frame, text="Export CSV", command=self.export_data)
        self.export_btn.pack(side="left", padx=10)

        self.kill_all_btn = ctk.CTkButton(self.top_frame, text="Kill All (Same Name)", fg_color="#D32F2F", hover_color="#B71C1C", command=self.kill_all_by_name)
        self.kill_all_btn.pack(side="right", padx=10)
        self.kill_all_btn.configure(state="disabled")

        self.kill_btn = ctk.CTkButton(self.top_frame, text="Kill Selected Process", fg_color="red", hover_color="darkred", command=self.kill_selected_process)
        self.kill_btn.pack(side="right", padx=10)
        self.kill_btn.configure(state="disabled")

        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Search (Port or Name)", textvariable=self.search_var)
        self.search_entry.pack(side="left", padx=10, fill="x", expand=True)
        self.search_entry.bind("<KeyRelease>", self.filter_data)

        # Data View (Treeview)
        # CustomTkinter doesn't have a Treeview, so we use ttk.Treeview with some styling
        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
        self.tree_frame.grid_columnconfigure(0, weight=1)
        self.tree_frame.grid_rowconfigure(0, weight=1)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#2b2b2b", fieldbackground="#2b2b2b", foreground="white", rowheight=25, borderwidth=0)
        self.style.map('Treeview', background=[('selected', '#1f538d')])
        self.style.configure("Treeview.Heading", background="#333333", foreground="white", relief="flat")
        self.style.map("Treeview.Heading", background=[('active', '#333333')])

        self.columns = ("pid", "name", "port", "protocol", "status", "local_address", "importance", "description")
        self.tree = ttk.Treeview(self.tree_frame, columns=self.columns, show="headings", selectmode="browse")
        
        self.tree.heading("pid", text="PID")
        self.tree.heading("name", text="Process Name")
        self.tree.heading("port", text="Port")
        self.tree.heading("protocol", text="Protocol")
        self.tree.heading("status", text="Status")
        self.tree.heading("local_address", text="Local Address")
        self.tree.heading("importance", text="Importance")
        self.tree.heading("description", text="Description")

        self.tree.column("pid", width=60, anchor="center")
        self.tree.column("name", width=150, anchor="w")
        self.tree.column("port", width=60, anchor="center")
        self.tree.column("protocol", width=60, anchor="center")
        self.tree.column("status", width=80, anchor="center")
        self.tree.column("local_address", width=120, anchor="w")
        self.tree.column("importance", width=80, anchor="center")
        self.tree.column("description", width=250, anchor="w")

        self.tree.grid(row=0, column=0, sticky="nsew")

        # Scrollbar
        self.scrollbar = ctk.CTkScrollbar(self.tree_frame, orientation="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Horizontal Scrollbar
        self.h_scrollbar = ctk.CTkScrollbar(self.tree_frame, orientation="horizontal", command=self.tree.xview)
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")
        self.tree.configure(xscrollcommand=self.h_scrollbar.set)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # Status Bar
        self.status_label = ctk.CTkLabel(self, text="Ready", anchor="w")
        self.status_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        # Data storage
        self.all_data = []

        # Initial Load
        self.refresh_data()

    def refresh_data(self):
        self.status_label.configure(text="Refreshing...")
        self.kill_btn.configure(state="disabled")
        # Run in thread to avoid freezing UI
        threading.Thread(target=self._fetch_data_thread, daemon=True).start()

    def _fetch_data_thread(self):
        data = backend.get_port_info()
        self.all_data = data
        self.after(0, self.update_tree, data)

    def update_tree(self, data):
        # Clear existing
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        search_term = self.search_var.get().lower()

        for item in data:
            # Filter
            if search_term:
                if (search_term not in str(item['pid']) and 
                    search_term not in item['name'].lower() and 
                    search_term not in str(item['port'])):
                    continue

            # Color coding for importance (optional, but ttk treeview row tags are tricky with custom colors in some themes)
            # For now just display text
            
            self.tree.insert("", "end", values=(
                item['pid'],
                item['name'],
                item['port'],
                item['protocol'],
                item['status'],
                item['local_address'],
                item['importance'],
                item['description']
            ))
        
        self.status_label.configure(text=f"Found {len(data)} connections.")

    def filter_data(self, event=None):
        self.update_tree(self.all_data)

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            importance = item['values'][6] # Index 6 is importance
            
            if importance == "不可kill":
                self.kill_btn.configure(state="disabled", text="Cannot Kill")
                self.kill_all_btn.configure(state="disabled")
            else:
                self.kill_btn.configure(state="normal", text="Kill Selected Process")
                self.kill_all_btn.configure(state="normal")
        else:
            self.kill_btn.configure(state="disabled", text="Kill Selected Process")
            self.kill_all_btn.configure(state="disabled")

    def export_data(self):
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not filename:
            return
        
        success, msg = backend.export_to_csv(self.all_data, filename)
        self.status_label.configure(text=msg)

    def kill_selected_process(self):
        selected = self.tree.selection()
        if not selected:
            return
        
        item = self.tree.item(selected[0])
        pid = item['values'][0]
        name = item['values'][1]
        
        success, msg = backend.kill_process(pid)
        self.status_label.configure(text=msg)
        
        if success:
            self.refresh_data()

    def kill_all_by_name(self):
        selected = self.tree.selection()
        if not selected:
            return
        
        item = self.tree.item(selected[0])
        name = item['values'][1]
        
        # Optional: Confirm dialog could go here
        
        success, msg = backend.kill_process_by_name(name)
        self.status_label.configure(text=msg)
        
        if success:
            self.refresh_data()


def is_admin():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin():
        app = PortManagerApp()
        app.mainloop()
    else:
        # Re-run the program with admin rights
        import ctypes
        import sys
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

