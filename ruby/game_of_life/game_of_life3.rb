class Cell
  def initialize(x, y)
    @x = x
    @y = y
  end
  
  def order 
    @x*10 + @y
  end  
  
  def x
    @x
  end
  
  def y
    @y
  end
  
 
  def status
    @status
  end
  attr_accessor :status

end

class LivingCell < Cell
  def initialize(x, y)
    super(x, y)
    @status = 1
  end
end

class DeadCell < Cell
  def initialize(x, y)
    super(x, y)
    @status = 0
  end
end

class World
  
  
  def initialize(x, y)
    @world = Array.new
    
    x.times do |x|
      y.times do |y|
        @world << (Random.new.rand(2) == 1 ? LivingCell.new(x, y) : DeadCell.new(x, y))
        
        # puts @world.size
      end
    end
  end
  
  
  def initialize_next
    @world.each do |cell| 
      world_new << cell.will_live ? LivingCell.new(cell.x, cell.y) : DeadCell.new(cell.x, cell.y)
    end
  end
  
  def render
    
    # @world.sort_by! {|cell|  cell.order} 
    
    @world.each do |cell|
      puts if cell.y == 0
      # print cell.status.to_s + ': ' + cell.x.to_s + ', ' + cell.y.to_s
      print cell.status.to_s
    end   
    
  end
end

# def test
  # myworld = World.new(20, 20)
  # myworld.initialize(20, 20)
# end
World.new(20, 20).render

# cell = LivingCell(1,1).new
# puts cell.status

# cell = Cell.new(1, 1)
# cell.status = 123
# puts cell.status