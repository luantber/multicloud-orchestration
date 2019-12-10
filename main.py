from matchmaking.Match import match 
import orchestation.planner as planner

spec = "specification.json"
match_spec = match(spec,use_cache=True)

planner.create_plan(match_spec)
planner.execute_plan()

