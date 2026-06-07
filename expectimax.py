tree = {
    "RouteA": {
        "Clear": {
            "prob": 0.5,
            "actions": {
                "Slow": 70,
                "Normal": [(0.8, 100), (0.2, 50)],
                "Fast": [(0.6, 140), (0.4, -30)]
            }
        },
        "Windy": {
            "prob": 0.3,
            "actions": {
                "Slow": 60,
                "Normal": [(0.6, 90), (0.4, 40)],
                "Fast": [(0.3, 150), (0.7, -50)]
            }
        },
        "Storm": {
            "prob": 0.2,
            "actions": {
                "Slow": 40,
                "Normal": [(0.5, 80), (0.5, 20)],
                "Fast": [(0.2, 130), (0.8, -80)]
            }
        }
    },

    "RouteB": {
        "Low": {
            "prob": 0.4,
            "actions": {
                "Slow": 65,
                "Normal": [(0.7, 110), (0.3, 60)],
                "Fast": [(0.5, 150), (0.5, -20)]
            }
        },
        "Moderate": {
            "prob": 0.4,
            "actions": {
                "Slow": 60,
                "Normal": [(0.6, 100), (0.4, 40)],
                "Fast": [(0.4, 140), (0.6, -40)]
            }
        },
        "Heavy": {
            "prob": 0.2,
            "actions": {
                "Slow": 50,
                "Normal": [(0.5, 90), (0.5, 30)],
                "Fast": [(0.2, 160), (0.8, -70)]
            }
        }
    }
}

def expected_value(outcome):
# write code here    
    if isinstance(outcome,int):
        return outcome
    t_val=0
    for prob,val in outcome:
        t_val+=prob*val
    return t_val
def expectimax(tree):
# write code here 
    best_route=None
    best_value=-float('inf')
    best_cond=None
    best_speed=None
    for route,conds in tree.items():
        route_exp_value=0
        for cond_name,cond_data in conds.items():
            prob_cond=cond_data['prob']
            action_value=-float('inf')
            action_speed=None
            for speed, outcome in cond_data['actions'].items():
                val = expected_value(outcome)
                if val >action_value:
                    action_value = val
                    action_speed = speed
        
            route_exp_value+=prob_cond*action_value
            
        if route_exp_value > best_value:
            best_value = route_exp_value
            best_route = route
            best_condition = max(conds, key=lambda k: conds[k]['prob'])
            best_speed = max(conds[best_condition]['actions'], 
                             key=lambda s: expected_value(conds[best_condition]['actions'][s]))

    return best_route, best_condition, best_speed, best_value

route,_,_, value = expectimax(tree)

print("Best Route:", route)
print("Expected Value:", round(value,2))
                               
# Run Program
route, condition, speed, value = expectimax(tree)

print("Best Route:", route)
print("Best Condition:", condition)
print("Best Speed:", speed)
print("Expected Value:", round(value, 2))

print("\nDecision Path:")
print("Start →", route, "→", condition, "→", speed)
