# bball_stats

## Infrastructure

1. Stats input app
2. Database
3. Stats website

## Stats input

### Main entities

- Match
  - Basketball
    - 4 x 4
    - 5 x 5
    - 4 x 5
    - 5 x 4
  - Streetball
    - 1 x 1
    - 2 x 2
    - 3 x 3
    - 3 x 4
    - 4 x 3  

- Person
  - Player
  - Referee

- Player stats and data

#### Game events

- Shot
  - Missed
    - Assist 
    - Defender
    - Rebound
    - Zone
    - Type of shot (jump shot, floater) 
    - Blocked by
  - Made
- Turnover
  - Stealed by
  - Assist
  - Type of
- Foul
  - On 
  - By
  - Offensive | Defensive
- Substitution
  - In
  - Out 
- Jump Ball
  - Player1
  - Player2
  - WinnedBy 

### Specification

- Video player
  - 1-2 camera? How to handle?
- Time line
- Score board
- Events
- Multi User interface
  - Conflicts 
