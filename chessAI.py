from tkinter import *

class Cell():
    FILLED_COLOR_BG = "green"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"

    

    def __init__(self, master, x, y, size):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill= False
      
        
      

    def _switch(self):
        """ Switch if the cell is filled or not. """
        self.fill= not self.fill

    def draw(self, piece):
        """ order to the cell to draw its representation on the canvas """
        if self.master != None :
            fill = Cell.FILLED_COLOR_BG
            outline = Cell.FILLED_COLOR_BORDER

            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size +5
            xmax = xmin + self.size
            ymin = self.ord * self.size +5 
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)
            self.master.create_text(xmin +20, ymin +20, text=piece, fill="black", anchor=NW , font="Helvetica 10 bold underline")
           

class CellGrid(Canvas):
    currentState = [[0 for x in range(8)] for y in range(8)]
    selectState = 0
    selectedCell = 0
    turn = 0
    def __init__(self,master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))

            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []

        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)  
        #bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of midified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        for rowCount in range(8):
            for columnCount in range(8):
                self.currentState[rowCount][columnCount]=""
        self.currentState[0][0] = "WR1"
        self.currentState[0][1] = "WN1"
        self.currentState[0][2] = "WB1"
        self.currentState[0][3] = "WK"
        self.currentState[0][4] = "WQ"
        self.currentState[0][5] = "WB2"
        self.currentState[0][6] = "WN2"
        self.currentState[0][7] = "WR2"
        self.currentState[1][0] = "WP1"
        self.currentState[1][1] = "WP2"
        self.currentState[1][2] = "WP3"
        self.currentState[1][3] = "WP4"
        self.currentState[1][4] = "WP5"
        self.currentState[1][5] = "WP6"
        self.currentState[1][6] = "WP7"
        self.currentState[1][7] = "WP8"
        
        self.currentState[7][0] = "BR1"
        self.currentState[7][1] = "BN1"
        self.currentState[7][2] = "BB1"
        self.currentState[7][3] = "BK"
        self.currentState[7][4] = "BQ"
        self.currentState[7][5] = "BB2"
        self.currentState[7][6] = "BN2"
        self.currentState[7][7] = "BR2"
        self.currentState[6][0] = "BP1"
        self.currentState[6][1] = "BP2"
        self.currentState[6][2] = "BP3"
        self.currentState[6][3] = "BP4"
        self.currentState[6][4] = "BP5"
        self.currentState[6][5] = "BP6"
        self.currentState[6][6] = "BP7"
        self.currentState[6][7] = "BP8"
        
        
        self.draw()


    def draw(self):
        rowCount=-1
        for row in self.grid:
            rowCount=rowCount+1
            columnCount=-1
            for cell in row:
                columnCount=columnCount+1
                cell.draw(self.currentState[rowCount][columnCount])

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    
    def handleMouseClick(self, event):
       
       if self.turn == 2:
           self.turn = 0
       row, column = self._eventCoords(event)
       self.selectedCell = self.currentState[row][column]
       if (self.selectState == 0):
           self.preRow = row
           self.preColumn = column
           self.Pre_current_State = self.currentState
           self.Pre_selected_Cell = self.currentState[row][column]
           self.selectedCell = self.currentState[row][column]
           
           self.currentState[row] [column] = ""
           
           
           self.selectState=1
       elif (self.selectState == 1):
           self.validMove(row, column)
            
           
            
            
            
            # Call validMove before moving
            #if(self.validMove(row, column)):
                
            
       self.drawboard()
            
       
       # cell._switch()
       # cell.draw()
        #add the cell to the list of cell switched during the click
      # self.switched.append(cell)

    def validMove(self, row, column):
           
            piece = self.selectedCell
            if piece == "":
                piece = "n"
            
            
            if piece[0] == "B" and self.Pre_selected_Cell[0] == "W" and self.turn == 0 or piece[0] == "W" and self.Pre_selected_Cell[0] == "B"  and self.turn == 1 or self.Pre_selected_Cell[0] == "W" and self.turn == 0 or self.Pre_selected_Cell[0] == "B" and self.turn == 1:
                
                if self.Pre_selected_Cell[1] == "R":
                    if self.preRow != row and column == self.preColumn or self.preColumn != column and row == self.preRow:
                        
                        self.currentState[row][column] = self.Pre_selected_Cell
                        self.turn = self.turn + 1
                    else:
                        self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                        print("else")
                if self.Pre_selected_Cell[1] == "B":
                    if self.preRow != row and column != self.preColumn and abs(self.preRow - row) == abs(self.preColumn - column):
                        self.currentState[row][column] = self.Pre_selected_Cell
                        self.turn = self.turn + 1
                    else:
                        self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                        print("else")
                if self.Pre_selected_Cell[1] == "Q":
                    if self.preRow != row and column != self.preColumn and abs(self.preRow - row) == abs(self.preColumn - column) or self.preRow != row and column == self.preColumn or self.preColumn != column and row == self.preRow:
                        self.currentState[row][column] = self.Pre_selected_Cell
                        self.turn = self.turn + 1
                    else:
                        self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                        print("else")
                if self.Pre_selected_Cell[1] == "K":
                    if abs(self.preRow - row) == 1 or abs(self.preColumn - column) == 1:
                        if self.preRow != row and column != self.preColumn and abs(self.preRow - row) == abs(self.preColumn - column) or self.preRow != row and column == self.preColumn or self.preColumn != column and row == self.preRow :
                            self.currentState[row][column] = self.Pre_selected_Cell
                            self.turn = self.turn + 1
                            
                        else:
                            self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                    else:
                            self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                            print("else")
                if self.Pre_selected_Cell[1] == "N":
                    if abs(self.preRow - row) == 2  and abs(column - self.preColumn) == 1 or abs(self.preColumn - column) == 2 and abs(row - self.preRow) == 1:
                        self.currentState[row][column] = self.Pre_selected_Cell
                    else:
                        self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                        print("else")
                        print("Invalid Move")
                if self.Pre_selected_Cell[1] == "P":
                    
                    if self.Pre_selected_Cell[0] == "W":
                        if self.currentState[self.preRow][self.preColumn] == "":
                            if self.preRow + 1 == row and abs(self.preColumn - column) == 1:
                                if self.selectedCell[0] == "B":
                                    self.currentState[row][column] = self.Pre_selected_Cell
                                    self.turn = self.turn + 1
                            elif self.preColumn - column == 0 and self.preRow + 1 == row:
                                self.currentState[row][column] = self.Pre_selected_Cell
                                self.turn = self.turn + 1
                            
                            elif self.preColumn - column == 0 and self.preRow + 2 == row:
                                if self.preRow == 1:
                                    self.currentState[row][column] = self.Pre_selected_Cell
                                    self.turn = self.turn + 1
                                else:
                                    self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                                
                            else:
                                self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                        else:
                            
                    if self.Pre_selected_Cell[0] == "B":
                        if self.currentState[self.preRow - 1][column] != "":
                            self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                        else:
                            if self.preRow - 1 == row and abs(self.preColumn - column) == 1:
                                if self.selectedCell[0] == "W":
                                    self.currentState[row][column] = self.Pre_selected_Cell
                                    self.turn = self.turn + 1
                            elif self.preColumn - column == 0 and self.preRow - 1 == row:
                                self.currentState[row][column] = self.Pre_selected_Cell
                                self.turn = self.turn + 1
                            
                            elif self.preColumn - column == 0 and self.preRow - 2 == row:
                                if self.preRow == 6:
                                    self.currentState[row][column] = self.Pre_selected_Cell
                                    self.turn = self.turn + 1
                                else:
                                    self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                                
                            else:
                                self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
                            
                    
                    
                    
                        

                    
                    
                
            else:
                self.currentState[self.preRow][self.preColumn] = self.Pre_selected_Cell
            
            self.selectState=0
    

        
    def handleMouseMotion(self, event):
       row, column = self._eventCoords(event)
       # cell = self.grid[row][column]

       # if cell not in self.switched:
        #    cell._switch()
          #  cell.draw()
           # self.switched.append(cell)

    def drag(self, event):
        row, column = self._eventCoords(event)
        widget = event.widget
        xc = widget.canvasx(event.x);
        yc = widget.canvasx(event.y)
        canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
        self.previous = (xc, yc)

    def drawboard(self):
 
        cellCount=1
        rowCount=-1
        for row in self.grid:
            rowCount=rowCount+1
            columnCount=-1
            cellCount = cellCount + 1
            for cell in row:
                cellCount=cellCount +1
                columnCount=columnCount+1
                if(cellCount%2==0):
                    cell._switch()
                cell.draw(self.currentState[rowCount][columnCount])

if __name__ == "__main__" :
    app = Tk()

    grid = CellGrid(app, 8, 8, 60)
    grid.pack()
    grid.drawboard()

    app.mainloop()
