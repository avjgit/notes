##sendto: sandra.ose.z@gmail.com
class Cell
  attr :x
  attr :y
  
  def initialize(x, y)
    @x = x
    @y = y
    
    # NN = false
    # NE = false
    # EE = false
    # ES = false
    # SS = false
    # SW = false
    # WW = false
    # WN = false
  end
end

class LivingCell < Cell
end

class DeadCell < Cell
end

class World
  
  attr :world
  
  def initialize(x, y)
    @world = Array.new
    x.times do |x|
      y.times do |y|
        @world << (Random.new.rand(2) == 0 ? LivingCell.new(x, y) : DeadCell.new(x, y))
      end
    end
  end
  
  def neighbors
    @world.each do |cell|
      (-1..1).each do |x|
        (-1..1).each do |y|
          if c
          cell.x+x, cell.y+y
        end
      end
    end
  end
  
  def render
    @world.each do |cell|
      if cell.y == 0
        puts
      end
      print cell.is_a?(LivingCell) ? 1 : 0
    end
  end
  
end

World.new(10, 10).render
