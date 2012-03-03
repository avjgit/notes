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



###3.2, 3.3 - Ruby Objects and Methods  



###3.4 - Object Oriented Programming in Ruby  



###3.5 - Ruby Metaprogramming  



###3.6 - Ruby Blocks, Iterators, Functional Idioms   


