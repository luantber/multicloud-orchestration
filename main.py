from matchmaking.Match import match 
from orchestation.planner import create_plan,execute_plan

spec = "specification.json"
match_spec = match(spec,use_cache=True)
create_plan(match_spec)

execute_plan()

