class Cell(x, y)
    # @live = live
    @x = x
    @y = y
    # live_next boolean
  def calculate_next_state(world)
    n1 = world
    n2
    n3
    n4
    n5
    n6
    n7
    n7
    
    world.each |cell| do
    
    
      (-1..1) do |x|
        (-1..1) do |y|
          world.include?(c)
        end
      end 
    
      if (
        ((cell.x == x-1) && (cell.y == y-1)) or
        ((cell.x == x)   && (cell.y == y-1)) or
        ((cell.x == x+1) && (cell.y == y-1)) or
        ((cell.x == x-1) && (cell.y == y))   or
        ((cell.x == x+1) && (cell.y == y)) or
        ((cell.x == x-1) && (cell.y == y-1)) or
        ((cell.x == x)   && (cell.y == y-1))
      )
          neighbors += cell.is_a?(LivingCell) ? 1 : 0
      end if
      
    end
  end
end

class LivingCell << Cell  
end

class DeadCell << Cell
end

class World
  def initialize(rows, cols)
    @rows = rows
    @cols = cols
    @world = []
    
    rows.each do |row|
      cols.each do |column|
        cell = Random.new.rand(2)==1 ? LivingCell.net : DeadCell.new        
        @world << cell(row, column)
      end
    end
  end  
  
  def initialize_new
    @world.each do |cell|
      new_world << cell.calculate_next_state == 1 ? LivingCell.new(cell.x, cell.y) : DeadCell.new(cell.x, cell.y)
  end
end

class Turn(world)
  # calculate_next_status
  # set_next_status
  
 
end