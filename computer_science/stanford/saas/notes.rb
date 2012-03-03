# Chapter One - Engineering Software is Different from Engineering Hardware



###1.1, 1.2 - Introduction - Engineering Software is Different from Engineering Hardware  
    cost of update


###1.3 - Development Processes: Waterfall vs. Agile  
  waterfall:
  - requirements analysis
  - architectural design
  - implementation
  - verification
  - operation and maintanance
  
  works well for things that would not change:
    embedded, NASA, aircraft
    
  agile: 
    individuals over processes
    working software over documentation
    collaboration over contracts
    responding to change over plan  
    
    items on the right still have value
    
    uses written requirements too (user stories)



###1.4 - Assurance  
  verification: is thing built right? (according to specs)
  validation:   is right thing built? (are specs correct?)

  levels:
    unittest (single method)
    module/ or functional: single unit
    integration: interfaces between units
    system/ acceptance: whole system
    
    coverage
    regression testing
    continuous integration
    tdd (tests before)
    
    "With testing, you can't prove there are no bugs, you can prove only that there are"



###1.5 - Productivity  
  techniques:
    clarity via conciseness
      syntax ("a.should be > 7" better than "assert.greater_or_equal(a, 7)")
      abstraction level (higher level languages)
    synthesis
    reuse
      procedures
      libraries
      OOP
      design patterns
    automation and tools

    DRY



###1.6 - Software as a Service  
  traditional: on client device
  saas: through internet
    no installation worries
    no data loss worries
    simple upgrades for devs
    simple upgrades for users
  ruby
    scripting
    oop
    functional
    dynamic types
    mixins (for reuse)
    metaprogramming



###1.7 - Service-Oriented Architecture  
  SOA: architecture, where all components are designed to be a service
  amazon usecase
    subsystems independent, as if in separate datacenters



###1.8, 1.9, 1.12 - Cloud Computing, Fallacies and Pitfalls  
  lot of common computers is cheaper then big one
  ... and common known stuff like adding people to late project makes it later


# Chapter Two - SaaS Architecture



###2.1, 2.2 - The Web as a Client-Server System; TCP/IP Introduction  
  web: client-server arch.
  request-reply oriented
  DNS (Domain Name system) in the middle - maps names to addresses
  IP (Internet protocol) address, four octets - 128.32.244.172
  127.0.0.1 - "this computer"
  TCP - Transmission Control protocol
  HTTP
    requests
      GET
      POSt
      URI (=URL)
      header
    responses
      protocol version
      status code
      header
      body
    status codes
      2xx - ok
      3xx - resource m.
      4xx - access problems
      5xx - server errors
  
  NetCat
  
  HTTP is stateless
  
  Cookies
  
  

###2.3 - HTML and CSS  
  IBM GML 60-ies
  SGML 1986
  
  CSS: apply per
    tag name <h1>
    class name .pageFrame
    element ID #pageHead
    tage name & class div.pageFrame
    tag name & id span#custName
    descendant relationship: "div .custName"
      search for and ID inside of a div
      
      <p class="a">foo,
        <span class="a">bar</span></p>
      which selector will select ONLY "bar"?
        span.a
        p .a
        .a span
        > all
    


###2.4 - 3-tiered Shared-Nothing Architecture and Scaling  
  Load Balancer could be used between each tier
    presentation
    logic
    persistence
  
  Sharding vs Replication


###2.5 - Model-View-Controller Architecture  
  alternatives:
    page controller (Sinatra)
    front controller (J2EE)
    template view (PHP)


###2.6 - Models, Databases and ActiveRecord  
  marshal = serialize
  Active records = every model knows how to CRUD itself
  each model gets it''s own db table
  column is attribute
  Rails add ID
  Schema: collection of all tables
  
  RDBMS is hard to scale
  
  alternative: DataMapper, used by Google


###2.7 - Controllers, Routes and RESTfulness  
  route 
    maps HTTP method + URI to controller action
      GET  /movies/3    - show movie 3
      POST /movies      - create new
      PUT  /movies/5    - update movie
      DELETE /movies/5
      
  Representational State Transfer
  If you can see an URI and say, what''s is going to do
  Amazon antipattern
    Same URI does different things depending on internal state
  
  Controllers ties models and views together via routes
  
###2.8 - Templates, Views and HAML  
  HAML - highly specified HTML. HTML on a diet
    %h1.pagename All Movies
    %table#movies
      %thead
        %th Movie Title
        %th Release DAte
        %th More Info
      %tbody
  RJS - remote Javascript

  Helper methods

  Are Haml with erb

###Summary and Reflections: SaaS Architecture  



# Chapter Three - Ruby and Rails Basics



###3.1 - Ruby 101  
  interpreted
  oop
    everything is an object
  dynamically typed: objects typed, variables - not
  dynamic
    modify code at runtime (metaprogramming)
    ask objects about themselves (reflection)
  
  
  conventions
    ClassNames
    method_names
    var_names ("snake case")
    bool_methods?
    changing_methods!
    CONSTANTS
    $SUPER_GLOBALS
    :symbols__mmutable_string
      to_s
      to_sym
      :rails == "rails" # => false
    
    
    vars must be asisgned before use
    class instances are nil until assignement
    
    array - can contain different types
    
    hash
      w = {'a' => 1, :b => [2, 3]}
      basically, hash are arrays where keys should be anyghing, not necessary integers
      
    everyghing, except fixnums, is passed by reference

    a = 41; "the answer is #{a+1}"

    rx = {:fox => /^arm/, 'fox' => [%r{AN(DO)$}, /an(do)/i]}
    Which expression will evaluate to non-nil?
    "armando" =~ rx{:fox}
     
    rx[:fox][1] =~ "ARMANDO"
     
    > rx['fox'][1] =~ "ARMANDO"
     
    "armando" =~ rx['fox', 1]
 
 
###3.2, 3.3 - Ruby Objects and Methods  
  all is a object - so, "57.methods" works
  my_str.length => my_str.send(:length)
  1 + 2         => 1.send(:+, 2)
  my_array[4]   => my_array.send(:[], 4)
  
  a.b
    calling method b on object a
    b is not an instance variable a
    a is not data structure, that has b as a member
    a is receiver to which I send method call, assuming a will respond

    
  instance members, not language operators
  so,
    5 + 3
    "a" + "b"
    [a,b] + [c] all are different methods named '+'
    
  
  a.should(be.send(:>=, 7))
  a.should(be() >= 7)
  a.should be >= 7
  
  
  def foo(arg, hash1, hash2)
  ...
  end
  Which is NOT a legal call to foo()?
    foo a, {:x => 1, :y => 2}, :z => 3
     
    foo(a, :x => 1, :y =>2, :z => 3)
     
    foo(a, {:x => 1, :y => 2}, {:z => 3})
     
    foo(a, {:x => 1}, {:y =>2, :z => 3})
   

###3.4 - Object Oriented Programming in Ruby  
  class SavingsAccount < Account #inheritance
  #constructor
  def initialize(starting_balance = 0)
    @balance = starting_balance
  end
  def balance #setter
    @balance
  end
  def balance=(new_amount) #setter
    @balance = new_amount
  end
  
  # or
  attr_accessor :balance #getter, setter
  
  def deposit(amount)
    @balance += amount
  end
  
  @@bank_name = "MyBank.com" #static variable
  def self.bank_name
  
  end
  
  
  no multiple inheritence


###3.5 - Ruby Metaprogramming  



###3.6 - Ruby Blocks, Iterators, Functional Idioms   


