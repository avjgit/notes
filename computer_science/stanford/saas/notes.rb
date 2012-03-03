# Week One:  




# Engineering SW is Different from HW (§1.1-§1.2) 
  cost of update




# Development Processes: Waterfall vs. Agile (§1.3)  
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




# Assurance (§1.4)  
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


# Productivity (§1.5)  
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

    
    
# Software as a Service (§1.6)  
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



# Service Oriented Architecture (§1.7)  




# Cloud Computing (§1.8)  




# Client-Server Architecture, HTTP, URIs, Cookies (§2.1-2.2)  




# HTML & CSS, XML & XPath (§2.2-2.3)  




# 3-tier shared-nothing architecture, horizontal scaling (§2.4)  





# Week Two:  




# Three pillars of Ruby (§3.1)  




# Everything is an object, and every operation is a method call (§3.2–3.3)  




# OOP in Ruby (§3.4)  




# Reflection and metaprogramming (§3.5)  




# Functional idioms and iterators (§3.6)  




# Model-View-Controller Design Pattern (§2.5)  




# Models: ActiveRecord and CRUD (§2.6)  




# Routes, Controllers and REST (§2.7)  




# Template Views (§2.8)  




# Homework 1: In this homework you will do some simple programming exercises to get familiar with the Ruby language. We will provide detailed automatic grading of your code.  
  




# Week Three:  




# Duck typing and mix-ins (§3.7)  




# Blocks and Yield (§3.8)  




# Rails Basics: Routes & REST (§3.9)  




# Databases and Migrations (§3.10)  




# ActiveRecord Basics (§3.11)  




# Controllers and Views (§3.12)  




# When things go wrong: Debugging (§3.13)  




# Forms (§3.14)  




# Redirection, the Flash and the Session (§3.15)  




# Finishing CRUD (§3.16)  




# Homework 2: In this homework you will clone a GitHub repo containing an existing simple Rails app, add a feature to the app, and deploy the result publicly on the Heroku platform. We will run live integration tests against your deployed version.  
  




# Week Four:  




# Introduction to Behavior-Driven Design and User Stories (§4.1)  




# SMART User Stories (§4.2)  




# Introducing and Running Cucumber and Capybara (§4.3-§4.4)  




# Lo-Fi UI Sketches and Storyboards (§4.5)  




# Enhancing Rotten Potatoes Again (§4.6)  




# Explicit vs. Implicit and Imperative vs. Declarative Scenarios (§4.7)  




# Fallacies & Pitfalls, BDD Pros & Cons (§4.8-§4.9)  




# Homework 3: In this homework you will create user stories to describe a feature of a SaaS app, use the Cucumber tool to turn those stories into executable acceptance tests, and run the tests against your SaaS app.  
  




# Week Five:  




# Testing Overview (§5.1)  




# FIRST, TDD and Getting Started with RSpec (§5.2)  




# The TDD Cycle: Red-Green-Refactor (§5.3)  




# More Controller Specs and Refactoring (§5.4)  




# Fixtures and Factories (§5.5)  




# TDD for the Model & Stubbing the Internet (§5.6-§5.7)  




# Coverage, Unit vs. Integration Tests, Other Testing Concepts, and Perspectives (§5.8-§5.11)  




# Homework 4: In this homework you will use a combination of Behavior-Driven Design (BDD) and Test-Driven Development (TDD) with the Cucumber and RSpec tools to add a new feature to a SaaS app, and deploy the resulting app on Heroku.  
  




# Homework 5: In this homework you will add more advanced features to a SaaS app, including associations among different entity types, third-party authentication such as Facebook Connect, and some JavaScript/AJAX functionality (exact details of HW 5 are still TBD).