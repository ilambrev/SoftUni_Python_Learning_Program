actor_name = input()
actor_score = float(input())
jury_members_count = int(input())

is_actor_nominated = actor_score >= 1250.5

if not is_actor_nominated:
    for _ in range(jury_members_count):
        jury_member_name = input()
        jury_memper_score = float(input())
        actor_score += len(jury_member_name) * jury_memper_score / 2
        
        if actor_score >= 1250.5:
            is_actor_nominated = True
            break

if is_actor_nominated:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {actor_score:.1f}!')
else:
    difference = 1250.5 - actor_score
    print(f'Sorry, {actor_name} you need {difference:.1f} more!')