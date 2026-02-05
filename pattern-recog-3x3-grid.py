"""WAP to recognise sequence of 3 x 3 grid pattern using tkinter 
and capture sequence in live output for multiple inputs"""

import tkinter as tk

class GridPatternRecog:
    def __init__(self, root):
        self.root=root
        self.root.title("Interactive 3 x 3 Pattern Grid system recognizer: ")
        self.canvas=tk.Canvas(root,width=300,height=300,bg="white")
        self.canvas.pack()
        self.dots=[]    #store the ID of the dots on canvas
        self.dot_coords=[]  #store x,y coords
        self.pattern=[] #store the sequence selected dots
        self.lines=[]   #store the line segments

        #3x3 grid formation
        for i in range(3):
            for j in range(3):
                x, y=50+j*100,50 +i*100
                dot=self.canvas.create_oval(x-10,y-10 ,x+10,y+ 10,fill="blue")
                self.dots.append(dot)
                self.dot_coords.append((x,y))
        #mouse-key binding (response to input)
        self.canvas.bind("<Button-1>", self.start_pattern)
        self.canvas.bind("<B1-Motion>", self.continue_pattern)
        self.canvas.bind("<ButtonRelease-1>", self.end_pattern)

    def if_clicked(self, x, y):
        """chks if cursor is in 20 px radius of any of prevailing dots..."""
        for i, (dx, dy) in enumerate(self.dot_coords):
            if abs(x - dx) < 20 and abs(y - dy) < 20:
                return i
        return None

    def start_pattern(self,event): # starts line
        self.reset_ui()
        dot_idx=self.if_clicked(event.x, event.y)
        if dot_idx is not None:
            self.add_pt(dot_idx)

    def continue_pattern(self, event): #continues line
        dot_idx=self.if_clicked(event.x, event.y)
        
        # def hover()
        if dot_idx is not None and dot_idx not in self.pattern:
            self.add_pt(dot_idx)
        
        # draw line (for guiding user) 
        if self.pattern:
            self.update_temp_line(event.x,event.y)

    def add_pt(self,idx):
        self.pattern.append(idx)
        self.canvas.itemconfig(self.dots[idx], fill="blue") # Highlight dot
        
        # If there's more than one dot, draw a permanent line between them
        if len(self.pattern)>1:
            p1=self.dot_coords[self.pattern[-2]]
            p2=self.dot_coords[self.pattern[-1]]
            line=self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="blue", width=3)
            self.lines.append(line)

    def update_temp_line(self,x, y):
        # Remove old temporary line and draw new one to mouse cursor
        self.canvas.delete("temp_line")
        last_dot=self.dot_coords[self.pattern[-1]]
        self.canvas.create_line(last_dot[0], last_dot[1], x, y, fill="lightblue", dash=(4, 4), tags="temp_line")

    def end_pattern(self,event):
        self.canvas.delete("temp_line")
        print(f"Pattern Captured: {self.pattern}")
        # You could add logic here to check if the pattern matches a password!

#reset ui
    def reset_ui(self):
        """Clears lines and resets dot colors."""
        for line in self.lines:
            self.canvas.delete(line)
        for dot in self.dots:
            self.canvas.itemconfig(dot, fill="gray")
        self.pattern=[]
        self.lines=[]

if __name__ == "__main__":
    root=tk.Tk()
    app=GridPatternRecog(root)
    root.mainloop()