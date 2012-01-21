def initiate(rows, columns)
  
  grid = Array.new
  
  rows.times do |row|
    grid[row] = Array.new
    columns.times do |column|
      # grid[row][column] = Random.new.rand(2) == 1 ? true : false
      grid[row][column] = Random.new.rand(2)
    end    
  end
  
  grid
end

def render(grid)
  # puts grid.map { |row| row.map {|cell| cell ? '1' : '0' }.join }.join "\n"
  puts grid.map { |row|.join }.join "\n"
end

def next_state(cell_x, cell_y)
  
end



def count_neighbors(grid, row, column)
  

  # subgrid = grid[row-1..row+1].map { |row| row[column-1..column+1] }  
  subgrid = grid[[0,row-1].max..[grid.length-1,row+1].min].map { |row| row[[0, column-1].max..[row.length,column+1].min] }  
  
  
  
  sugrid.sum
end

def game
  grid = initiate(10, 10)
  render(grid)
  subgrid = count_neighbors(grid, 0, 0)
  puts 
  render(subgrid)
end

game